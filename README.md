# Przetwarzanie Obrazów z URL

Program do wczytywania obrazów z internetu i wykonywania podstawowych operacji przetwarzania obrazu przy użyciu bibliotek PIL, NumPy i Matplotlib.

## Spis treści

- [Opis](#opis)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Funkcjonalności](#funkcjonalności)
- [Struktura projektu](#struktura-projektu)
- [Przykład działania](#przykład-działania)
- [Autor](#autor)
- [Licencja](#licencja)

## Opis

Program demonstruje podstawowe techniki przetwarzania obrazów w Pythonie. Pobiera obraz papugi tęczowej z Wikimedia Commons, a następnie wykonuje serię transformacji: zmniejszenie rozmiaru, konwersję do skali szarości i obrót. Wyniki są wizualizowane za pomocą Matplotlib, a wartości pikseli wyświetlane jako macierz NumPy.

## Wymagania

### Wymagania systemowe
- Python 3.7 lub nowszy
- Połączenie z internetem (do pobierania obrazów)

### Wymagane biblioteki
- `Pillow` (PIL) >= 9.0.0
- `numpy` >= 1.21.0
- `matplotlib` >= 3.3.0

## Instalacja

1. Sklonuj repozytorium lub pobierz plik projektu:
```bash
git clone <url-repozytorium>
cd <nazwa-projektu>
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install Pillow numpy matplotlib
```


## Użycie

Uruchom program za pomocą interpretera Python:

```bash
python GKiPO_zad1.py
```

Program automatycznie:
1. Pobierze obraz z określonego URL
2. Wyświetli oryginalny obraz w oknie Matplotlib
3. Przetworzy obraz (zmniejszenie, konwersja do skali szarości, obrót)
4. Wyświetli przetworzony obraz
5. Wydrukuje fragment macierzy pikseli (10x10) w konsoli

## Funkcjonalności

### 1. Pobieranie obrazu z URL
Program pobiera obraz bezpośrednio z internetu za pomocą `urllib.request`, symulując przeglądarkę przez ustawienie nagłówka User-Agent.

### 2. Wyświetlanie oryginalnego obrazu
Pierwotny obraz jest wyświetlany w oknie Matplotlib z zachowaniem oryginalnych proporcji.

### 3. Zmiana rozmiaru
Obraz jest zmniejszany o połowę przy użyciu algorytmu LANCZOS, który zapewnia wysoką jakość resampleowania.

### 4. Konwersja do skali szarości
Kolorowy obraz RGB jest konwertowany do obrazu w skali szarości (tryb "L" w PIL).

### 5. Obrót obrazu
Obraz w skali szarości jest obracany o -90 stopni (w prawo) z parametrem `expand=True`, aby uniknąć obcięcia.

### 6. Analiza macierzy pikseli
Program konwertuje obraz na tablicę NumPy i wyświetla fragment macierzy wartości pikseli (10x10 pikseli z lewego górnego rogu).


## Przykład działania

### Wyjście konsoli
```
Ten program wczytuje obraz z internetu i wykonuje podstawowe operacje na obrazie.

[Wyświetlenie oryginalnego obrazu w oknie Matplotlib]
[Wyświetlenie przetworzonego obrazu w oknie Matplotlib]

Macierz zmienionego obrazu:

[[123 125 127 ... 134 136 138]
 [124 126 128 ... 135 137 139]
 ...
 [145 147 149 ... 156 158 160]]
```

### Przepływ danych
```
URL → Pobieranie → Oryginalny obraz (wyświetlenie)
                          ↓
                    Zmiana rozmiaru (50%)
                          ↓
                    Skala szarości
                          ↓
                    Obrót (-90°)
                          ↓
            Przetworzony obraz (wyświetlenie)
                          ↓
                    Macierz NumPy (wydruk)
```

## Możliwe modyfikacje

### Zmiana źródła obrazu
Aby użyć innego obrazu, zmień wartość zmiennej `url`:
```python
url = "https://twoj-url-do-obrazu.jpg"
```

### Dostosowanie parametrów przetwarzania
- **Stopień zmniejszenia**: Zmień dzielnik w `width // 2, height // 2`
- **Kąt obrotu**: Zmień wartość w `rotate(-90, expand=True)`
- **Rozmiar wyświetlanej macierzy**: Zmień `[:10, :10]` na żądane wymiary

## Obsługa błędów

Program nie zawiera zaawansowanej obsługi błędów. Możliwe problemy:
- **Brak połączenia z internetem**: Program zakończy się błędem urllib
- **Nieprawidłowy URL**: Błąd HTTP 404 lub podobny
- **Uszkodzony plik obrazu**: Błąd PIL przy otwieraniu obrazu

## Licencja

Projekt udostępniony na licencji MIT. Obraz papugi tęczowej pochodzi z Wikimedia Commons i jest dostępny na licencji Creative Commons.


---

**Uwaga**: Program służy celom edukacyjnym i demonstracyjnym. Zawsze sprawdzaj prawa autorskie do obrazów przed ich wykorzystaniem w projektach komercyjnych.
