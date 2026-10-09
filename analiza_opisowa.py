# analiza_opisowa.py - opisy premium dla 22 wibracji zwiazanych z 22 znakami alfabetu hebrajskiego

ANALIZY = {
   0: {
        "Prawa": "Aktywuje czysty stan Ain Sof. Twoim kosmicznym darem jest absolutna wolność od rodowych uwarunkowań i nieskończony potencjał kreacji.",
        "Lewa": "Lekcja braku schematów. Wyzwaniem jest porzucenie lęku przed pustką i nauczenie się ufania procesowi życia bez sztywnych planów.",
        "Talent": "Uniwersalny multiplikator. Twój talent pozwala Ci błyskawicznie adaptować się do każdych warunków i zaczynać wszystko od nowa.",
        "Gleboka": "Twoja esencja to Tabula Rasa – czysta, niezapisana karta. Nie ograniczają Cię żadne ziemskie definicje ani blokady.",
        "Wezel": "Opór objawia się jako totalny chaos, brak odpowiedzialności lub ucieczka od rzeczywistości w iluzję.",
        "Tikkun": "Główną misją jest zamanifestowanie pełnej wolności oraz pokazanie rodowi, że można żyć bez niesienia jakiegokolwiek ciężaru.",
        "Posag": "Stan Ain Sof i pełna absolucja rodowa. Przodek wyzerował licznik i pozostawia rodzinie pole wolne od duchowego sabotażu."
    },
    1: {
        "Prawa": "Strumień czystej woli i inicjacji (energia litery Alef). Twoim darem jest potężna siła manifestacji myśli w materii oraz zdolność rozpoczynania nowych cykli ewolucyjnych.",
        "Lewa": "Wyzwanie dotyczy egoizmu, manipulacji słowem oraz lęku przed porażką, który blokuje przed wykonaniem pierwszego kroku.",
        "Talent": "Inicjator i kanał dla Boskiego Światła. Masz wrodzony talent do materializacji idei, przewodzenia i dawania impulsu do działania.",
        "Gleboka": "Twoja najgłębsza esencja to Punkt Początkowy – chwila, w której nienazwany potencjał staje się realną intencją.",
        "Wezel": "Opór manifestuje się jako mentalny paraliż, syndrom oszusta lub chorobliwa potrzeba mentalnej kontroli nad otoczeniem.",
        "Tikkun": "Misja zakłada naukę brania pełnej odpowiedzialności za swoje słowa i czyny oraz używanie siły woli do wznoszenia, a nie dominacji.",
        "Posag": "Posag pioniera i jasnego umysłu. Przodek przełamał rodową stagnację, pozostawiając matrycę odwagi i twórczego intelektu."
    },
    2: {
        "Prawa": "Strumień głębokiej intuicji i empatii (energia litery Bet - Naczynie). Twoim darem jest unikalny radar na emocje innych oraz dar naturalnego uzdrawiania obecnością.",
        "Lewa": "Lekcja radzenia sobie ze skrajnym emocjonalizmem, skrytością, lękami rodzinnymi oraz uzależnieniem od opinii innych.",
        "Talent": "Wybitny strateg i dyplomata. Twój talent to umiejętność czytania między wierszami i budowania harmonijnych sojuszy.",
        "Gleboka": "W głębi duszy Twoja esencja to Czyste Naczynie – strażnik wewnętrznej mądrości, który ufa cichemu głosowi wyższego prowadzenia.",
        "Wezel": "Blokada aktywuje się jako paraliżujący lęk przed odrzuceniem lub całkowite wycofanie się z relacji i ucieczka w samotność.",
        "Tikkun": "Wyzwanie ewolucyjne polega na zbudowaniu silnych, zdrowych granic psychicznych i zaufaniu własnemu wewnętrznemu głosowi.",
        "Posag": "Potencjał relacyjności, partnerstwa i mądrości. Przodek uczy ród domykania spraw ugodowych w pełnym szacunku."
    },
    3: {
        "Prawa": "Nurt nieograniczonej obfitości i płodności (Sefira Bina). Twój kosmiczny dar to zdolność materializacji dobrobytu, kreacja piękna oraz naturalne generowanie wzrostu.",
        "Lewa": "Lekcja wymaga przepracowania lęku przed brakiem, zaborczości, chęci kontroli bliskich oraz uzależnienia od luksusu w materii.",
        "Talent": "Alchemik materii i naturalny kreator. Masz wrodzony talent do rozwijania projektów, opieki nad strukturami i tworzenia harmonijnego środowiska.",
        "Gleboka": "Twoja esencja to Matryca Wzrostu. Przepełnia Cię kosmiczna energia dawania życia pomysłom, relacjom i fizycznym formom.",
        "Wezel": "Blokada manifestuje się jako twórcza niemoc, permanentne niezadowolenie z siebie lub toksyczna duma odrzucająca wsparcie.",
        "Tikkun": "Misja polega na zrozumieniu, że prawdziwa obfitość płynie z serca, oraz na transformacji rodowych programów ubóstwa w stan duchowego bogactwa.",
        "Posag": "Błogosławieństwo rodowej obfitości i wzrostu. Przodek zakorzenił w polu rodziny poczucie bezpieczeństwa materialnego i emocjonalnego."
    },
    4: {
        "Prawa": "Strumień stabilizacji, porządku i najwyższego autorytetu (Sefira Chochma). Twój dar to niezłomna struktura, zdolność budowania trwałych fundamentów i strategiczne myślenie.",
        "Lewa": "Wyzwanie zakłada przepracowanie despotyzmu, sztywności przekonań, tłumienia emocji oraz lęku przed utratą życiowej kontroli.",
        "Talent": "Budowniczy systemów. Posiadasz wrodzony talent do zarządzania ludźmi, tworzenia stabilnych praw i wprowadzania ładu w chaotyczne przestrzenie.",
        "Gleboka": "Twoja esencja to Filar Stabilności. Stanowisz punkt oparcia dla całego systemu rodowego, emanując naturalnym autorytetem.",
        "Wezel": "Opór aktywuje się jako chorobliwa surowość, tyrania wobec bliskich lub przeciwnie – całkowity brak życiowej struktury.",
        "Tikkun": "Głównym zadaniem jest integracja autorytetu z elastycznością oraz nauka rządzenia poprzez mądrość, a nie lęk i przymus.",
        "Posag": "Posag siły, prawa i stabilności rodowej. Przodek ugruntował pozycję rodziny, dając potomnym niezłomny fundament do rozwoju."
    },
    5: {
        "Prawa": "Strumień duchowego przewodnictwa i mądrości (energia litery He). Twoim darem jest łatwość przyswajania i przekazywania wiedzy o głębokim sensie istnienia.",
        "Lewa": "Lekcja wyjścia z dogmatyzmu, fanatyzmu przekonań oraz tendencji do moralizowania i oceniania innych ludzi.",
        "Talent": "Naturalny nauczyciel i mentor. Twój talent to umiejętność tłumaczenia skomplikowanych prawd w prosty, transformujący sposób.",
        "Gleboka": "Twoja esencja to Kosmiczny Kanał Wiedzy. Dążysz do życia opartego na autentycznych zasadach moralnych i głębokim wglądzie.",
        "Wezel": "Punkt oporu objawia się jako kompleks wyższości intelektualnej lub przeciwnie – paraliżujący lęk, że wciąż wiesz za mało.",
        "Tikkun": "Misja zakłada transformację wiedzy teoretycznej w żywą mądrość serca oraz naukę tolerancji dla odmiennych ścieżek życia.",
        "Posag": "Energia wolności, transformacji i zmian. Często oznacza odejście, które uczy ród elastyczności i odpuszczania kontroli."
    },
    6: {
        "Prawa": "Nurt harmonizacji przeciwieństw i świętej geometrii relacji (energia litery Waw). Twój dar to umiejętność dokonywania wyborów z poziomu serca i godzenia skrajności.",
        "Lewa": "Wyzwanie dotyczy paraliżu decyzyjnego, idealizacji partnerów, lęku przed odrzuceniem oraz rodowych uwikłań w trójkąty relacyjne.",
        "Talent": "Magnes serca i naturalny rozjemca. Twój talent to zdolność budowania głębokich więzi, wyczucie estetyki oraz wnoszenie miłości w skłócone przestrzenie.",
        "Gleboka": "W głębi duszy jesteś Punktem Zjednoczenia. Dążysz do bezwarunkowej akceptacji i integracji tego, co w świecie rodowym zostało rozdzielone.",
        "Wezel": "Blokada objawia się jako permanentne wątpliwości, brak lojalności wobec siebie lub uzależnienie własnego szczęścia od decyzji innych osób.",
        "Tikkun": "Misja wymaga wyjścia z iluzji zewnętrznego dopasowania i dokonania ostatecznego wyboru własnej, autentycznej drogi duszy.",
        "Posag": "Błogosławieństwo czystej miłości i pojednania. Przodek uzdrowił dawne dramaty relacyjne, pozostawiając w polu rodu matrycę zgody."
    },
    7: {
        "Prawa": "Potężny nurt determinacji i duchowego ukierunkowania (energia litery Zajin). Dar polega na niezłomnej sile parcia do przodu i umiejętności pokonywania przeszkód.",
        "Lewa": "Lekcja opanowania wewnętrznego pośpiechu, pychy, narcyzmu oraz tendencji do 'idącego po trupach' parcia do celu.",
        "Talent": "Wizjoner i zdobywca przestrzeni. Twój talent manifestuje się poprzez umiejętność wyznaczania jasnych kierunków i mobilizowania innych do działania.",
        "Gleboka": "Esencją Twojej duszy jest Ukierunkowany Strumień Światła. Żyjesz w ciągłym ruchu, dążąc do ewolucji i ciągłego przekraczania barier.",
        "Wezel": "Blokada to lęk przed porażką, który paraliżuje Cię przed podjęciem jakiegokolwiek działania, lub chaos i działanie bez planu.",
        "Tikkun": "Wyzwanie polega na integracji wewnętrznego spokoju i zrozumieniu, że droga do celu jest ważniejsza niż samo trofeum.",
        "Posag": "Potencjał duchowy, intelektualny i przełamywanie stagnacji rodowej. Dusza pozostawia przestrzeń do głębokich wglądów."
    },
    8: {
        "Prawa": "Strumień równowagi, prawdy i obiektywizmu (Sefira Gewura). Twoim kosmicznym darem jest naturalne zrozumienie prawa przyczyny i skutku oraz bezbłędny zmysł sprawiedliwości.",
        "Lewa": "Wyzwanie zakłada przepracowanie surowego osądu wobec siebie i innych, puszczenie zadawnionych urazów oraz uzdrowienie poczucia głębokiej niesprawiedliwości.",
        "Talent": "Mistrzostwo w porządkowaniu chaosu i godzeniu skrajności. Masz wrodzony talent do obiektywnej oceny sytuacji, strategii oraz struktur formalnych.",
        "Gleboka": "Twoja esencja to Matryca Kosmicznej Równowagi. Dążysz do prawdy, przejrzystości i harmonii, stając się filarem stabilności dla swojego otoczenia.",
        "Wezel": "Opór manifestuje się jako skrajna sztywność moralna, nieustępliwość, krytykanctwo lub paraliż przed podjęciem decyzji ze strachu przed błędem.",
        "Tikkun": "Główną misją naprawczą jest zamiana surowego, chłodnego osądu w mądre wyrozumienie oraz nauka elastyczności w relacjach międzyludzkich.",
        "Posag": "Sprawiedliwość i równowaga karmiczna. Przodek pozostawia w polu rodu czystą matrycę prawdy, domykając i rozliczając dawne krzywdy pokoleniowe."
    },
    
    9: {
        "Prawa": "Nurt wewnętrznego światła i mądrości odosobnienia (energia litery Tet). Twoim kosmicznym darem jest głęboki wgląd, cierpliwość oraz zdolność czerpania wiedzy z własnego wnętrza.",
        "Lewa": "Lekcja wymaga zmierzenia się z lękiem przed opuszczeniem, tendencją do całkowitej izolacji społecznej oraz zgorzknieniem wynikającym z niezrozumienia.",
        "Talent": "Wybitny analityk i doradca duchowy. Twój talent to zdolność głębokiej syntezy wiedzy, prowadzenie innych przez kryzysy oraz naturalne wyciszanie emocji.",
        "Gleboka": "W głębi duszy jesteś Strażnikiem Wewnętrznego Płomienia – poszukiwaczem prawdy absolutnej, który potrzebuje przestrzeni i ciszy, aby naładować swoje naczynie.",
        "Wezel": "Blokada objawia się jako aspołeczność, ucieczka od realnego świata w intelektualizm oraz lęk przed pokazaniem światu swojej autentycznej wrażliwości.",
        "Tikkun": "Misja zakłada wyjście ze swojej przestrzeni samotności, aby dzielić się wypracowanym wewnętrznym światłem i mądrością z potrzebującymi ludźmi.",
        "Posag": "Potencjał duchowy i mądrość syntezy. Przodek pozostawia po sobie przestrzeń do głębokich wglądów, uwalniając ród od powierzchownych dążeń materialnych."
    },
    10: {
        "Prawa": "Strumień przeznaczenia i boskiej iskry (energia litery Jod). Twoim kosmicznym darem jest naturalne zaufanie do cykli życia oraz lekkość w poruszaniu się po spiralach zmian.",
        "Lewa": "Wyzwanie zakłada przepracowanie syndromu 'ofiary losu', lęku przed nieznanym oraz poczucia permanentnego utknięcia w niesprzyjających warunkach.",
        "Talent": "Generowanie impulsów do transformacji. Masz wrodzony talent do chwytania właściwych momentów, intuicyjnego wyczuwania szans oraz potężną siłę manifestacji.",
        "Gleboka": "Twoja esencja to Kosmiczny Cykl Zmian – dynamiczny punkt zwrotny, który uczy otoczenie, że każda zmiana niesie w sobie ukryte błogosławieństwo.",
        "Wezel": "Opór aktywuje się jako chorobliwa walka z naturalnym biegiem wydarzeń, hazardowe podejście do życia lub całkowity paraliż przed podjęciem ryzyka.",
        "Tikkun": "Głównym wyzwaniem ewolucyjnym jest odpuszczenie neurotycznej kontroli i odbudowanie głębokiego, niezłomnego zaufania do prowadzenia wyższej mądrości.",
        "Posag": "Potężna moc manifestacji i transformacji skrajności. Przodek uwalnia pole rodu z dawnych stagnacji, zostawiając impuls do dynamicznej ewolucji."
    },

    11: {
        "Prawa": "Potężny nurt wewnętrznej siły, pasji i witalności. Twój kosmiczny dar to niezłomność, magnetyzm osobisty oraz zdolność regeneracji poprzez aktywację wyższego światła.",
        "Lewa": "Lekcja wymaga opanowania destrukcyjnej surowości (Gewura), tłumienia emocji oraz radzenia sobie z lękiem przed bezsilnością i utratą kontroli.",
        "Talent": "Transformacja surowej energii życiowej. Masz wrodzony talent do uzdrawiania, motywowania innych oraz zarządzania wielkimi zasobami energetycznymi pola.",
        "Gleboka": "W głębi duszy Twoja esencja to Gmach Mocy – czyste naczynie, które potrafi okiełznać najdziksze ziemskie instynkty za pomocą łagodności i duchowego współczucia.",
        "Wezel": "Blokada manifestuje się jako tyrania wobec otoczenia, wybuchy tłumionego gniewu lub permanentne wycieńczenie energetyczne spowodowane walką z samym sobą.",
        "Tikkun": "Misja polega na integracji własnej siły z wrażliwością, rezygnacji z rozwiązań siłowych na rzecz mądrego współczucia i ochrony słabszych struktur rodowych.",
        "Posag": "Posag niezłomności i potężnej ochrony energetycznej. Przodek pozostawia potomkom zasób ogromnej odporności psychofizycznej i siły życiowej."
    },
    12: {
        "Prawa": "Strumień nowej perspektywy i bezwarunkowego altruizmu. Twoim kosmicznym darem jest unikalne postrzeganie świata (energia litery Lamed) oraz zdolność dostrzegania ukrytych, boskich znaczeń.",
        "Lewa": "Wyzwanie zakłada przepracowanie syndromu męczennika, tendencji do stawiania się w roli ofiary oraz paraliżu decyzyjnego w krytycznych momentach.",
        "Talent": "Duchowe oświecenie i zmiana paradygmatów. Twój talent pozwala Ci znajdować genialne rozwiązania poprzez zatrzymanie się i spojrzenie na problem z poziomu wyższej świadomości.",
        "Gleboka": "Twoja esencja to stan Cichego Wglądu – mędrca, który wie, kiedy należy odpuścić działanie w materii na rzecz głębokiej transformacji wewnętrznej i oczyszczenia intencji.",
        "Wezel": "Opór aktywuje się jako wymuszone poświęcanie się dla innych, ucieczka w cierpiętnictwo lub całkowity paraliż uniemożliwiający ruch do przodu.",
        "Tikkun": "Główną misją naprawczą jest uzdrowienie rodowych programów ofiarności, nauka zdrowych granic oraz transformacja stagnacji w nową mądrość.",
        "Posag": "Uwalnianie rodowych poświęceń i zmiana optyki. Przodek pozostawia dar głębokiej empatii, ucząc ród wolności od dawnych schematów udręki."
    },
    13: {
        "Prawa": "Nurt głębokiej, radykalnej transformacji i odrodzenia (energia litery Mem - alchemia wody). Twój kosmiczny dar to umiejętność puszczania tego, co stare, i oczyszczanie przestrzeni pod nowe.",
        "Lewa": "Lekcja wymaga zmierzenia się z paraliżującym lękiem przed zmianą, toksycznym przywiązywaniem się do form oraz lękiem przed symboliczną stratą.",
        "Talent": "Alchemia i regeneracja pola. Masz wrodzony talent do przeprowadzania struktur, systemów lub ludzi przez procesy głębokiego kryzysu i odrodzenia.",
        "Gleboka": "W głębi duszy reprezentujesz Esencję Odnowy. Jesteś katalizatorem zmian, który nie pozwala na stagnację, iluzję i fikcję w swoim otoczeniu.",
        "Wezel": "Blokada objawia się jako chorobliwy opór przed ewolucją, trzymanie się destrukcyjnych relacji lub popadanie w stany głębokiej apatii i marazmu.",
        "Tikkun": "Misja zakłada pełne zrozumienie, że koniec jest jedynie początkiem nowego cyklu, oraz naukę zaufania do procesów naturalnego puszczania i odradzania duszy.",
        "Posag": "Głębokie oczyszczenie pola rodowego. Przodek zdołał przetransformować dawne, ciężkie uwarunkowania materialne w czystą mądrość i wolność dla potomnych."
    },
    14: {
        "Prawa": "Strumień duchowej alchemii, harmonii i umiaru. Twoim kosmicznym darem jest wrodzona zdolność do łagodzenia napięć, cierpliwość oraz idealne wyczucie proporcji (Sefira Tiferet).",
        "Lewa": "Wyzwanie dotyczy skrajnej niestabilności emocjonalnej, braku umiaru w jakiejkolwiek dziedzinie życia oraz wewnętrznego rozbicia na skrajności.",
        "Talent": "Harmonizowanie skonfliktowanych przestrzeni. Twój talent manifestuje się poprzez płynne łączenie różnych energii, talent uzdrowicielski oraz sztukę duchowej dyplomacji.",
        "Gleboka": "Twoja najgłębsza esencja to Złoty Środek – anioł stróż harmonii, który wnosi spokój, równowagę i wyważenie wszędzie, gdzie się pojawi.",
        "Wezel": "Opór aktywuje się jako emocjonalny chaos, popadanie w skrajności (od euforii do głębokiego smutku) lub wewnętrzne lenistwo maskowane spokojem.",
        "Tikkun": "Głównym wyzwaniem ewolucyjnym jest odnalezienie wewnętrznego punktu ciszy (alchemicznego środka) oraz integracja rozproszonych aspektów osobowości.",
        "Posag": "Alchemia, wyciszenie i harmonia duszy. Przodek pozostawia w posagu pole wolne od skrajnych dramatów, przynosząc kosmiczny spokój linii rodowej."
    },
    15: {
        "Prawa": "Potężny nurt magnetyzmu osobistego, charyzmy i kreacji materialnej. Twój dar to ogromna siła przyciągania, witalność oraz zdolność zarządzania materią.",
        "Lewa": "Lekcja wymaga przepracowania mechanizmów manipulacji, uzależnień (własnych lub cudzych), obsesji oraz lęku przed zniewoleniem materialnym (Klipot - siły cienia).",
        "Talent": "Mistrzostwo w manifestacji ziemskiej i praca z cieniem. Masz wrodzony talent do dostrzegania ukrytych motywów, psychologii oraz budowania potęgi materialnej.",
        "Gleboka": "W głębi duszy jesteś Strażnikiem Charyzmy. Posiadasz ogromny rezerwuar energii, który właściwie ukierunkowany potrafi kreować wielkie rzeczy na ziemi.",
        "Wezel": "Blokada manifestuje się jako uwikłanie w toksyczne układy władzy, ucieczka w destrukcyjne nałogi lub chorobliwa żądza kontroli nad otoczeniem.",
        "Tikkun": "Misja zakłada pełne wyzwolenie własnej woli spod uwarunkowań materii i lęków, transformację cienia i użycie charyzmy do wyzwalania innych.",
        "Posag": "Potężna siła kreacji materialnej i magnetyzmu. Przodek pozostawia w spadku zdolność budowania dobrobytu, z wyzwaniem zachowania czystości intencji."
    },
    16: {
        "Prawa": "Strumień gwałtownego wyzwolenia, prawdy i burzenia fałszywych struktur (energia litery Pe). Twoim darem jest odwaga do stawania w prawdzie i oczyszczania przestrzeni z iluzji.",
        "Lewa": "Wyzwanie zakłada przepracowanie katastrofizmu, lęku przed nagłym kryzysem życiowym oraz dumy, która blokuje przed proszeniem o pomoc.",
        "Talent": "Budowniczy Nowego Fundamentu. Twój talent to zdolność do błyskawicznego podnoszenia się z najtrudniejszych kryzysów i budowania swojego życia na stabilnej skale.",
        "Gleboka": "Twoja esencja to Przebudzenie Gwałtowne – punkt, który poprzez dynamiczne wydarzenia kruszy to, co było sztuczne, uwalniając czyste światło duszy.",
        "Wezel": "Punkt oporu objawia się jako chorobliwe trzymanie się fasadowego wizerunku, lęk przed rozpadem starych schematów lub skłonność do autodestrukcji.",
        "Tikkun": "Główną misją naprawczą jest nauka elastyczności, pokory wobec boskich zmian oraz zrozumienie, że każde zburzenie starej formy to akt kosmicznego wyzwolenia.",
        "Posag": "Gwałtowne oczyszczenie i wyzwolenie prawdy rodowej. Przodek zburzył fałszywe fasady pokoleniowe, zostawiając potomkom fundament absolutnej autentyczności."
    },
    17: {
        "Prawa": "Nurt niezłomnej nadziei, kosmicznego wsparcia i czystego talentu (energia litery Cadi). Twój dar to artystyczna lub duchowa inspiracja oraz głęboka wiara w boskie prowadzenie.",
        "Lewa": "Lekcja wymaga zmierzenia się z utratą wiary w sens życia, skłonnością do czarnowidztwa, naiwnością oraz permanentnym brakiem uznania dla samego siebie.",
        "Talent": "Inspiracja i magnetyzm twórczy. Masz wrodzony talent artystyczny, wizjonerski lub uzdrowicielski, który potrafi wnosić światło i nadzieję w życie innych.",
        "Gleboka": "W głębi duszy jesteś Sprawiedliwym (Cadyk) – istotą powołaną do lśnienia swoim autentycznym światłem, która przypomina otoczeniu o istnieniu wyższego porządku.",
        "Wezel": "Blokada manifestuje się jako paraliżująca niewiara we własne możliwości, lęk przed wyjściem z cienia lub ucieczka w świat nierealnych mrzonek i fantazji.",
        "Tikkun": "Wyzwanie polega na pełnym uziemieniu swoich talentów, odważnym pokazaniu ich światu oraz odbudowaniu głębokiego poczucia wewnętrznej unikalności.",
        "Posag": "Dar kosmicznego prowadzenia i opieki wyższych instancji. Przodek pozostawił w polu rodu czyste światło nadziei i talentu, które chroni przed mrokiem."
    },
    18: {
        "Prawa": "Strumień mistycznej wyobraźni, głębokiego magnetyzmu i pracy z podświadomością (energia litery Kof). Twój dar to zdolność materializacji marzeń oraz czytanie ukrytych sygnałów i przeczuć.",
        "Lewa": "Lekcja radzenia sobie z głębokimi, rodowymi lękami, uleganiem iluzjom, autooszustwem oraz podatnością na manipulacje psychiczne.",
        "Talent": "Potężna moc wizualizacji i kreacji. Masz wrodzony talent do pracy z psychiką, wprowadzania innych w stan głębokiego wglądu oraz intuicyjnego wyczuwania fałszu.",
        "Gleboka": "Twoja esencja to Strażnik Nocy i Podświadomości – łącznik z głębokim oceanem ukrytych sił psychicznych. Jesteś połączony z naturalnymi, niewidzialnymi rytmami istnienia.",
        "Wezel": "Opór manifestuje się jako paraliżujący lęk przed nieznanym, ucieczka od rzeczywistości w nałogi, stany lękowe lub zagubienie w labiryncie własnych iluzji.",
        "Tikkun": "Główną misją jest rozświetlenie mroków własnej i rodowej podświadomości, transformacja lęku w czystą intuicję oraz zakotwiczenie boskich wizji w materii.",
        "Posag": "Mądrość intuicyjna i oczyszczone pole iluzji. Przodek przetarł szlak przez rodowe lęki, pozostawiając potomkom dar głębokiego jasnowidzenia emocjonalnego."
    },
        19: {
        "Prawa": "Nurt potężnej witalności, radości istnienia i czystej manifestacji sukcesu (energia litery Resz). Twój kosmiczny dar to ogromna charyzma, jasność myślenia i zdolność dawania duchowego ciepła.",
        "Lewa": "Wyzwanie zakłada przepracowanie chorobliwego egocentryzmu, pychy, narcyzmu oraz tendencji do emocjonalnego spalania lub dominowania nad otoczeniem.",
        "Talent": "Lider i naturalny kreator obfitości. Twój talent to zdolność przyciągania dobrobytu, rozjaśniania najtrudniejszych sytuacji oraz naturalnego przewodzenia innym w materii.",
        "Gleboka": "W głębi duszy jesteś Pierwotnym Źródłem Światła – emanacją, która nie potrzebuje niczego z zewnątrz, by lśnić i ogrzewać całe swoje otoczenie.",
        "Wezel": "Blokada objawia się jako kompleks niższości maskowany arogancją, utrata energii życiowej lub paraliżujący lęk przed brakiem bycia zauważonym.",
        "Tikkun": "Misja zakłada używanie swojej potężnej energii do służby innym, rezygnację z walki o poklask na rzecz autentycznego, bezwarunkowego wspierania rodu.",
        "Posag": "Błogosławieństwo obfitości, zdrowia i sukcesu materialnego. Przodek wypracował stabilną pozycję rodową, zostawiając matrycę szczęścia i radości."
    },
    20: {
        "Prawa": "Strumień rodowego przebudzenia, odnowy i wyższej świadomości (energia litery Szin - ogień kosmiczny). Twój dar to głębokie połączenie z mądrością przodków oraz dar transformacji karmy.",
        "Lewa": "Lekcja wymaga zmierzenia się z surowym ocenianiem, rodowymi konfliktami, lękiem przed zmianą systemową oraz uwikłaniem w dawne, rodowe winy.",
        "Talent": "Uzdrowiciel karmy i integrator systemowy. Masz wrodzony talent do godzenia skłóconych rodzin, domykania procesów kosmicznej sprawiedliwości i transformacji starych struktur.",
        "Gleboka": "Twoja esencja to Przebudzenie Kosmiczne – moment absolutnej prawdy, w którym dusza słyszy wewnętrzne powołanie do powrotu do Boskiego Źródła.",
        "Wezel": "Opór aktywuje się jako sztywne trzymanie się przestarzałych tradycji rodowych, odmawianie wybaczenia lub paraliżujący lęk przed oceną ze strony rodziny.",
        "Tikkun": "Głównym wyzwaniem jest uzdrowienie i pełna integracja drzewa genealogicznego, odpuszczenie dawnych win oraz przebudzenie wyższej świadomości w linii.",
        "Posag": "Pełne wybaczenie rodowe i wyzwolenie z węzłów karmicznych. Przodek oczyścił pamięć komórkową rodu, dając potomkom czysty start i nowe powołanie."
    },
    21: {
        "Prawa": "Nurt globalnej świadomości, kosmicznej harmonii i ostatecznej realizacji (energia litery Taw - dopełnienie stworzenia). Twój dar to brak ograniczeń, łatwość adaptacji oraz poczucie jedności z całym stworzeniem.",
        "Lewa": "Wyzwanie dotyczy lęku przed wyjściem ze strefy komfortu, klaustrofobii życiowej, poczucia obcości na ziemi oraz stawiania sobie sztucznych barier.",
        "Talent": "Integrator i budowniczy mostów. Twój talent to łatwość w rozumieniu globalnych procesów, naturalne budowanie szerokich relacji i pomyślne domykanie wielkich projektów.",
        "Gleboka": "W głębi duszy jesteś Pełnią Manifestacji – istotą, która osiągnęła pełną integrację wewnętrzną, zrealizowała swoje duchowe cele i czuje jedność z wszechświatem.",
        "Wezel": "Blokada manifestuje się jako rezygnacja z marzeń ze strachu przed ich ogromem, utknięcie w ciasnych schematach lub totalna separacja od ludzi.",
        "Tikkun": "Misja zakłada przekraczanie wszelkich granic (mentalnych i geograficznych), niesienie idei jedności oraz pokazanie rodowi, że świat jest bezpiecznym miejscem do życia.",
        "Posag": "Posag globalnego sukcesu, ochrony w podróżach i pełnej realizacji. Przodek domknął stary cykl doświadczeń, dając linii rodowej wolność i kosmiczny zasięg."
    },
    22: {
        "Prawa": "Strumień najwyższego mistrzostwa duchowego i kosmicznej wolności ponad podziałami (dostęp do najwyższej Sefiry Keter - Korony). Twój dar to absolutna niezależność i moc przewodzenia nowej erze świadomości.",
        "Lewa": "Lekcja wymaga opanowania duchowej pychy, lęku przed totalną odpowiedzialnością za innych oraz tendencji do izolowania się z poczucia wyższości.",
        "Talent": "Wielki architekt nowej rzeczywistości. Masz wrodzony talent do tworzenia nowych systemów filozoficznych, duchowych lub społecznych, które rewolucjonizują strukturę rodu.",
        "Gleboka": "Twoja esencja to Stan Mistrzowski – dojrzałej duszy, która zintegrowała wszystkie ziemskie lekcje i powróciła do niższego świata, by służyć jako czysty drogowskaz.",
        "Wezel": "Opór objawia się jako totalny nihilizm, odrzucenie praw naturalnych lub paraliżujący lęk przed porażką na poziomie globalnym.",
        "Tikkun": "Główną misją jest zamanifestowanie najwyższej mądrości w codziennym, prostym życiu oraz przeprowadzenie linii rodowej przez proces ostatecznego oczyszczenia.",
        "Posag": "Absolutne mistrzostwo i duchowa suwerenność. Przodek wyzerował wszelkie długi i pozostawił w polu czystą, boską matrycę nieograniczonych możliwości."
    }

}



def pobierz_analize_premium(numer, klucz):
    """Zwraca opis premium; dla niepełnych wpisów korzysta z bazy podstawowej."""
    wpis = ANALIZY.get(numer, {})
    if klucz in wpis:
        return wpis[klucz]
    from dane import KABALA_DICTIONARY
    bazowy = KABALA_DICTIONARY.get(numer, {})
    mapa = {
        "Prawa": "znaczenie",
        "Lewa": "cien",
        "Talent": "znaczenie",
        "Gleboka": "archetyp",
        "Wezel": "cien",
        "Tikkun": "znaczenie",
        "Posag": "posag",
    }
    return bazowy.get(mapa.get(klucz, "znaczenie"), "Brak opisu.")
