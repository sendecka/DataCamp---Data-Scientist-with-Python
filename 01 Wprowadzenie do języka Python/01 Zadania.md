# <p style="text-align: center;">Python Zadania </p>

## Zadanie 1 Moduł 2 

Do zmiennej zdanie zapisz dowolne zdanie (w kodzie lub pobrane za pomocą input()), a następnie wyświetl na konsoli tekst postaci: „W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}” . W miejsca {liczba_liter1} oraz {liczba_liter2} podstaw zmienne, które będą przechowywały liczbę wystąpień danych liter (poszukaj odpowiedniej metody dla typu str). Litery, które mają być wyszukane to 4 litera nazwiska oraz 3 litera imienia osoby wykonującej ćwiczenie, np. imie = „Krzysztof”, nazwisko = „Ropiak”, litera_1 = imie[2], litera_2 = nazwisko[3].

## Zadanie 2 Moduł 2 

Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w przykładach z tego podrozdziału (np. z wyrównaniem, ilością pozycji liczby, znakiem itp.).

## Zadanie 1 Moduł 3

Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.

## Zadanie 2 Moduł 3

Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.

## Zadanie 3 Moduł 3

Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia poprzez funkcję input(). Następnie wyświetl ciąg unikalnych znaków z wczytanego zdania, zapisanych alfabetycznie małymi literami.*

* wykorzystaj rzutowanie typu str na set oraz set na list i użyj funkcji sortującej listę

## Zadanie 4 Moduł 3

Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1) a wartościami nazwy polskich miesięcy.

## Zadanie 5 Moduł 3

Stwórz podobny słownik jak w zadaniu 4, ale z angielskimi nazwami miesięcy. Połącz teraz słowniki tak, żeby przykładowo dla kwietnia, dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].

## Zadanie 6 Moduł 3

Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik, który będzie zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy klucz będzie miał przypisaną wartość 1. Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1}

## Zadanie 7 Moduł 3

Wykorzystaj moduł string (dodaje się go poprzez instrukcję import string zapisaną na początku skryptu) i następnie:

wczytaj ze standardowego wejścia dowolny łańcuch znaków,
używając formatowania znaków wyświetl ile znaków oraz jaki procent (zamienionych na małe litery) z nich pokrywa się ze zbiorem znaków z: string.ascii_lowercase, string.digits.
Przykład:
Wejście (input):
Ala ma kota.

Wyjście (output):
W zdaniu 'Ala ma kota.' występuje 6 znaków wspólnych ze zbiorem string.ascii_lowercase, co stanowi 23.00 % tego zbioru.
W zdaniu 'Ala ma kota.' występuje 0 znaków wspólnych ze zbiorem string.digits, co stanowi 0.00 % tego zbioru.

## Zadanie 8 Moduł 3

Napisz kod, w którym pobierzesz za pomocą funkcji input() 3 wartości przypisując je do zmiennych: start, stop oraz step. Następnie użyj ich jako parametrów funkcji range i wykorzystując przykłady z listingu 10 wypisz wszystkie wartości ciągu wygenerowane przez tę funkcję. Zwróć uwagę na typ danych, który zwraca funkcja input() - będzie konieczna konwersja (rzutowanie).

## Zadanie 1 Moduł 4

Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie (użyj instrukcji input).

## Zadanie 2 Moduł 4

Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie. Wynik wyświetla na ekranie (ale użyj instrukcji readline() i write()).

## Zadanie 3 Moduł 4

Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:

czy a zawiera się w przedziale (0,10]
oraz czy jednocześnie a>b lub b>c.
Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.

## Zadanie 4 Moduł 4

Napisz pętlę, która wyświetla liczby podzielne przez 5 z zakresu [0,50]

## Zadanie 5 Moduł 4

Napisz pętle (while), która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie. Liczby pobierane są w postaci oddzielonej spacjami. Pętla kończy działanie po wpisaniu słowa quit.

