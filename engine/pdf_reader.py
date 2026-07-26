import fitz


class PDFReader:

    def __init__(self, pdf_path):
        self.pdf = fitz.open(pdf_path)

    def read(self):

        pages = []

        for page in self.pdf:
            pages.append(page.get_text())

        return pages


if __name__ == "__main__":

    reader = PDFReader("../samples/sample.pdf")

    pages = reader.read()

    for i, page in enumerate(pages):

        print("=" * 80)
        print("PAGE", i + 1)
        print("=" * 80)
        print(page)
