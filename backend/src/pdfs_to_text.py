from pypdf import PdfReader

all_text = ""

reader = PdfReader("data/Netherland_Dwarf_rabbit.pdf")
for page in reader.pages:
    text = page.extract_text()
    if text:
        all_text += text + "\n"

print(all_text)