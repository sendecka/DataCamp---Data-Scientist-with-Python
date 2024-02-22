# 4 - Macierze
#### 1. Utwórz macierz z 3 wierszy i 8 kolumn z wartościami 1:24
```
matrix(1:24, nrow=3, ncol=8)
```
#### 2. Utwórz macierz z wartościami 1:24 z 4 kolumnami
```
matrix(1:24, ncol=4)
```
#### 3. Urzywając funkcji dim() utwórz macierz m1 z vectora 1:10 o wymiarach 2 wiersze 5 kolumn
```
m1 <- 1:10
dim(m1) <- c(2,5); m1
```
#### 4. Używając funkcji dim() utwórz macierz m2 z vectora -4:3 o wymiarach 2 wiersze 4 kolumny
```
m2 <- -4:3
dim(m2) <- c(2,4); m2
```
#### 5. Połącz macierze m1 i m2
```
m1m2 <-cbind(m1, m2)
m1m2
```
#### 6. Wyświetl wymiar otrzymanego wyniku
```
dim (cbind(m1, m2))
dim(m1m2)
```
#### 7. Utwórz macierz, której wierszami będą wektory: 1:5, 5:9, (1,5,3,2,6)
```
rbind(1:5, 5:9, c(1, 5, 3, 2, 6))
```
#### 8. Utwórz 3 wektory od długości 10 elementów o wartości z zakresu od -3 do 3. Nazwij je v1, v2, v3.
```
v1 <- sample(-3:3, 10, replace = T)
v2 <- sample(-3:3, 10, replace = T)
v3 <- sample(-3:3, 10, replace = T)
v1; v2; v3
```
#### 9. Utwórz macierz, której kolumnami będą vektory v1, v2, v3
```
rbind(v1, v2, v3)
```
#### 10. Utwórz macierz mt o 3 kolumnach i 20 wierszach. W pierwszej kolumnie powinny pojawić się wartości kolejno od 1 do 20, w drugiej na przemian wartości -5 i 6, w trzeciej wartości od 40:59.
```
mt <- cbind(1:20, c(-5,6), 40:59); mt
```
#### 11. Z macierzy mt wybierz pierwszy, trzeci i ostatni element.
```
mt[c(1,3, length(mt))]
```
#### 12. Z macierzy mt wybierz kolumny parzyste
```
mt[ ,c(F,T)]
```
#### 13. Z mt wybierz wszystkie wiersze bez 3 i 17
```
mt[-c(3,17),]
```
#### 14. Dodaj do mt wiersz z liczbami z zakresu od -600 do 300
```
rbind(mt, seq(-600,300, length.out = 3))
```
#### 15. Z macierzy mt wybierz te kolumny, które w 4 wierszu mają wartości z zakresu od -10 do 280
```
mt[ , mt [4, ] >= -10 & mt [4, ] < 280]
```
#### 16. Z macierzy wybierz elementy większe od 20
```
mt[mt > 20]
```
#### 17. Do kolumny 2 wiersz 1 wpisz wartość 42
```
mt[1,2] <- 42
```
#### 18. Do kolumny 3 wpisz wartość 5
```
mt[ ,3] <- 5
```
#### 19. (*) Dla wierszy 2 i 3 dla wartości parzystych wpisz wartość 2. 
```
mt[2, ]
mt[3, ]
mt[2, mt[2, ]%% 2 == 0] <- 2
mt[3, mt[3, ]%% 2 == 0] <- 2
mt
```


# Zadanie 5. Listy

#### 1. Utwórz listę 11 z 3 elementów a1: vector numeryczny 5 elementowy, a2: 3 elementowy wektor logiczny, a3: 13 elementowy vector znakowy
```
l1 <- list(a1 = c(1,2,6,9,5), a2 = c(T,F,F), a3 = letters[2:14])
```
#### 2. Wybierz element a3 listy
```
l1$a3
```
#### 3. Sprawdź typ wybranego elementu
```
typeof(l1$a3)
```
#### 4. Wybierz element a1 jako vector
```
v <- l1$a1; v
```
#### 5. Wybierz pierwsze 3 elementy z a3
```
l1$a3[1:3]
```
#### 6. Wyświetl nazwy elementów listy
```
names(l1)
```
#### 7. Dodaj do listy element 'moj' w postaci macierzy 3 kolumny 4 wiersze o wartości z zakresu 1:12
```
l1$moj <- matrix(1:12, ncol = 4, nrow = 3)
```
#### 8 .Wypisz wartość 4 do 3 elementu vectora a1
```
l1$a3[3] <- 4
```
#### 9. Stwórz listę 12 złożoną z 3 wektorów liczbowych 1:43, 3:56, -5:8
```
l2 <- list (1:43, 3:56, -5:8);l2
```
#### 10. Połącz listę l1 i l2 w listę l3
```
l3 <- c(l2, l1); l3
```
#### 11. (*) Dodaj listę l1 jako element l2
```
l2$l1 <- l1;l2
```
#### 12. (*) Wybierz z macierzy 'moj' 2 wiersze i kolumny o wartościach powyżej średniej wartości elementów z a1
```
l1$moj
l1$moj[2, ]
mean(l1$a1)
l1$moj[2,l1$moj[2, ] > mean (l1$a1)]
```
