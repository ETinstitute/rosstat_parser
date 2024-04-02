import fitz
from fitz import Page


with fitz.open('osn-12-2023.pdf') as doc:
    print(doc.pages())

    for page in doc.pages():

        page: Page

        print(page.get_textbox())
