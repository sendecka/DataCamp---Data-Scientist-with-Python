

# 3.2 Część B
#### 1. Utwórz vector składający się z 13 pierwszych małych liter alfabetu i nazwij go l (? letters)
```
l <- letters[1:13]
```
#### 2. Z l wybierz 3 pierwsze elementy
```
l[1:3]
```
#### 3. Z l wybierz 3, 5, i 9 element
```
l[c(3, 5, 9)]
```
#### 4. Z l wybierz elementy o indeksach parzystych
```
l[c(F,T)]
```
#### 5. Wybierz z l elementy powyżej „g”
```
l[l>"g"]
```
#### 6. Utwórz vector q o długości 20 elementów składający się z wartości od -5 do 5
```
q <- seq(-5,5, length.out =  20)
q
q <- sample(-5:5, 20,replace = T)
q
```
#### 7. Utwórz logiczny vector z wartością true dla elementów q większych od 2
```
q>2
```
#### 8. Z q wybierz elementy większe od 2
```
lq <- q[q>2]
lq
```
#### 9. Policz ile jest takich elementów
```
length(q[q>2])
```
#### 10. Z q wybierz co 3 element
```
q[c(F,F,T)]
```
#### 11. Z q wybierz elementy których kwadrat jest większy od 7
```
q[q*q>7]
```
#### 12. Utwórz vectory: a1 z wartościami od 4 do 7 i a2 z wartościami od 0 do 9
```
a1 <- 4:7
a2 <- 0:9
```
#### 13. Oblicz sumę elementów a1 (? sum)
```
sum(a1)
```
#### 14. Posortuj vector d (? order)
```
d[order(d)]
```


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



# Zadanie 6. Factora

#### 1. Utwórz vector vf1 o długości 17 z elementów ("mały", "średni", "duży")
```
vf1 <- sample(c("mały", "średni", "duży"), 17, replace = T)
vf1
```
#### 2. Przekształć vf1 w faktor ff1 (bez kolejności)
```
ff1 <- factor(vf1)
```
#### 3. Utwórz vector vf2 o długości 14 z wartościami całkowitymi z przedziału od 1 do 6.
```
vf2 <- sample(1:6, 14, replace = T)
vf2
```
#### 4. Z vf2 utwórz factor ff2 tak aby poziomy miały nazwy od "F" do "A"
```
ff2 <- factor(vf2, levels = 1:6, labels = LETTERS[6:1])
ff2
```
#### 5. Wyświetl poziomy ff2
```
levels(ff2)
```
#### 6. Policz wystąpienia "C" w FF2
```
sum(ff2 == "C")
```
#### 7. Z vf2 utwórz ordered factor
```
ordered(vf2)
factor(vf2, ordered=T)
```
#### 8. Za pomocą table() wyświetl wynik dla vf2
```
table(vf2)
```
#### 9. Z ff2 wybierz elementy 1,5 i 12
```
ff2[c(1,5,12)]
```
#### 10. Z ff2 wybierz elementy o wartości "A" i "D"
```
ff2[ff2=="A" | ff2=="D"]
```


# Zadanie 7 DATA FRAME

#### 1. Utwórz Data Frame df ze zmiennych: 
#### a. C1 - vector 8 elementowy z imionami osób c("Ala", "Beata", "Marek", "Igor", "Franciszek", "Adam", "Tomek", "Argh")
#### b. S1 - vector 8 elementowy z płcią poszczególnych osób c("k", "k", "m", "m", "m", "m", "m", "m")
#### c. Hi - vecor z wzrostem w cm poszczególnych osób sample(100:220, 8)
```
c1 <- c("Ala", "Beata", "Marek", "Igor", "Franciszek", "Adam", "Tomek", "Argh")
s1 <- c("k", "k", "m", "m", "m", "m", "m", "m")
hi <- sample(100:220, 8)
df <- data.frame(c1, s1, hi);
```
#### 2. Wyświetl strukturę df
```
str(df)
```
#### 3. Wyświetl elementy df
```
df
```
#### 4. Wyświetl wymiar df
```
dim(df)
```
#### 5. Z df wybierz 2 i 5 linie
```
df[c(2,5),]
```
#### 6. Z df wybierz zmienną hi
```
df$hi
df[ ,3]
```
#### 7. Wyświetl nazwy zmiennych z df
```
colnames(df)
```
#### 8. Z df wybierz linie dla których w hi znajduje się wartość większa od 150
```
df[df$hi > 150,]
```



