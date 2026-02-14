# DevOps mini project (Flask)

## Wymagania
- Python 3.11
- Git

## Uruchomienie lokalnie (Windows PowerShell)
1. Aktywuj venv:
   .\.venv\Scripts\Activate.ps1

2. Zainstaluj paczki:
   pip install -r requirements.txt

3. Uruchom aplikację:
   python app.py

Aplikacja:
- http://localhost:5000/
- http://localhost:5000/products

## Testy
Uruchom:
python -m pytest


## CI
Workflow CI uruchamia testy automatycznie na Pull Requestach (GitHub Actions).

## CD
Workflow CD wdraża aplikację automatycznie na Azure po push/merge do main.
Publiczny adres aplikacji: devops-projekt-marcin537-g4e5adh6c4eefpbb.germanywestcentral-01.azurewebsites.net.azurewebsites.net
