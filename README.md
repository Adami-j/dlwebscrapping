# script-test-url

# Description
The purpose of this application is to download files from a website called "Wawacity" using the "AllDebrid" service. The application allows the user to specify the Wawacity site URL, the AllDebrid API key, and the desired hosting service name (e.g., Uptobox, Turbobit, etc.). The application then scrapes the download links from the Wawacity site, unlocks them with AllDebrid, and saves them to a text file. The user can also load previously saved links from the text file and download the corresponding files. The application also allows the user to select a download folder to save the downloaded files. Additionally, the application clears the content of the text file upon closing.

## Here are the steps:
### 1-
if you don't have Python or pip, run the .bat script pyinstall.bat, and then run the second script requirementInstall.bat to install all required external libraries.

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
