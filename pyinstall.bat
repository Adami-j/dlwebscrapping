@echo off

rem Verifier si Python est deja installe
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python est deja installe
) else (
    echo Python n'est pas installe, telechargement de la derniere version...
    curl https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe -o python_installer.exe
    echo Installation de Python...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
)

rem Verifier si Pip est deja installe
pip --version >nul 2>&1
if %errorlevel% == 0 (
    echo Pip est deja installe
) else (
    echo Pip n'est pas installe, telechargement de la derniere version...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    echo Installation de Pip...
    python get-pip.py
    del get-pip.py
)

echo Terminé.