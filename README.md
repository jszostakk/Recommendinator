# RECOMMENDINATOR

### Aplikacja do Polecania Filmów i Seriali

#### Hubert Tomana, Jakub Szostak

## 1. Opis tematu projektu

Projekt ma na celu stworzenie aplikacji do polecania filmów i seriali, wykorzystując przy tym mechanizm Content-Based Filtering. Dodatkowo chcielibyśmy stworzyć GUI 
pozwalające na swobodne wykorzystywanie tej aplikacji.

## 2. Szczegóły Działania Aplikacji

* Po wpisaniu tytułu, który nam się podobał, wyświetli się lista proponowanych filmów i seriali, 
która zostanie utworzona na podstawie metody Content-Based Filtering : 
  * Jest to metoda opierająca się na wybieraniu polecanych filmów na podstawie jego cech, jak 
  reżyser, aktorzy, gatunek, opis, porównując do wpisanego filmu
* Program będzie wykorzystywał bazę filmów oraz seriali w plikach 
.csv dołączonych do projektu.
* Strategie wyszukiwania :
  * GUI będzie umożliwiało wpisanie tekstu od użytkownika
  * Wyszukiwanie będzie odporne na potencjalne błędy w pisowni – biblioteka 
  Difflib.
  * Wymagane będzie wpisanie przez użytkownika tytułu filmu w języku angielskim.

## 3. Wykorzystane technologie
  
* Język Programowania – Python
  * Scikit Learn
  * Numpy
  * Pandas
  * Difflib
* GUI – Tkinter
* Prototyp – Figma
* Bazy Danych – Kaggle -> CSV
* Workspace/System Kontroli Wersji – Google Colab
* Task Manager - Jira

https://colab.research.google.com/drive/13ULzUI2c1Oy9Ay6sV5Jx4h9k98H4hEzK?usp=sharing

## 4. Harmonogram pracy

* GUI oraz API –> 03.04 – 17.04
* Wybór i połączenie baz danych –> 17.04 – 24.04
* Działanie systemów filtracji, implementacja systemu polecania -> 24.04 – 15.05
  * Załadowanie baz danych
  * Implementacja wyszukiwania
  * Algorytm tworzący listę polecanych filmów
  * Poprawki i dopełnienie projektu