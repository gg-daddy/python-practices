import PyPDF2


def rotate_pdf(src_pdf, output_pdf, rotation_degrees=180):
    with open(src_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            page.rotate(rotation_degrees)
            writer.add_page(page)
        with open(output_pdf, "wb") as output:
            writer.write(output)


def combine_pdfs(pdf_list, output_pdf="combined.pdf"):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_pdf)


def add_watermark(src_pdf, watermark_pdf, output_pdf):
    with open(src_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        watermark_page = PyPDF2.PdfReader(watermark_pdf).pages[0]
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:

            page.merge_page(watermark_page)
            writer.add_page(page)
        with open(output_pdf, "wb") as output:
            writer.write(output)


if __name__ == "__main__":
    combine_pdfs(["Get_Started_With_Smallpdf.pdf", "2402.04253.pdf"], "1-combined.pdf")
    add_watermark("1-combined.pdf", "wtr.pdf", "2-watermarked.pdf")
    rotate_pdf("2-watermarked.pdf", "3-result.pdf", rotation_degrees=270)
