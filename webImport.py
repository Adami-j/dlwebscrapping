import requests
from bs4 import BeautifulSoup

url = "URL"  # URL of the website you want to scrape

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open("turbobit_links.txt", "w") as f:
    for link_row in soup.find_all("tr", class_="link-row"):
        link = link_row.find("a", class_="link")
        host_name = link_row.find("td", class_="text-center")
        preferred_host = "Turbobit"  # Name of your preferred host
        if link and host_name and preferred_host in host_name.text:
            f.write(link["href"] + "\n")

print("Turbobit links saved in turbobit_links.txt")