# Zadanie 8 Import/Eksport

#### 1. Utwórz wektory v <- -100:100, wektor logiczny 1 <- c(T,F,T,T,T,F), 
#### wektor c("A ja jaj", "OJ", "Pff")
```
V <- -100:100;v
l <- c(T,F,T,T,T,F); l
c <- c("A ja jaj", "OJ", "Pff"); c
```
#### 2. Zapisz wektor v do pliku vfile.RData
```
save(v,file="vfile.RData")
```
#### 3. Zapisz wektory l i c plik lc.RData
```
save(l,c,file="lc.RData")
```
#### 4. Przypisz wektor c do v
```
v<-c;v
```
#### 5. Załaduj dane z pliku vfile.RData
```
load(file="vfile.RData")
v
```
#### 6. Obejrzyj plik c1.csv i odczytaj z niego dane
```
read.table(file="c1.csv")
```
#### 7. Zapisz v do pliku vfile.csv
```
write.table(x=v, file="vfile.csv")
```
#### 8. Załaduj dane z pliku x1.xlsx
```
library(openxlsx)
read.x(sx(xlsxFile = "x1.xlsx", sheet = 1))
```
#### 9. Odczytaj dane z pliku r.dbf (użyj read.dbf z pakietu foreign)
```
library(foreign)
read.dbf(flie =  "r.dbf")
```


# Zadanie 9 Wartości specjalne

#### 1. Utwórz 100 elementowy wektor t z wartościami z zakrasu od 20 do 90
```
t<-sample(20:90, 100, replace = T);t
```
#### 2. W t wpisz w wartości NA dla wartości z przedziału od 60 do 80
```
t[t>60 & t<=80]<-NA
```
#### 3. Użyj is.na() na wektorze t
```
is.na(t)
```
#### 4. Utwórz 20 elementowy vector v o wartościach z przedziału od -7 do 3
```
v<-sample(-7:3,20,replace=T);v
```
#### 5. Policz pierwiastek z vectora v
```
sqrt(v)
```
#### 6. Wypisz wartości dla których pierwiastek daje wartość NAN
```
v[is.nan(sqrt(v))]
```
#### 7. Korzystając ze swojej wiedzy matematycznej utwórz vector vnii z wartościami Nan, -Inf, Inf
```
vnii<-c(sqrt(-1),exp(1000),-exp(1000))
```
#### 8. Sprawdź, które z wartości w tym wektorze są Inf i wypisz w nie wartośc 42,
```
vnii[vnii == Inf]<-42
vnii
```


# Zadanie 10 Podstawowe funkcje matematyczne

#### 1. Utwórz vector a jako -12:12
```
a<- -12:12;a
```
#### 2. Wylicz wartości bezwzględne elementów a
```
abs(a)
```
#### 3. Wylicz pierwiastek dla liczb z zakresu od -3 do 10
```
sqrt(-3:10)
```
#### 4. Dla każdego elementu a oblicz exp wynik przypisz do ve
```
ve <-exp(a); ve
```
#### 5. Oblicz logarytm z liczby 3
```
log(3)
```
#### 6. Użyj sinpi() do obliczeń sinusa 30 stopni
```
sinpi(1/6)
```
#### 7. Zaokrąglij wartość ve do liczb całkowitych
```
ve
round(ve);ve
```
#### 8. Zaokrąglij wartość ve do 3 miejsc po przecinku
```
round(ve, digits=3)
```
##### 9. Zaokrąglij wartość ve do pełnych 100
```
round(ve, digit = -2)
```
#### 10. Na wartościach ve użyj metody floor(), celing(), trun()
```
floor(ve)
ceiling(ve)
trunc(ve)
```



