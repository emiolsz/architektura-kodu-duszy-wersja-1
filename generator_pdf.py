"""Generator raportu PDF w układzie kartowym (wariant środkowy z podglądu)."""
import io
import datetime
from xml.sax.saxutils import escape

from flask import send_file
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from dane import KABALA_DICTIONARY
from analiza_opisowa import pobierz_analize_premium

# Rejestruj fonty tylko raz i niezależnie od katalogu uruchomienia.
import os
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
for _name, _file in (("DejaVuSans", "DejaVuSans.ttf"), ("DejaVuSans-Bold", "DejaVuSans-Bold.ttf")):
    if _name not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont(_name, os.path.join(_BASE_DIR, _file)))

PAPIER = colors.HexColor("#FBF8EF")
RAMKA = colors.HexColor("#CDBB96")
BRAZ = colors.HexColor("#6D5635")
CIEMNY = colors.HexColor("#3F3A32")


def _date_parts(value):
    if not value:
        return None
    try:
        dt = datetime.datetime.strptime(value, "%Y-%m-%d")
        return dt.day, dt.month, dt.year
    except (TypeError, ValueError):
        return None


def _profil_z_daty(value, funkcja):
    parts = _date_parts(value)
    return funkcja(*parts) if parts else None


def _safe(value):
    return escape(str(value or ""))


def dodaj_tlo(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.white)
    canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)
    canvas.restoreState()


def _karta(label, key, prof, styles):
    number = prof.get(key)
    info = KABALA_DICTIONARY.get(number, {})
    archetyp = info.get("archetyp", "")
    litera = info.get("litera", "")
    opis_key = {"Prawa": "Prawa", "Lewa": "Lewa", "Talent": "Talent", "Gleboka": "Gleboka", "Wezel": "Wezel", "Tikkun": "Tikkun"}[key]
    opis = pobierz_analize_premium(number, opis_key) if number is not None else "Brak danych."
    lewa = Paragraph(
        f'<font name="DejaVuSans-Bold" color="#5B4932">{_safe(label)}</font><br/>'
        f'<font size="7" color="#9A7945">Wibracja {number} • {_safe(archetyp)} • {_safe(litera)}</font><br/>'
        f'<font size="7">{_safe(opis)}</font>', styles["card"])
    prawa = Paragraph(f'<font name="DejaVuSans-Bold" size="13" color="#9A7945">{number}</font>', styles["number"])
    t = Table([[lewa, prawa]], colWidths=[143*mm, 15*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), PAPIER), ("BOX", (0,0), (-1,-1), 0.65, RAMKA),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("LEFTPADDING", (0,0), (-1,-1), 7),
        ("RIGHTPADDING", (0,0), (-1,-1), 7), ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5), ("LINEBEFORE", (1,0), (1,0), 0.5, RAMKA),
    ]))
    return KeepTogether([t, Spacer(1, 2.5*mm)])


def wybuduj_archiwalny_pdf(typ, imie1, data_ur1, profil_glowny, request_form,
                            funkcja_profil, funkcja_smierc):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=20*mm, leftMargin=20*mm,
                            topMargin=14*mm, bottomMargin=14*mm,
                            title="Raport Architektury Kodu Duszy", author="Soul Decoder")
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="reportTitle", fontName="DejaVuSans-Bold", fontSize=16,
        leading=18, alignment=1, textColor=CIEMNY, spaceAfter=1*mm))
    styles.add(ParagraphStyle(name="subtitle", fontName="DejaVuSans", fontSize=7,
        leading=9, alignment=1, textColor=BRAZ, spaceAfter=4*mm))
    styles.add(ParagraphStyle(name="section", fontName="DejaVuSans-Bold", fontSize=8,
        leading=10, textColor=BRAZ, spaceBefore=1*mm, spaceAfter=2*mm))
    styles.add(ParagraphStyle(name="card", fontName="DejaVuSans", fontSize=7.2,
        leading=9, textColor=CIEMNY))
    styles.add(ParagraphStyle(name="number", fontName="DejaVuSans-Bold", fontSize=13,
        leading=15, alignment=1))
    styles.add(ParagraphStyle(name="footer", fontName="DejaVuSans", fontSize=6,
        textColor=colors.HexColor("#777777")))

    story = [Paragraph("RAPORT ARCHITEKTURY<br/>KODU DUSZY", styles["reportTitle"]),
             Paragraph("PROPOZYCJA • VINTAGE / KSIĘGA", styles["subtitle"])]
    osoby = []
    if profil_glowny:
        pos = _profil_z_daty(request_form.get("d_sm1"), funkcja_smierc)
        osoby.append((imie1 or "Profil główny", "Profil główny", profil_glowny, pos))
    if typ == "PELNY":
        try:
            ile = max(0, min(10, int(request_form.get("d_ile_osob", 0) or 0)))
        except (TypeError, ValueError):
            ile = 0
        for i in range(ile):
            prof = _profil_z_daty(request_form.get(f"d_ur_{i}"), funkcja_profil)
            if prof:
                pos = _profil_z_daty(request_form.get(f"d_sm_{i}"), funkcja_smierc)
                osoby.append((request_form.get(f"d_imie_{i}") or "Osoba", request_form.get(f"d_rel_{i}") or "", prof, pos))

    for idx, (nazwa, rel, prof, pos) in enumerate(osoby):
        if idx:
            story.append(Spacer(1, 3*mm))
        story.append(Paragraph(f"{_safe(nazwa).upper()} — {_safe(rel).upper()}", styles["section"]))
        story.append(Paragraph(f"Data urodzenia: {_safe(data_ur1 if idx == 0 else '')}" if idx == 0 else "", styles["footer"]))
        for label, key in [("PRAWA STRONA • Dar", "Prawa"), ("LEWA STRONA • Karma", "Lewa"),
                           ("TALENT • Kreacja", "Talent"), ("GŁĘBOKA OSOBOWOŚĆ", "Gleboka"),
                           ("WĘZEŁ OPORU • Blokada", "Wezel"), ("TIKKUN • Lekcja Duszy", "Tikkun")]:
            story.append(_karta(label, key, prof, styles))
        if pos:
            num = pos.get("Transformacja")
            info = KABALA_DICTIONARY.get(num, {})
            opis = pobierz_analize_premium(num, "Posag")
            story.append(Paragraph(f"TRANSFORMACJA • Wibracja {num} • {_safe(info.get('archetyp', ''))}", styles["section"]))
            story.append(Paragraph(_safe(opis), styles["card"]))

    if not osoby:
        story.append(Paragraph("Brak poprawnych danych do wygenerowania raportu. Wróć do formularza i oblicz profil ponownie.", styles["card"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(f"SOUL DECODER • RAPORT ARCHITEKTURY KODU DUSZY • {datetime.datetime.now().strftime('%d.%m.%Y')}", styles["footer"]))
    doc.build(story, onFirstPage=dodaj_tlo, onLaterPages=dodaj_tlo)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name=f"Raport_Kodu_Duszy_{typ or 'PELNY'}.pdf", mimetype="application/pdf")
