import tkinter as tk
import time
import sys
import os
import requests
import json
from bs4 import BeautifulSoup

import undetected_chromedriver as uc
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from tkinter import filedialog  # Importer filedialog séparément



def scrape_wawacity(url,host):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for link_row in soup.find_all("tr", class_="link-row"):
        link = link_row.find("a", class_="link")
        host_name = link_row.find("td", class_="text-center")
        preferred_host = host  # Name of your preferred host
        if link and host_name and preferred_host in host_name.text:
            print(link["href"])
            links.append(link["href"])

    return links

def process_link(links, api_key,host):
    driver = uc.Chrome()
    for link in links:
       
        driver.get(link)

        # Find and click the "continuer" button
        while True:
            try:
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "subButton")))
            except:
                # Retry if the CAPTCHA is not solved
                print("CAPTCHA not solved, retrying...")
                driver.get(link)
                continue

            try:
                # Click the "Continuer" button
                time.sleep(3)
                form = driver.find_element(By.ID, "myForm")
                form.submit()

                link_element = driver.find_element(By.XPATH, "//a[contains(@href, '"+host.lower()+"')]")

                # Extract the link from the href attribute
                link = link_element.get_attribute("href")
               
                filepath = os.path.join(os.getcwd(), "scrappedLinks.txt")  # Path to the output file

                if not os.path.exists(filepath):
                    open(filepath, 'w').close()  # Create the file if it doesn't exist

                with open(filepath, "a+", newline="", encoding="utf-8") as f:
                    f.write(link + "\n")
                
            except NoSuchElementException:
                print("Element not found, retrying...")
                continue
            
            except:
                print("Unknown exception, retrying...")
                continue

            break  # Exit the while loop once the link is processed successfully

        time.sleep(3)  # Wait for the browser to finish processing before closing the window

    driver.quit()

def download_series(url, api_key,host):
    links = scrape_wawacity(url,host)
    process_link(links, api_key,host)

def read_links_from_file(api_key):
    filepath = os.path.join(os.getcwd(), "scrappedLinks.txt")
    
    links = []
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                link = line.strip()  # enlever les espaces blancs autour du lien
                api_endpoint = f"https://api.alldebrid.com/v4/link/unlock?agent=myAppName&apikey={api_key}&link={link}"
                response = requests.get(api_endpoint)

                data = response.json()["data"]
                scraped_link = data["link"]
                print(scraped_link)

                links.append(scraped_link)
    return links

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Downloader wawa/alldebrid")
        self.master.geometry("400x550")
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        self.url_label = tk.Label(self.master, text="Wawacity url")
        self.url_label.pack()

        self.url_entry = tk.Entry(self.master, width=50)
        self.url_entry.pack()

        self.hosts = ["Uptobox", "Turbobit", "Nitroflare","Rapidgator","1fichier","Fikper","Filerice"]  # liste de noms d'hébergeurs

        self.host_label = tk.Label(self.master, text="Choose a hosting service:")
        self.host_label.pack()

        self.host_var = tk.StringVar()
        self.host_var.set(self.hosts[0])  # valeur par défaut

        self.host_menu = tk.OptionMenu(self.master, self.host_var, *self.hosts)
        self.host_menu.pack()

        self.api_label = tk.Label(self.master, text="API key")
        self.api_label.pack()

        self.api_entry = tk.Entry(self.master, width=50, show="*")
        self.api_entry.pack()

        self.download_button = tk.Button(self.master, text="Scrap links", command=self.start_download)
        self.download_button.pack()

        self.all_button = tk.Button(self.master, text="AllDebrid process", command=self.read_links_from_file)
        self.all_button.pack()

        self.output_label = tk.Label(self.master, text="Files")
        self.output_label.pack()

        self.output_text = tk.Text(self.master, height=20, width=80)
        self.output_text.pack()

    def start_download(self):
        url = self.url_entry.get()
        api_key = self.api_entry.get()
        host = self.host_var.get()
        if url and api_key:
            self.download_button.config(state=tk.DISABLED)
            self.output_text.delete('1.0', tk.END)
            download_series(url, api_key,host)
            self.download_button.config(state=tk.NORMAL)
    def read_links_from_file(self):
        api_key = self.api_entry.get()
        links =read_links_from_file(api_key)
        # Ouvrir une boîte de dialogue de sélection de dossier
        self.download_path = tk.filedialog.askdirectory(initialdir='')
        for link in links:
            filename = link.split("/")[-1]  # Extraire le nom du fichier à partir de l'URL
            filepath = os.path.join(self.download_path, filename)
            with open(filepath, "wb") as f:
                response = requests.get(link)
                f.write(response.content)
            print(self.download_path)
    def on_closing(self):
        filepath = os.path.join(os.getcwd(), "scrappedLinks.txt")
        with open(filepath, "w", encoding="utf-8") as f:
          f.write("")
        self.master.destroy()
        
   
  
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
