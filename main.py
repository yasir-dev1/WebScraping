from bs4 import BeautifulSoup
import requests
import re
from fpdf import FPDF

url = "https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# PDF dosyası oluştur
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

paragraphs = soup.find_all("p")
pattern = r"\d+\.\s"

for paragraph in paragraphs:
    strong = paragraph.find("strong")

    pattern = r"\d+\.\s"

    if strong is not None and re.match(pattern, strong.text):
        # Paragrafı PDF dosyasına yazdır
        pdf.multi_cell(0, 10, paragraph.get_text())
        pdf.ln()

# PDF dosyasını kaydet
pdf.output("paragraph_result.pdf")

print("PDF dosyası oluşturuldu: paragraph_result.pdf")
