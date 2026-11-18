from pypdf import PdfReader
from backend.constants import DATA_PATH


def extract_text_from_pdf(path) -> str:
    all_text = ""

    reader = PdfReader(path)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n"

    return all_text

def export_txt(text, path):
    with open(path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    print(DATA_PATH)