# Zadanie 11 Podstawowe funkcje znakowe

#### 1. Utwórz wektor znakowy s o zawartości "DUŻE", "małe, "te inne 123456789"
```
s <- c("DUŻE", "małe", "te inne 123456789")
s
```
#### 2. Oblicz liczbę znaków elementów s
```
nchart(s)
```
#### 3. Utwórz s1 jako połączenie elementów s oddzielowych spacją
```
s1<-paste(s,collapse=" ")
```
#### 4. Wyświetl s1 w postaci małych liter
```
tolower(s1)
```
#### 5. Utwórz 300 elementowy wektor a o zawartości: "a.1", "a.2", ...,"a.300"
```
a<-paste("a", 1:300, sep=",");a
```
#### 6. Znajdź indeks elementu "a.9"
```
match("a.9",a)
```
#### 7. W napisie "Ala ma kota. Ala na rybki" zmień "kota" na"psa"
```
ar<-sub(x=c("Ala ma kota. Ala ma rybki"), pattern="kota", replacement="psa")
ar
```


# Zadanie 12 Podstawowe funkcje losujące/funkcje analityczne

#### 1. Używając rozkładu normalnego wylosuj 30 liczb i zapisz je w wektorze v
```
v<-rnorm(30);v
```
#### 2. Oblicz średnią elementów v
```
mean(v)
```
#### 3. Oblicz medianę elementów v
```
median(v)
```
#### 4. Oblicz kwantyl rzędu 0.1 wektora v
```
quantile(v)
```
#### 5. Oblicz odchylenie standardowe v
```
sd(v)
```
#### 6. Utwórz wektor 7 elementowy p1 o zakresie wartości od -10 do 10
```
pl<-sample(-10:10, 7); pl
```
#### 7. Utwórz wektor -3:4 i nazwij go p2
```
p2<--3:4; p2
```
#### 8. Oblicz minimum z wartości p1
```
min(p1)
```
#### 9. Wylicz zakres wartości wektora v
```
range(v)
```
#### 10. Oblicz minimalne wartości między wektorami p1 i p2
```
p1; p2
pmin(p1,p2)
```


# Zadanie 13 Instrukcje sterujące

#### 1. Utwórz wektor v o 10 elementach z zakresu od -100:100
```
v<-sample(-100:100,10); v
```
#### 2. Napisz instrukcję warunkową tak by wyświetlić "TAK" 
#### jeśli średnia z elementów v jest większa niż 20 i "NIE" w przeciwnym wypadku
```
if (mean(v)>20){
  print("TAK")
} else{
  print("NIE")
}

ifelse(mean(v)>20, "TAK", "NIE")
if(mean(v)>20) print("TAK") else print("NIE")
```
#### 3. Korzystając z pętli for napisz skrypt wyliczający sumę elementów v i wyświetlający ją na konsoli
```
s<-0
for(e in v) {
  s<-s+e
}
s
sum(s)
```


# ZADANIE 14 WŁASNE FUNKCJE

#### 1. Napisz funkcję foo wyświetlającą na konsolę wartość podanego parametru
```
foo <- function(x) {
  print(x)
}

foo(14)
foo(1:8)
```
#### 2. Napisz funkcję hgtg zwracającą liczbę 42
```
hgtg <- function() {
  return(42)
}

c <-hgtg(); c
```
#### 3. Napisz funkcję goo zwracającą podany element wektora -100:100
```
goo <- function(x = 15) {
  return((-100:100)[x])
}

goo(4)
goo(48)
goo(4008)
goo(1:5)
```
#### 4. Zmodyfikuj goo tak by obsłużyć przypadki szczególne
```
goo <-function(x) {
  if(length(x) !=1) {
    warning("Za dużo wartości")
    return(NA)
  }
  if(x<1 | x>length(-100:100)) {
    warning("Indeks spoza zakresu")
    return(NA)
  }
  return((-100:100)[x])
}
goo(0)
goo(45)
goo(4000)
```
