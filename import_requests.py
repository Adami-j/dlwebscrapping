import requests
import itertools

url = "https://www.wawacity{}"

letters = "abcdefghijklmnopqrstuvwxyz"
max_len = 3

extensions = ['.' + ''.join(i) for i in itertools.product(letters, repeat=max_len)]

valid_extensions = ('.com', '.org', '.net', '.edu', '.gov', '.mil', '.co', '.info', '.biz', '.name', '.pro', '.mobi', '.tv', '.me', '.io', '.eu', '.fr', '.de', '.it', '.es', '.nl', '.be', '.ch')

valid_urls = []

for ext in extensions:
    test_url = url.format(ext)
    try:
        response = requests.get(test_url)
        if response.status_code == 200:
            if not ext.endswith(valid_extensions):
                valid_urls.append(test_url)
    except requests.exceptions.ConnectionError as e:
        #print(f"Erreur de connexion pour l'URL {test_url} : {e}")
        continue

print("Les URL valides sont : ")
for valid_url in valid_urls:
    print(valid_url)