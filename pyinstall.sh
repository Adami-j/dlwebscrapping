#!/bin/bash

# Verifier si Python est deja installe
if command -v python >/dev/null 2>&1 ; then
    echo "Python est deja installe"
else
    echo "Python n'est pas installe, telechargement de la derniere version..."
    curl https://www.python.org/ftp/python/3.10.0/python-3.10.0-macos11.pkg -o python_installer.pkg
    echo "Installation de Python..."
    sudo installer -pkg python_installer.pkg -target /
    rm python_installer.pkg
fi

# Verifier si Pip est deja installe
if command -v pip >/dev/null 2>&1 ; then
    echo "Pip est deja installe"
else
    echo "Pip n'est pas installe, telechargement de la derniere version..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    echo "Installation de Pip..."
    python get-pip.py
    rm get-pip.py
fi

echo "Termine."
