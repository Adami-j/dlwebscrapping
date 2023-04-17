# EN

# Description
The purpose of this application is to download files from a website called "Wawacity" using the "AllDebrid" service. The application allows the user to specify the Wawacity site URL, the AllDebrid API key, and the desired hosting service name (e.g., Uptobox, Turbobit, etc.). The application then scrapes the download links from the Wawacity site, unlocks them with AllDebrid, and saves them to a text file. The user can also load previously saved links from the text file and download the corresponding files. The application also allows the user to select a download folder to save the downloaded files. Additionally, the application clears the content of the text file upon closing.

## Here are the steps:
### 1-
# Windows
if you don't have Python or pip, run the .bat script pyinstall.bat, and then run the second script requirementInstall.bat to install all required external libraries.
# MacOS
open terminal in your project directory
execute following commands 
chmod u+wrx pyinstall.sh 
chmod u+wrx requirementInstall.sh
then execute 
./pyinstall.sh    
./requirementInstall.sh    

### 2-
launch the application with python3 launch.py in the command prompt or with the Python interpreter by right-clicking and selecting ******.

### 3-
So when you're in the app![image](https://user-images.githubusercontent.com/71751140/232118603-38e2f88c-28ea-4ff2-914a-a8be63b1e094.png)
You can see 3 buttons : 
The first's search particular host (example : you wanna download Turbobit links -> select it)
The second launch the scrap of all links in the firstly provided url. F.E: ![image](https://user-images.githubusercontent.com/71751140/232122749-cdca4760-e310-4ea1-a3ef-a49dca8449ec.png)

When you scraps links, you can observe that a new file has been created scrappedLinks.txt, it will be removed when you stoped the app. ![image](https://user-images.githubusercontent.com/71751140/232122822-6e6e4182-dba0-4f68-a2d4-950ab2aed48c.png)
 
Then if you want to download theses files, get your api key on https://alldebrid.fr/ 
and click on Alldebrid process, you'll see finder window : select folder where yw to download and wait.

# Remember that you can only download content you already own physicaly 


# FR
# Description

Le but de cette application est de télécharger des fichiers depuis un site web appelé "Wawacity" en utilisant le service "AllDebrid". L'application permet à l'utilisateur de spécifier l'URL du site Wawacity, la clé d'API AllDebrid et le nom du service d'hébergement souhaité (par exemple, Uptobox, Turbobit, etc.). L'application récupère ensuite les liens de téléchargement du site Wawacity, les déverrouille avec AllDebrid et les enregistre dans un fichier texte. L'utilisateur peut également charger les liens précédemment enregistrés à partir du fichier texte et télécharger les fichiers correspondants. L'application permet également à l'utilisateur de sélectionner un dossier de téléchargement pour enregistrer les fichiers téléchargés. De plus, l'application efface le contenu du fichier texte lors de la fermeture.

## Voici les étapes :

### 1-
Windows
Si vous n'avez pas Python ou pip, exécutez le script .bat pyinstall.bat, puis exécutez le deuxième script requirementInstall.bat pour installer toutes les bibliothèques externes requises.

MacOS
Ouvrez le terminal dans votre répertoire de projet
Exécutez les commandes suivantes
chmod u+wrx pyinstall.sh
chmod u+wrx requirementInstall.sh
puis exécutez
./pyinstall.sh
./requirementInstall.sh

### 2-
Lancez l'application avec python3 launch.py dans l'invite de commande ou avec l'interpréteur Python en faisant un clic droit et en sélectionnant ******.

### 3-
Donc lorsque vous êtes dans l'application image
Vous pouvez voir 3 boutons :
Le premier permet de rechercher un hébergeur particulier (par exemple : vous voulez télécharger des liens Turbobit -> sélectionnez-le)
Le deuxième lance la récupération de tous les liens dans l'URL fourni en premier. Par exemple : image

Lorsque vous récupérez les liens, vous pouvez observer qu'un nouveau fichier a été créé, "scrappedLinks.txt", qui sera supprimé lorsque vous arrêterez l'application. image

Ensuite, si vous souhaitez télécharger ces fichiers, récupérez votre clé d'API sur https://alldebrid.fr/ et cliquez sur le processus Alldebrid. Vous verrez une fenêtre de recherche : sélectionnez le dossier où vous souhaitez télécharger et attendez. 

# Rappelez-vous que vous ne pouvez télécharger que du contenu que vous possédez déjà physiquement