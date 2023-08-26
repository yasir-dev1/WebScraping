from bs4 import BeautifulSoup
import requests
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

url = "https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find_all("p")
pattern = r"\d+\.\s"

# Collect the paragraphs that match the pattern
matching_paragraphs = []

for paragraph in paragraphs:
    strong = paragraph.find("strong")
    
    if strong is not None and re.match(pattern, strong.text):
        matching_paragraphs.append(paragraph.get_text())

# Write matching paragraphs to a PDF file
pdf_filename = "result.pdf"

c = canvas.Canvas(pdf_filename, pagesize=letter)
text = "\n\n".join(matching_paragraphs)

# Add the text to the PDF
c.drawString(100, 700, text)
c.save()

print(f"Matching paragraphs saved to {pdf_filename}")
