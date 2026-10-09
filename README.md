# soul-decoder-app

# Soul Decoder App (Kabalistyczny Dekoder Matrycy Duszy)

## 📌 O Projekcie
**Soul Decoder App** to zaawansowana aplikacja analityczno-diagnostyczna służąca do wielopokoleniowego dekodowania profilu psychologiczno-karmicznego na podstawie struktur dat. Projekt opiera się na zmodyfikowanej metodologii kabalistycznej matrycy 22 energii (odpowiadających literom alfabetu hebrajskiego oraz Wielkim Arkanom). 

Aplikacja nie pełni roli „wróżby” – jest to deterministyczny system algorytmiczny, który przekształca dane wejściowe (daty urodzenia i śmierci) w spójną instrukcję i mapę drogową do pracy nad własnym potencjałem, blokadami oraz dziedzictwem rodowym.

---

## 🚀 Kluczowe Funkcjonalności (Moduły Systemu)

### 1. Core Engine (Silnik Matematyczny Profilu)
*   **Redukcja Modularna do 22 Stanów:** Implementacja ścisłego algorytmu redukcji cyfr przez sumowanie wyłącznie w sytuacji, gdy wartość przekracza 22 (system zamknięty bazujący na 22 energiach).
*   **Mapowanie Archetypów:** Dynamiczne przypisywanie wyliczonych liczb do obiektów w bazie danych zawierających: nazwę litery hebrajskiej, archetyp, jasną stronę (potencjał) oraz aspekt cienia (blokadę).

### 2. Wielopokoleniowa Analiza Linii Męskiej (Psychogenealogia)
*   **Struktura Drzewa Rodowego (Tree Data Structure):** Algorytm przetwarza dane wertykalnie w linii męskiej: *Pradziadek ➔ Dziadek ➔ Ojciec ➔ Użytkownik*.
*   **Detekcja Rezonansu i Replikacji Wzorców:** System automatycznie porównuje profile przodków w poszukiwaniu powtarzających się napięć energetycznych (np. Węzeł Oporu ojca stający się Karmą syna), flagując tzw. *Długi Rodowe do przepracowania*.
*   **Transfer Aktywnego Posagu:** Analiza i mapowanie odziedziczonych talentów i zasobów wspierających ekspansję użytkownika.

### 3. Moduł Transformacji Przejścia (Data Śmierci)
*   **Dekodowanie Posagu Energetycznego:** Algorytm analizuje moment zamknięcia cyklu materialnego (datę śmierci przodków), wyliczając *Liczbę Przejścia*.
*   **Korelacja międzypokoleniowa:** System bada, w jaki sposób uwolniona w momencie śmierci esencja przodka wpływa na matrycę urodzenia potomków (jako dodatkowy zasób lub ostateczne wyzwanie ewolucyjne).

### 4. Moduł Raportowania i UI (W trakcie wdrażania)
*   **Generator PDF:** Automatyczne składanie i formatowanie wielostronicowych, spersonalizowanych raportów analitycznych gotowych do druku.
*   **Interfejs Webowy:** Przejrzysty panel użytkownika (UI) z dynamicznymi polami wyboru dat.

---

## 🛠️ Stack Technologiczny
*   **Język programowania:** Python 3.x
*   **Struktury danych:** Zaawansowane mapowanie obiektowo-słownikowe (Dictionares & Custom Objects)
*   **Architektura algorytmu:** Operacje na wartościach bezwzględnych (`abs`), dynamiczne pętle redukcji cyfr (`while`), analiza porównawcza grafów/drzew relacyjnych.

---

## 📐 Logika Algorytmu (Przykład dla Daty Urodzenia)
Dla struktury danych wejściowych systemu, profil generowany jest z operacji matematycznych na poszczególnych komponentach daty:
1.  **Prawa Strona (Filar Dawania/Dar):** Zredukowany dzień urodzenia.
2.  **Lewa Strona (Filar Karmy/Lekcja):** Zredukowany miesiąc urodzenia.
3.  **Głęboka Osobowość (Esencja):** Suma cyfr roku urodzenia (redukowana do max 22).
4.  **Talent (Kreacja):** Suma pól: *Prawa Strona + Lewa Strona + Głęboka Osobowość* (poddana redukcji do 22).
5.  **Węzeł Oporu (Blokada):** Wartość bezwzględna z różnicy: `|Głęboka Osobowość - Lewa Strona|`.
6.  **Tikkun (Naprawa Karmiczna):** Wartość bezwzględna z różnicy: `|Węzeł Oporu - Prawa Strona|`.

---

## 👥 Autor
*   **Emilia Olszewska (emiolsz)** – [Profil GitHub](https://github.com/emiolsz)

