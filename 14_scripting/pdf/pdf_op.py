import PyPDF2

with open("Get_Started_With_Smallpdf.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    print(page)
    page.rotate(180)

    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
