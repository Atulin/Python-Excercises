# Dokumentacja

## Opis algorytmu

Zasrosowano algorytm najbliższego sąsiada.

Sprawdza on który z punktów grafu
znajduje się najbliżej punktu startowego, a następnie przechodzi do niego,
dopisuje go do listy odwiedzonych punktów, i usuwa punkt startowy z listy
początkowej punktów.

W kolejnym punkcie, ponownie odnajdowany jest najbliższy punkt (z pominięciem
usuniętego już punktu startowego), algorytm przechodzi do niego, usuwa
obecny punkt z listy, i dodaje nowy punkt do listy odwiedzonych punktów. 

Algorytm kończy działanie gdy na początkowej liście punktów nie pozostanie
żaden punkt do odwiedzenia.

## Obliczenia

Obliczenie dystansu pomiędzy dwoma punktami dokonane zostało przy użyciu
wzoru Pitagorasa: a^2 + b^2 = c ^2

## Dokumentacja kodu

`class Point`

Klasa przechowująca punkt w przestrzeniu dwuwymiarowej.

Posiada on następujące parametry:

* `name: str` String będący nazwą węzła, może to być litera, nazwa miasta, etc.
* `x: int` Integer przechowujący pozycję w osi X
* `y: int` Integer przechowujący pozycję w osi Y

Oraz następujące metody:

* `__init__(self, name: str, x: int, y: int)` Konstruktor przyjmujący
nazwę węzła oraz jego koordynary
* `__str__(self)` Metoda konwertująca węzeł na string
* `__repr__(self)` Metoda wypisująca węzeł do konsoli

Pozostałe zawarte w kodzie funkcje to:

* `distance(a: Point, b: Point) -> float` Funkcja przyjmująca dwa punkty
i zwracająca float stanowiący odległość między nimi
* `total_length(graph: list) -> float` Funkcja ta przyjmuje jako
argument listę punktów i zwraca całkowitą długość ściezki łączącej je
* `hamilton(graph: list, starting_point_name: str) -> list` Funkcja
obliczająca ścieżkę. Przyjmuje liste punktów oraz nazwe punktu startowego
jako parametry, zwraca posortowaną listę punktów.
* `shuffle(points_array: list, starting_point_name: str) -> list` Funkcja
przenosząca wybrany punkt na początek listy. Przyjmuje listę punktów oraz
nazwę punktu startowego za argumenty, zwraca posortowaną listę punktów.