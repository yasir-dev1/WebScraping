from bs4 import *
import requests
import re

url = "https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php"


r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

paragraphs = soup.find_all("p")
pattern = r"\d+\.\s"

for paragraph in paragraphs:
    strong = paragraph.find("strong")
    
    

    pattern = r"\d+\.\s"

    if strong is not None and re.match(pattern, strong.text):
        print(paragraph.text)
