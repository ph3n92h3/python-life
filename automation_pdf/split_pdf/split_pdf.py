from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = ''
pdf_file_reader = PdfFileReader(pdf_file_path)

for page in range(pdf_file_reader.getNumPages()):
    pdf_file_writer = PdfFileWriter()
    pdf_file_writer.addPage(pdf_file_reader.getPage(page))  # 每次添加单页

    with open(pdf_file_path[:-4]+f'_{page+1}.pdf', 'wb') as page_pdf:
        pdf_file_writer.write(page_pdf)