## Zadanie 6 Moduł 4

Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście. Liczby dodajemy do momentu wpisania słowa 'stop' zamiast liczby. Wykorzystaj pętle while. Po wpisaniu stop wyświetl listę liczb.

## Zadanie 7 Moduł 4

Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry. Wynik wyświetla na ekranie. Napisz dwa rozwiązania: jedno z uzyciem pętli for a drugie z użyciem pętli while.

## Zadanie 8 Moduł 4

Napisz skrypt, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży, ale nie więcej jak 10.

A
AA
AAA
AAAA
AAAAA
AAAAAA

## Zadanie 9 Moduł 4

Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100 w formie znanej z lekcji matematyki w szkole podstawowej.

## Zadanie 10 Moduł 4

Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9, ale tylko nieparzysta wysokość.

Przykład wyjścia dla wysokosc = 3

 o
ooo
 o
oraz wysokosc = 5

  o
 ooo
ooooo
 ooo
  o
itd.


## Zadanie 1 Moduł 5

Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
A={1/x: x∈<1,10>}
B={1, 2, 4, 8,…, $2^{10}$}
C={x: x∈ B i x jest liczbą podzielną przez 4}

## Zadanie 2 Moduł 5

Wygeneruj macierz (lista dwupoziomowa) losowych wartości (sprawdź pakiet random) 4x4 i wykorzystując Python Comprehension zdefiniuj listę, która będzie zawierała tylko elementy znajdujące się na przekątnej.

## Zadanie 3 Moduł 5

Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą tylko te produkty, których wartość to sztuki.

Mechanizm przedstawiony w tym podrozdziale jest bardzo przydatny, chociaż skomplikowane polecenia mogą być wyzwaniem do zinterpretowania względem „tradycyjnego” podejścia. Więcej przykładów można znaleźć w dokumentacji Pythona pod adresem https://docs.python.org/3.11/tutorial/datastructures.html#nested-list-comprehensions

## Zadanie 4 Moduł 5

Zdefiniuj funkcję, która "pyta" użytkownika o jego imię i po jego podaniu wyświetla komunikat 'Witaj {imie}!'.

## Zadanie 5 Moduł 5

Napisz funkcję, która przyjmuje jeden argument pozycyjny, o domyślnej wartości 4, i na podstawie tego argumentu wypisuje na wyjściu (konsola) n*n tych wartości, np.: dla liczby 3:

333
333
333

## Zadanie 6 Moduł 5

Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów ciągu.

## Zadanie 7 Moduł 5

Napisz funkcję, która wykorzystuje symbol **. Funkcja przyjmuje argumenty w postaci: klucz to nazwa drużyny a wartość to ilość punktów, które drużyna zdobyła. Funkcja zlicza ile jest wszystkich punktów razem i zwraca tę wartość.

## Zadanie 1 Moduł 6

Wczytaj plik zamowienia.csv i dokonaj w nim kilku przekształceń:

pozbądź się znaku z (właściwie zł) z kolumny Utarg
zamień separator wartości dziesiętnej w tej samej kolumnie na '.'
pozbądź się spacji jako separatora tysięcy w kolumnie Utarg
zamień format daty w pliku na RRRR-MM-DD
Podziel plik na dwie części i zapisz je tak, aby dane dla każdego kraju (Polska, Niemcy) znajdowały się w oddzielnych plikach o nazwach zamowienia_polska.csv i zamowienia_niemcy.csv.

## Zadanie 2 Moduł 6

Napisz funkcję, która przyjmuje listę plików oraz nazwę nowego pliku jako argumenty wejściowe. Funkcja scala zawartość plików w jeden plik wynikowy o podanej wcześniej nazwie.

Zadania powtórzeniowe
Zadanie 3

Napisz funkcję, która będzie zwracała 3 największe wartości z listy numerycznej. Lista jest parametrem wejściowym funkcji.

Zadanie 4

