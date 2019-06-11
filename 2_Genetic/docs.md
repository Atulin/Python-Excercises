# Algorytm genetyczny

## Sposób kodowania informacji

W przypadku prostych informacji jak liczby, najłatwiej jest zakodować je
w postaci binarnej. Daje nam to możliwośc łatwego krzyżowania ich poprzez
przecięcie łańcuchów bitów i złożenie ich kawałków z różnych osobników, a
także łatwej mutacji poprzez odwrócenie losowego bitu.

## Przebieg algorytmu

### Założenia

* 6 chromosomów (osobników)
* Szansa krzyżowania 0.8
* Szansa mutacji 0.2

### Przebieg

Algorytm szukał będzie takiej wartości x, aby funkcja 3x+6 przyjęła
największą możliwą wartość w zadanym zakresie x.

Zakres x to [0, 255]

#### 1. Generujemy losową pulę sześciu ośmiobitowych osobników, obliczamy ich fitness

fitness = 3 * x + 6

1. [ 1 1 1 1 1 1 1 1 ] = 255, fitness = 771
2. [ 1 0 0 0 1 0 0 1 ] = 137, fitness = 417
3. [ 0 0 0 1 1 0 1 0 ] = 26, fitness = 84
4. [ 1 0 0 1 0 1 0 0 ] = 148, fitness = 450
5. [ 0 1 0 1 0 1 1 1 ] = 87, fitness = 267
6. [ 0 0 1 1 0 1 0 0 ] = 52, fitness = 162

#### 2. Eliminujemy najsłabsze osobniki regułą koła ruletki

Kolejne wartości koła ruletki to:

1. 0
2. 0 + 771 = 771
3. 771 + 417 = 1188
4. 1188 + 84 = 1272
5. 1272 + 450 = 1722
6. 1722 + 267 = 1989
7. 1989 + 162 = 2151

Następnie losujemy sześć liczb z zakreso [0, 2151] i sprawdzamy w który
slot ruletki wpadają:

1. 1719 – przypada na slot 4
2. 2147 – przypada na slot 6
3. 674 – przypada na slot 1
4. 1390 – przypada na slot 5
5. 1631 – przypada na slot 5
6. 81 – przypada na slot 1

Numery slotów stanowią numery osobników które przechodzą do następnej fazy
algorytmu. Osobniki te to:

1. [ 1 0 0 1 0 1 0 0 ] = 148, fitness = 450
2. [ 0 0 1 1 0 1 0 0 ] = 52, fitness = 162
3. [ 1 1 1 1 1 1 1 1 ] = 255, fitness = 771
4. [ 0 1 0 1 0 1 1 1 ] = 87, fitness = 267
5. [ 0 1 0 1 0 1 1 1 ] = 87, fitness = 267
6. [ 1 1 1 1 1 1 1 1 ] = 255, fitness = 771

#### 3. Krzyżujemy z sobą osobniki które przetrwały

Kolejną fazą algorytmu jest krzyżowanie w parach bazując na obranej szansie
krzyżowania: 0.8.

Pary dobieramy w kolejności występowania, choć można je również dobierać
losowo. W związku z tym, obrane pary to:

1. (1, 2)
2. (3, 4)
3. (5, 6)

Dla każdej pary losować będziemy liczbę z zakresu [0, 1]. Jeśli okaże się
mniejsza od 0.8, osobniki skrzyżują się w wylosowanym miejscu.

1. 0.87712
2. 0.78912
3. 0.12168

W związku z tym, krzyżować będą się dwie pary – (3, 4) oraz (5, 6):

1. Wylosowane miejsce krzyżowania to 3, oba osobniki rozcinamy więc
za trzecim bitem:

    1. [ 1 1 1 ] [ 1 1 1 1 1 ]
    2. [ 0 1 0 ] [ 1 0 1 1 1 ]
    
    a następnie zamieniamy końcówki miejscami, tworząc dwa nowe osobniki:
    
    1. [ 1 1 1 ] [ 1 0 1 1 1 ]
    2. [ 0 1 0 ] [ 1 1 1 1 1 ]

2. Wylosowane miejsce krzyżowania to 6, oba osobniki rozcinamy więc
za szóstym bitem:

    1. [ 0 1 0 1 0 1 ] [ 1 1 ]
    2. [ 1 1 1 1 1 1 ] [ 1 1 ]

    Jak widać, końcówki obu osobników są takie same, więc nawet po ich
    zamianie wartość żadnego z osobników się nie zmieni:

    1. [ 0 1 0 1 0 1 ] [ 1 1 ]
    2. [ 1 1 1 1 1 1 ] [ 1 1 ]
    
Po dokonaniu krzyżowania, otrzymujemy nową pulę osobników:

1. [ 1 0 0 1 0 1 0 0 ] = 148, fitness = 450
2. [ 0 0 1 1 0 1 0 0 ] = 52, fitness = 162
3. [ 1 1 1 1 0 1 1 1 ] = 247, fitness = 747
4. [ 0 1 0 1 1 1 1 1 ] = 95, fitness = 291
5. [ 0 1 0 1 0 1 1 1 ] = 87, fitness = 267
6. [ 1 1 1 1 1 1 1 1 ] = 255, fitness = 771

#### 4. Na końcu mutujemy osobniki w populacji

Dla każdego osobnika, podobnie jak w przypadku par w poprzednim kroku, 
wylosowana zostanie liczba z przedziału [0, 1]. Jeśli okaże się mniejsza
od obranej szansy 0.2, osobnik zostanie zmutowany poprzez odwrócenie
bitu w losowym miejscu.

1. [ 1 0 0 1 0 1 **0** 0 ] – 0.013 osobnik zmutuje na bicie numer 7
2. [ 0 0 1 1 0 1 0 0 ] – 0.781
3. [ 1 1 1 1 0 1 1 1 ] – 0.391
4. [ 0 1 0 1 1 1 1 1 ] – 0.67
5. [ 0 1 0 **1** 0 1 1 1 ] – 0.088 osobnik zmutuje na bicie numer 4
6. [ 1 1 1 1 1 1 1 1 ] – 0.928

Nowa populacja, po dokonaniu mutacji, prezentuje się następująco:

1. [ 1 0 0 1 0 1 1 0 ] = 150, fitness = 456
2. [ 0 0 1 1 0 1 0 0 ] = 52, fitness = 162
3. [ 1 1 1 1 0 1 1 1 ] = 247, fitness = 747
4. [ 0 1 0 1 1 1 1 1 ] = 95, fitness = 291
5. [ 0 1 0 0 0 1 1 1 ] = 71, fitness = 219
6. [ 1 1 1 1 1 1 1 1 ] = 255, fitness = 771

#### 5. Kolejne kroki

Kroki 1 do 4 należy powtarzać aż do osiągnięcia pożądanych rezultatów