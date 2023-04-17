#RECOMMENDINATOR
###Aplikacja do Polecania Filmów i Seriali
####Hubert Tomana, Jakub Szostak
##1. Opis tematu projektu
Projekt ma na celu stworzenie aplikacji do polecania filmów i seriali, wykorzystując przy tym zarówno
Collaborative Filtering oraz Content-Based Filtering. Dodatkowo chcielibyśmy stworzyć GUI 
pozwalające na swobodne wykorzystywanie tej aplikacji.
##2. Szczegóły Działania Aplikacji
* Po wpisaniu tytułu, który nam się podobał, wyświetli się lista proponowanych filmów i seriali, 
która zostanie utworzona na podstawie dwóch metod : 
  * Content-Based Filtering – Wybieranie polecanych filmów na podstawie jego cech, jak 
  reżyser, aktorzy, gatunek, opis, porównując do wpisanego filmu
  * Collaborative Filtering – Polecanie na podstawie innych użytkowników. Metoda ta 
  wykorzystywać będzie do tego oceny użytkowników w bazie
* Dodatkowo chcielibyśmy dodać opcję wyświetlania proponowanych filmów bez wpisywania 
uprzednio żadnego tytułu.
* Program będzie wykorzystywał bazę użytkowników oraz filmów wraz z ich ocenami w plikach 
.csv dołączonych do projektu.
* Strategie wyszukiwania : 
  * Będzie dostępne wyszukiwanie zarówno po tytule, aktorze oraz reżyserze, jak i 
  gatunku filmu. 
  * Wyszukiwanie będzie również odporne na potencjalne błędy w pisowni – biblioteka 
  difflib.
  * GUI będzie umożliwiało wpisanie tekstu od użytkownika oraz wyboru kategorii, po której 
  dany użytkownik chce szukać.
##3. Wykorzystane technologie
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
##4. Harmonogram pracy
* GUI oraz API –> 03.04 – 17.04
* Wybór i połączenie baz danych –> 17.04 – 24.04
* Działanie systemów filtracji, implementacja systemu polecania -> 24.04 – 15.05
  * Załadowanie baz danych
  * Implementacja wyszukiwania
  * Algorytm tworzący listę polecanych filmów
  * Poprawki i dopełnienie projektu