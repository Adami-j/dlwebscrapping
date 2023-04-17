@echo off

rem Verifier si pip est installe
pip --version >nul 2>&1
if %errorlevel% == 0 (
    echo pip est deja installe
) else (
    echo pip n'est pas installe, telechargement de la derniere version...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    echo Installation de pip...
    python get-pip.py
    del get-pip.py
)

rem Installer les bibliotheques requises
pip install tkinter
pip install requests
pip install beautifulsoup4
pip install undetected-chromedriver
pip install selenium
pip install urllib3

echo Termine.