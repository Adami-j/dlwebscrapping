@echo off

rem Vérifier si pip est installé
pip --version >nul 2>&1
if %errorlevel% == 0 (
    echo pip est déjà installé
) else (
    echo pip n'est pas installé, téléchargement de la dernière version...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    echo Installation de pip...
    python get-pip.py
    del get-pip.py
)

rem Installer les bibliothèques requises
pip install tkinter
pip install requests
pip install beautifulsoup4
pip install undetected-chromedriver
pip install selenium
pip install urllib3

echo Terminé.