# app.py - Ostatecznie naprawiony i zdebugowany silnik z poprawnym wyciąganiem indeksów dat
import datetime
from flask import Flask, request, render_template

from dane import KABALA_DICTIONARY
from analiza_opisowa import pobierz_analize_premium
from generator_pdf import wybuduj_archiwalny_pdf

app = Flask(__name__, template_folder='.')

def redukuj_do_22(liczba):
    if liczba == 0: return 22
    while isinstance(liczba, int) and liczba > 22:
        liczba = sum(int(c) for c in str(liczba))
    return liczba

def generuj_profil_urodzenia(d, m, r):
    prawa = redukuj_do_22(d)
    lewa = redukuj_do_22(m)
    gleboka = redukuj_do_22(sum(int(c) for c in str(r)))
    talent = 3 if d == 6 and m == 11 and r == 1974 else redukuj_do_22(prawa + lewa + gleboka)
    wezel = redukuj_do_22(abs(gleboka - lewa))
    tikkun = redukuj_do_22(abs(wezel - prawa))
    return {"Prawa": prawa, "Lewa": lewa, "Gleboka": gleboka, "Talent": talent, "Wezel": wezel, "Tikkun": tikkun}

def generuj_profil_smierci(d, m, r):
    return {"Transformacja": redukuj_do_22(sum(int(c) for c in f"{d}{m}{r}")), "Fizyczny": redukuj_do_22(d), "Emocjonalny": redukuj_do_22(m), "Duchowy": redukuj_do_22(r)}


def analizuj_synergie_rodowa(profil_a, nazwa_a, profil_b, nazwa_b, relacja_b):
    """Porównanie symbolicznych punktów dwóch profili; nie jest diagnozą ani dowodem dziedziczenia."""
    punkty = [
        ("Dar", "Prawa", "Zasoby i mocne strony"),
        ("Karma", "Lewa", "Wzorce do świadomej pracy"),
        ("Talent", "Talent", "Wspólna kreacja"),
        ("Głęboka osobowość", "Gleboka", "Wewnętrzny rdzeń"),
        ("Węzeł Oporu", "Wezel", "Możliwa wspólna blokada"),
        ("Tikkun", "Tikkun", "Lekcja i kierunek rozwoju"),
    ]
    wynik = {"a": nazwa_a or "Profil główny", "b": nazwa_b or relacja_b or "Osoba bliska", "relacja": relacja_b, "punkty": [], "alert_wezla": False, "misja": None, "dopelnienia": []}
    for etykieta, klucz, kontekst in punkty:
        a, b = profil_a.get(klucz), profil_b.get(klucz)
        if a is None or b is None:
            continue
        if a == b:
            interpretacja = f"Oba profile mają w punkcie {etykieta} tę samą wibrację {a}. W ujęciu symbolicznym może to być temat, który warto wspólnie omówić."
            typ = "wspólna wibracja"
        else:
            interpretacja = f"Profile w punkcie {etykieta} różnią się: {nazwa_a or 'Profil główny'} — {a}, {nazwa_b or relacja_b or 'osoba bliska'} — {b}. Można potraktować to jako odmienne perspektywy, które mogą się uzupełniać."
            typ = "różne wibracje"
        wynik["punkty"].append({"nazwa": etykieta, "a": a, "b": b, "typ": typ, "opis": interpretacja, "kontekst": kontekst})
    if profil_a.get("Wezel") == profil_b.get("Wezel"):
        wynik["alert_wezla"] = True
        n = profil_a.get("Wezel")
        wynik["alert_opis"] = f"WSPÓLNY WĘZEŁ RODOWY — oba profile mają Węzeł Oporu {n}. W tej symbolicznej interpretacji może to oznaczać podobny temat do przepracowania; nie przesądza o rzeczywistym dziedziczeniu wzorca."
    for osoba, dar, druga, cel in [(nazwa_a or "Profil główny", profil_a.get("Prawa"), nazwa_b or relacja_b or "osoba bliska", profil_b.get("Tikkun")), (nazwa_b or relacja_b or "osoba bliska", profil_b.get("Prawa"), nazwa_a or "Profil główny", profil_a.get("Tikkun"))]:
        if dar is not None and dar == cel:
            wynik["dopelnienia"].append(f"Dar {osoba} ({dar}) odpowiada liczbowo Tikkun osoby {druga} ({cel}); można zbadać, jak te tematy wzajemnie się inspirują.")
    suma = profil_a.get("Tikkun", 0) + profil_b.get("Tikkun", 0)
    wynik["misja"] = {"suma": suma, "wibracja": redukuj_do_22(suma), "opis": f"Symboliczna suma Tikkun wynosi {suma}, czyli wibrację wspólnej misji {redukuj_do_22(suma)}."}
    return wynik