Mając listę mieszana = [1, 2.3, ‘Zbyszek’, 5, ‘Marian’, 3.0] napisz funkcję, która zapisze wartości dla każdego typu do słownika gdzie pod kluczem równym nazwie typu zmiennej (int, float, str, itp.) wartością będzie lista elementów z listy 'mieszana' danego typu. Przykład: {'int': [1,5], 'str': ['Zbyszek','Marian']} itd.

Zadanie 5

Napisz funkcję:

parametr wejściowy to lista stringów z nazwiskami
funkcja zapisuje do dwóch oddzielnych plików o nazwach ‘A-M_nazwiska.txt’ oraz ‘N-Ż_nazwiska.txt’ odpowiednie nazwiska z podanej listy
Zadanie 6

Napisz funkcję, która wyświetla podany tekst odwracając kolejność liter w wyrazach. Np. „Ala ma kota” wyświetli „alA am atok”

Zadanie 7

Napisz funkcję, która:

jako parametr wejściowy pobiera zdanie wpisywane z klawiatury,
ponownie z klawiatury pobiera nazwę pliku, w którym zapisany zostanie wynik działania funkcji,
do pliku zapisywane są unikalne wyrazy ze zdania pisane małymi literami po jednym w linii,
ze zdania zostaną usunięte ewentualne przecinki i kropki.
Zadanie 8

Napisz funkcję, która losuje 5 liczb całkowitych z przedziału <1, 20> dopóki w jednym losowaniu nie wystąpi 1 i 20. Wyświetl ilość wykonanych losowań po spełnieniu warunku.

Zadanie 9

Napisz funkcję, która posiada zaszytą listę 3 nagród ['samochód', '10000 PLN', 'PS 4 Pro']. Przygotuj plik z 10 imionami i nazwiskami zapisanymi po 1 w wierszu. Następnie funkcja wczytuje plik, losuje zwycięzcę dla każdej z trzech nagród i zapisuje wyniki w pliku o nazwie zwycięzcy.txt wpis postaci: Imię nazwisko, nagroda.

Zadanie 10

Napisz funkcję, która:

„rozdaje” karty z talii 52 kart (np. As pik, Dama karo, itd.) dla 4 graczy
karty rozdawane są bez powtórzeń po 5 dla każdego gracza
wyświetlana jest informacja jak wygląda „ręka” każdego z graczy, np. Alan [As pik, 9 karo, itd.]
Zadanie 11

Napisz funkcję, która wczytuje z pliku zawierającego imiona i nazwiska osób zapisane po jednym w linii, np.

Marek Markowski
Paweł Budzikowski

Funkcja generuje dla podanej listy adresy e-mail postaci: imie.nazwisko@imgw.pl i zapisuje dane do nowego pliku dopisując przy wcześniejszym nazwisku wygenerowany adres, np.

Marek Markowski, marek.markowski@imgw.pl itd.

W nazwach e-mail powinny być zastępowane ewentualne polskie znaki (ż,ź na z, ą na a itd.).

Zadanie 12

Przygotuj plik z kilkoma hasłami, które nadają się do gry 'Koło fortuny'. Wczytaj te hasła do listy i losuj jedno z nich. Na ekranie wyświetlaj hasło bez ujawniania poszczególnych liter, np.:___ _____ ___ __ _______ dla hasła 'Bez pracy nie ma kołaczy'. Nastepnie w pętli pozwalaj uzytkownikowi na podawanie jednej litery, która będzie podstawiana w miejscach gdzie występuje lub wyświetlaj komunikat, że takiej litery nie ma w haśle. Dodaj też funkcjonalność, która pozwala na odgadnięcie (wpisanie) całego hasła.

Zadanie 13

Napisz funkcję, która będzie pobierała dwa parametry wejściowe:

łańcuch znaków
liczbę całkowitą
Funkcja ma skracać podany łańcuch znaków tak, żeby po dodaniu ... na końcu jego długość nie była większa niż max (podany jako drugi parametr) i aby tekst nie był urwany w połowie wyrazu. Funkcja zwraca skrócony tekst.

