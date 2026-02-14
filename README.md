DevOps mini project (Flask) 🚀
=============================

Prosta aplikacja webowa w Python (Flask) z testami + CI/CD na GitHub Actions oraz wdrożeniem do Azure.

------------------------------------------------------------

Wymagania ✅
-----------
- Python 3.11 🐍
- Git 🌿
- (Opcjonalnie) VS Code 💻

------------------------------------------------------------

Uruchomienie lokalnie (Windows / PowerShell) ▶️
----------------------------------------------

1) Aktywuj virtualenv:
   .\.venv\Scripts\Activate.ps1

2) Zainstaluj zależności:
   pip install -r requirements.txt

3) Uruchom aplikację:
   python app.py

------------------------------------------------------------

Endpointy 🌐
-----------
Po uruchomieniu lokalnie aplikacja działa tutaj:
- Home 🏠:     http://localhost:5000/
- Products 🛒: http://localhost:5000/products

------------------------------------------------------------

Testy 🧪
--------
Uruchom testy poleceniem:
python -m pytest

------------------------------------------------------------

CI (Continuous Integration) 🔁
------------------------------
Workflow CI uruchamia się automatycznie na Pull Requestach i:
- instaluje zależności,
- odpala testy (pytest),
- zapisuje raport testów jako artifact.

------------------------------------------------------------

CD (Continuous Deployment) 🚚
-----------------------------
Workflow CD uruchamia się automatycznie po push/merge do main i wdraża aplikację na Azure Web App.

Publiczny adres aplikacji 🌍:
https://devops-projekt-marcin537-g4e5adh6c4eefpbb.germanywestcentral-01.azurewebsites.net/

Dostępne endpointy na Azure:
- https://devops-projekt-marcin537-g4e5adh6c4eefpbb.germanywestcentral-01.azurewebsites.net/
- https://devops-projekt-marcin537-g4e5adh6c4eefpbb.germanywestcentral-01.azurewebsites.net/products

------------------------------------------------------------

Backlog / zadania 📌
-------------------
Projekt jest prowadzony w oparciu o:
- GitHub Issues (zadania)
- GitHub Projects (tablica Todo / In progress / Done)
- Pull Requesty powiązane z zadaniami
