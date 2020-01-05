import requests
import re

f = open('chapter3/igirisu.txt')
s = f.read()
f.close()

kokki = re.search(r'\|国旗画像\s=\s(.*)', s).group(1)

URL = 'https://en.wikipedia.org/w/api.php'

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:" + kokki,
    "iiprop": "url"
}
print(PARAMS)
response = requests.get(URL, params=PARAMS).json()

print(response['query']['pages']['23473560']['imageinfo'][0]['url'])
