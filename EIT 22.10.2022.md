# 22.10.2022
___
created: 22-10-2022 14:11
tags: #EIT
author: Bartłomiej Kotarski
___


# Oprocentowanie proste: 

Jeżeli dochód od wypożyczonego kapitału wypłacany jest jego właścicielowi po upłynięciu każdego roku to wówczas jego obliczenie zostaje dokonane za pomocą procentu prostego. 

$$I = P * i * n$$
$$F = P + J$$
$$i = \frac{p}{100}$$
p[%]
i[i]

- **P** = Wartość początkowa wypożyczonego kapitału (Sa to np nakłady inwestycyjne poniesione na budowę elektrowni) [wyrażona w złotówkach].
- **p** = Jest to roczna stawka procentowa dochodu (zysku) od wypożyczonego kapitału. (oprocentowanie kapitału, stawka akumulacyjna, czynnik dyskontowy) [wyrażona w procentach].
- **i** = Jest to roczna stawka oprocentowania lecz wyrażana w postaci ułamka dziesiętnego. 
- **n** = Jest to okres, na który kapitał został pożyczony. (Okres działalności inwestycyjnej) [wyrażana w latach].
- **I** = Dochód (zysk) z wypożyczonego kapitału za okres `n` lat.
- F = Wartość końcowa wypożyczonego kapitału po `n` latach. [wartość wyrażana w złotówkach].

**Zadanie 1**
Jaka będzie wartość końcowa i dochód (zysk) z kapitału początkowego `P = 1000zł` wypożyczonego na `n = 4 lata`
przy jego oprocentowaniu prostym `p=6%`

$I = P * n * i = 1000 * 4 * 0,06 = 240$
$F = P + J = 1000 + 240 = 1240 zł$

**Zadanie 2** 
Po jakim czasie kapitał początkowy `p = 1000zł` wzrośnie do `F równego 1500 zł` , jeśli jego oprocentowanie proste wynosi `p = 7%`. 
Jaka jest wartość dobowa oprocentowania?

$$i_d = \frac{i}{365}$$
$J = F - P = 1500 - 1000 = 500zł$
$n = \frac{J}{P * i} = \frac{500}{0,07 * 1000} = 7,14 lat$
$i_d = \frac{0,07}{365} = 0,0002$


---

# Oprocentowanie składanie okresowe (nie-ciągłe)

Jeżeli dochód (zysk) z wypożyczonego kapitału, **nie jest wypłacany** co roku, lecz doliczany do wypożyczonego kapitału (przy czym jest on doliczany w końcu roku) to wówczas mamy do czynienia z oprocentowaniem kapitału, procentem składanym okresowym (nieciągłym), doliczane są procenty do procentów. Mówimy wówczas o akumulacji (nagromadzeniu kapitału)

Wówczas wartość kapitału początkowego P po n latach działalności można wyznaczyć ze wzoru:
$$F = P (1 + i)^n$$
$$F = P * u ^n$$
$$u = 1 + i$$

- **u** = Czynnik oprocentowujący. Jest on odwrotnością czynnika dyskontującego.


Obliczanie wartości końcowej kapitału po `n latach`  gdy znana jest jego wartość początkowa (liczmy F a znamy P) nosi nazwę **akumulowania**. 

A obliczanie wartości początkowej kapitału (znamy P a liczymy F), gdy znana jest jego wartość końcowa po `n latach` nosi nazwę **dyskontowania**.

**Dyskontem** nazywamy odsetki potrącone przez nabywcę zobowiązania pieniężnego, płatnego w terminie późniejszym. 


**Zadanie 4**
Jaka będzie wartość końcowa kapitału początkowego  `P = 1000zł` wypożyczonego na 4 lata przy jego oprocentowaniu składanym `p = 6%`. Jaka będzie wartość końcowa???

- n = 4 lata
- P = 1000zł
- p = 6% 

$F = 1000 * (1 + 0,06)^4 = 1262,48$
$J = F - P = 1262,48 - 1000 = 262,48zł$

Porównując zadaniem 1, zysk jest większy przy **oprocentowaniu składanym** niż przy **oprocentowaniu prostym**. Jest to korzystniejsze rozwiązanie dla osoby wypożyczającej, procent prosty jest korzystniejszy dla pożyczającego. 


**Zadanie 5**
Po jakim czasie kapitał początkowy `P = 1000zł` wzrośnie do `F = 1500 zł`, jeżeli będzie on oprocentowany procentem składanym `p = 7%`. 

$$n = \frac{log\frac{F}{P}}{log(1 + i)}$$
$n  \approx 6 lat$

*Jakie byłoby w tym przypadku oprocentowanie dobowe?*

**Wnioski** - porównując wynik z zadaniem 2, widać, że zastosowanie procentu składanego skróciło okres oprocentowania z **7,14 lat** do **6 lat** (a więc o 1 rok/1 miesiąc i 22 dni)



**Zadanie 6**
Jaka była wartość początkowa kapitału, jeśli oprocentowanie **procentem składanym** `p = 6%` przez okres `n = 4 lata` przedstawia on wartość końcową `F = 1000 zł` 


**Zadanie 7**
Jaka była wartość początkowa kapitału, jeśli oprocentowanie **procentem prostym** `p = 6%` przez okres `n = 4 lata` przedstawia on wartość końcową `F = 1000 zł`. 
- P = ?

$$I = P * i * n \Longrightarrow P = \frac{I}{i * n}$$
$$F = P + J \Longrightarrow P = F - J$$
$P = \frac{F}{i * n + 1} = \frac{1000}{0,06 * 4 + 1} = 806,45zł$
