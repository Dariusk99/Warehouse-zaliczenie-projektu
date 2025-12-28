# ERP Warehouse & Order management system
56031 Dariusz Kośnicki
Python 3.13.0

ERP Warehouse & Order Management System to prosta aplikacja webowa do zarządzania stanem magazynowym oraz obsługą zamówień. Projekt umożliwia:

-Dodawanie i śledzenie produktów w magazynie.
-Wyświetlanie zamówień dodanych przez klienta.
-Możliwość składania zamówień po stronie klienta.

Strona klienta została dodana wyłącznie w celach testowych by nie używać postmana. Działa w tym samym origin by uprościć cały deployment i ominąć zbędną konfiguracje CORS, proxy.

Technologie:
Backend: Flask
Frontend: HTML, CSS, JS
Database: In memory
ORM: SQLAlchemy
Walidacja: Marshmallow

Instalacja:
1. Sklonuj repo
git clone https://github.com/Dariusk99/Warehouse-zaliczenie-projektu.git
cd Warehouse-zaliczenie-projektu
2. Utwórz wirtualne środowisko
python -m venv venv
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
3. Zainstaluj zależności
pip install -r requirements.txt
4. Uruchom plik startowy
python Warehouse.py

Przykładowy sposób użycia:
1. Otwórz stronę startową localhost:5000 i przejdź do linku "ERP System".
2. W zakładce "Magazyn", dodaj nowy przedmiot do magazynu.
3. Wróć na stronę localhost:5000 i przejdź do linku "Strona klienta".
4. Zarejestruj się i zaloguj. Po zalogowaniu dodaj przedmiot do koszyka.
5. W zakładce "Koszyk" przejdź do linku "Zamów". Wypełnij formularz i kliknij "Zamawiam"
6. Wróć na stronę "ERP System" i sprawdź czy zamówienie od klienta pojawiło się w zakładce "Zamówienia"