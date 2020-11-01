import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200 :
        print(f'Success! Response = {response.status_code}')
        #print(f'content {response.text}')
        soup = BeautifulSoup (response.text, features="html.parser")
        print(f'Hasil pemanggilan = {url}')
        print(f'Tittle = {soup.title.string}')

    else:
        print(f'Oops, ada kesalahan pada request = {response.status_code}')
except Exception as e:
    print(f'There is an error = {e}')