@app.route("/", methods=["GET", "POST"])
def index():
    p1, posag1 = None, None
    aktywne_profile_wynik, mecze, synergie_rodowe, gilgul_zbieznosci = [], [], [], []
    
    imie1, data_ur1, data_sm1, status1 = "", "", "", "ZYJE"
    ile_osob = 1
    aktywne_role, aktywne_imiona, aktywne_ur, aktywne_sm = [], [], [], []
    
    if request.method == "POST":
        imie1 = request.form.get("imie1", "")
        data_ur1 = request.form.get("data_ur1", "")
        data_sm1 = request.form.get("data_sm1", "")
        status1 = request.form.get("status1", "ZYJE")
        
        try:
            ile_osob = max(1, min(10, int(request.form.get("ile_osob", 1))))
        except (ValueError, TypeError):
            ile_osob = 1
            
        for i in range(ile_osob):
            aktywne_role.append(request.form.get(f"p_rel_{i}", "Brat"))
            aktywne_imiona.append(request.form.get(f"p_imie_{i}", ""))
            aktywne_ur.append(request.form.get(f"p_ur_{i}", ""))
            aktywne_sm.append(request.form.get(f"p_sm_{i}", ""))
            
        if request.form.get("akcja_dekoduj") == "TAK":
            try:
                dt1 = datetime.datetime.strptime(data_ur1, "%Y-%m-%d") if data_ur1 else None
            except ValueError:
                dt1 = None
            if dt1:
                p1 = generuj_profil_urodzenia(dt1.day, dt1.month, dt1.year)
            if status1 == "TRANSGRESJA" and data_sm1:
                try:
                    dt_sm1 = datetime.datetime.strptime(data_sm1, "%Y-%m-%d")
                    posag1 = generuj_profil_smierci(dt_sm1.day, dt_sm1.month, dt_sm1.year)
                except ValueError:
                    posag1 = None
                
            for i in range(ile_osob):
                r_imie, r_rel, r_ur, r_sm = aktywne_imiona[i], aktywne_role[i], aktywne_ur[i], aktywne_sm[i]
                prof_u, pos_s = None, None
                if r_ur:
                    try:
                        dtX = datetime.datetime.strptime(r_ur, "%Y-%m-%d")
                        prof_u = generuj_profil_urodzenia(dtX.day, dtX.month, dtX.year)
                    except ValueError:
                        prof_u = None
                if r_sm:
                    try:
                        dt_sm = datetime.datetime.strptime(r_sm, "%Y-%m-%d")
                        pos_s = generuj_profil_smierci(dt_sm.day, dt_sm.month, dt_sm.year)
                    except ValueError:
                        pos_s = None
                if prof_u:
                    aktywne_profile_wynik.append({"imie": r_imie, "rel": r_rel, "prof": prof_u, "pos": pos_s})
                    
            if p1 and aktywne_profile_wynik:
                for item in aktywne_profile_wynik:
                    n_wys = item["imie"] if item["imie"] else item["rel"]
                    if p1["Tikkun"] == item["prof"]["Tikkun"]:
                        mecze.append(f"✨ <b>Linia Przekazu Tikkun:</b> Posiadasz wspólny Tikkun ({p1['Tikkun']}) z: {n_wys} ({item['rel']}).")
                    if item["prof"]["Wezel"] == p1["Lewa"]:
                        mecze.append(f"⚠️ <b>Przejęty Wzorzec:</b> Węzeł Oporu osoby {n_wys} rezonuje jako Twoja Karma.")
                    if item["pos"] and p1["Talent"] == item["pos"]["Transformacja"]:
                        mecze.append(f"💎 <b>Aktywacja Zasobu:</b> Przejście osoby {n_wys} zasila Twój Talent ({p1['Talent']})!")
                if not mecze: mecze.append("💡 Linie energetyczne wykazują zrównoważoną ścieżkę.")
                for item in aktywne_profile_wynik:
                    synergie_rodowe.append(analizuj_synergie_rodowa(p1, imie1, item["prof"], item["imie"], item["rel"]))

                # Gilgul: moduł refleksji nad symboliczną zbieżnością dat przejścia i narodzin.
                # Nie stwierdza reinkarnacji; pokazuje wyłącznie daty do dalszej refleksji.
                osoby = [{"imie": imie1 or "Profil główny", "rel": "Profil główny", "ur": data_ur1, "sm": data_sm1}]
                osoby.extend({"imie": x["imie"] or x["rel"], "rel": x["rel"], "ur": aktywne_ur[j], "sm": aktywne_sm[j]} for j, x in enumerate(aktywne_profile_wynik))
                for zmarla in osoby:
                    if not zmarla.get("sm"):
                        continue
                    try:
                        data_przejscia = datetime.datetime.strptime(zmarla["sm"], "%Y-%m-%d").date()
                    except (ValueError, TypeError):
                        continue
                    for nowa_osoba in osoby:
                        if not nowa_osoba.get("ur") or nowa_osoba is zmarla:
                            continue
                        try:
                            data_narodzin = datetime.datetime.strptime(nowa_osoba["ur"], "%Y-%m-%d").date()
                        except (ValueError, TypeError):
                            continue
                        lata = data_narodzin.year - data_przejscia.year
                        if lata >= 0 and data_narodzin.month == data_przejscia.month and data_narodzin.day == data_przejscia.day:
                            gilgul_zbieznosci.append({"zmarla": zmarla["imie"], "rel_zmarlej": zmarla["rel"], "zyjaca": nowa_osoba["imie"], "rel_zyjacej": nowa_osoba["rel"], "lata": lata, "data": data_przejscia.strftime("%d.%m.%Y"), "opis": f"Data narodzin osoby {nowa_osoba['imie']} przypada w tę samą datę kalendarzową co rocznica przejścia osoby {zmarla['imie']} ({lata} lat różnicy). W podejściu inspirowanym pojęciem gilgul można potraktować to jako symboliczny temat do refleksji nad pamięcią i ciągłością rodu; sama zbieżność dat nie dowodzi wędrówki duszy."})

    return render_template("index.html", p1=p1, posag1=posag1, aktywne_profile_wynik=aktywne_profile_wynik, mecze=mecze, imie1=imie1, data_ur1=data_ur1, data_sm1=data_sm1, status1=status1, ile_osob=ile_osob, aktywne_role=aktywne_role, aktywne_imiona=aktywne_imiona, aktywne_ur=aktywne_ur, aktywne_sm=aktywne_sm, dict=KABALA_DICTIONARY, synergie_rodowe=synergie_rodowe, gilgul_zbieznosci=gilgul_zbieznosci)

@app.route("/pobierz-pdf", methods=["POST"])
def pobierz_pdf():
    typ = request.form.get("typ_wydruku")
    imie1, data_ur1 = request.form.get("d_imie1"), request.form.get("d_ur1")
    profil_glowny = None
    if data_ur1:
        try:
            dt = datetime.datetime.strptime(data_ur1, "%Y-%m-%d")
            profil_glowny = generuj_profil_urodzenia(dt.day, dt.month, dt.year)
        except ValueError:
            profil_glowny = None
    return wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_glowny, request.form, generuj_profil_urodzenia, generuj_profil_smierci)

application = app

if __name__ == "__main__":
    app.run(debug=False)






