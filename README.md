# Instrukcja uruchomienia skryptu

Ten plik README zawiera instrukcje dotyczące uruchomienia skryptu znajdującego się w tym repozytorium. Aby poprawnie uruchomić skrypt, postępuj zgodnie z poniższymi krokami:

## Wymagania wstępne

1. Upewnij się, że masz zainstalowaną bazę danych PostgreSQL. Jeśli nie masz jej jeszcze zainstalowanej, możesz pobrać ją ze strony [postgresql.org](https://www.postgresql.org/) i postępować zgodnie z instrukcjami instalacji dla swojego systemu.

## Pobranie repozytorium

1. Sklonuj lub pobierz zawartość tego repozytorium na swój lokalny komputer
2. Przejdź do katalogu z pobranym repozytorium:
	

## Konfiguracja bazy danych

1. Otwórz plik `private.cfg` znajdujący się w repozytorium.

2. Wprowadź odpowiednie zmiany:

	```ini
	[SQL]
	DB_NAME_DEFAULT = postgres
	DB_USER = postgres
	DB_PASSWORD = TWOJE_HASLO
	```

Zastąp 'TWOJE_HASLO' swoim rzeczywistym hasłem dostępu do bazy danych PostgreSQL.

## Uruchamianie skryptu

1. Upewnij się, że masz zainstalowane środowisko umożliwiające uruchamianie notatników Jupyter (np. Jupyter Notebook) lub edytora kodu (np. Visual Studio Code).

- **Jupyter Notebook**: Jeśli nie masz go jeszcze zainstalowanego, możesz to zrobić, używając komendy:

	```
	!pip install jupyter
	```
- **Visual Studio Code**: Jeśli preferujesz korzystanie z edytora kodu, upewnij się, że masz zainstalowany [Visual Studio Code](https://code.visualstudio.com/) oraz odpowiednie rozszerzenia do pracy z językiem, który jest używany w skrypcie.

2. Uruchom odpowiednie środowisko (Jupyter Notebook lub Visual Studio Code) i otwórz plik `run_script.ipynb`.

3. Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki. Jeśli nie to zainstaluj, używając komendy:

	```
	!pip install ipython-sql
	!pip install configparser
	!pip install pandas
	!pip install psycopg2
	```

4. W pliku `run_script.ipynb` wykonaj wszystkie kroki opisane w notatniku, aby uruchomić skrypt.

5. Postępuj zgodnie z instrukcjami i wykorzystaj plik `private.cfg` z poprawnie wprowadzonymi danymi dostępowymi do bazy danych.

