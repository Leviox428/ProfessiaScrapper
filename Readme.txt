ProfesiaScrapper

ProfesiaScrapper je webscraping aplikácia, ktorá získava a analyzuje dáta zo stránky profesia.sk. Cieľom aplikácie je zhromažďovať informácie o pracovných ponukách na Slovensku, konkrétne o počte ponúk v jednotlivých regiónoch a priemernej mzde v každom regióne.

Funkcionalita aplikácie
Aplikácia je rozdelená na dve hlavné časti:

	1.Serverová časť - Server každú hodinu vykonáva webscraping na stránke profesia.sk a získané dáta ukladá do Firestore databázy. Tento proces je 	automatizovaný a zabezpečuje, že aplikácia má vždy aktuálne údaje.

	2.Klientská časť - Klientská aplikácia je určená pre používateľov, ktorí sa môžu zaregistrovať a prihlásiť. Po prihlásení môžu zobraziť 	vizualizované údaje o počte pracovných ponúk a priemernej mzde v jednotlivých regiónoch Slovenska. Grafy sú zobrazené vo forme stĺpcových grafov, čo 	používateľom umožňuje jednoduchú analýzu údajov.

Ciele aplikácie
Získať aktuálne dáta o pracovnom trhu na Slovensku zo stránky profesia.sk.
Umožniť používateľom prehľadné zobrazenie počtu pracovných ponúk a priemernej mzdy v rôznych regiónoch.
Poskytnúť vizuálne analýzy týchto údajov prostredníctvom grafov.
ProfesiaScrapper je užitočný nástroj pre každého, kto sa zaujíma o dynamiku pracovného trhu na Slovensku a chce mať prístup k aktuálnym údajom o pracovných príležitostiach a mzdách v rôznych regiónoch.

Zoznam použitých modulov (ukážky v Jupiter notebooku):
customtkinter - Grafické rozhranie aplikácie (GUI)
matplotlib - grafy
flask - python server
schedule - plánovanie (vykonávanie) funkcie v časových intervaloch napr. každú hodinu
threading - modul pre multithreading
time - modul pre prácu s časom 
bs4 (beautifull soup) - modul pre webscrappovanie, teda získavanie html zo stránok
re - modul pre regexy
request - modul pre vykonávanie http requestov
firebase_admin - firebase admin SDK pre prácu s databázou
dataclasses - modul pre vytváranie data tried
os - modul pre prácu s operačným systémom
dotenv - modul pre prácu s .env súbormi

Zdroje:
https://www.profesia.sk - stránka, z ktorej aplikácia zbiera dáta
https://firebase.google.com/docs/firestore - príručka a dokumentácia na používanie firestore databázy a firestore auth na login a register
https://www.geeksforgeeks.org/how-to-use-threadpoolexecutor-in-python3/ - použitý kód pre multithreading