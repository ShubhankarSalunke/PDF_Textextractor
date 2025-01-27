from PyPDF2 import PdfReader

path = #Path to the file

reader = PdfReader(path)

for page_num, page in enumerate(reader.pages, start =1):
    print(f"Page Number : {page_num}")
    print(page.extract_text())
    print("-" * 100)

print(text) 
