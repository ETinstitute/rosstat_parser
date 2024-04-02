import fitz
import tabula


def find_page_with_keyword(keyword, filename):
    doc = fitz.open(filename)

    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        text = page.get_text()

        if keyword in text:
            return page_number

    return None


def get_table_by_page(page_number, filename):
    table = tabula.read_pdf(filename, pages=page_number)
    return table


def main():
    filename = "osn-12-2023.pdf"
    keyword = "ИНДЕКСЫ ПРОМЫШЛЕННОГО ПРОИЗВОДСТВА"

    if page_number := find_page_with_keyword(keyword, filename):
        print(f"Страница с ключевым словом '{keyword}' найдена на странице {page_number}.")
        table = get_table_by_page(filename=filename, page_number=page_number)
        print(table[0])

    else:
        print(f"Ключевое слово '{keyword}' не найдено в PDF-файле.")


if __name__ == "__main__":
    main()
