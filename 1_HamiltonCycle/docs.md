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
wzoru Pitagorasa: `a^2 + b^2 = c ^2` zmodyfikowanego do postaci 
`c = sqrt(a^2 + b^2)`

1. Odległość z punktu E do punktu A to sqrt((5-1)^2+(2-2)^2)=4.0
2. Odległość z punktu E do punktu B to sqrt((5-3)^2+(2-1)^2)=2.24
3. Odległość z punktu E do punktu C to sqrt((5-3)^2+(2-6)^2)=4.47
4. Odległość z punktu E do punktu D to sqrt((5-6)^2+(2-7)^2)=5.1

Najkrótsza droga prowadzi do punktu B, ten punkt obieramy więc za następny:

1. Odległość z punktu B do punktu A to sqrt((3-1)^2+(1-2)^2)=2.24
2. Odległość z punktu B do punktu C to sqrt((3-3)^2+(1-6)^2)=5.0
3. Odległość z punktu B do punktu D to sqrt((3-6)^2+(1-7)^2)=6.71

Z punktu B najbliżej jest do punktu A, tak więc dalej sprawdzamy odległości z niego

1. Odległość z punktu A do punktu C to sqrt((1-3)^2+(2-6)^2)=4.47
2. Odległość z punktu A do punktu D to sqrt((1-6)^2+(2-7)^2)=7.07

Najbliżej jest do punktu D, a odległośc ta wynosi sqrt((3-6)^2+(6-7)^2)=3.16

Odległośc z punktu D do punktu startowego E to sqrt((6-5)^2+(7-2)^2)=5.1

Ostatecznie, najkrótsza ścieżka to E -> B -> A -> C -> D -> E, ma ona długość 17.21




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