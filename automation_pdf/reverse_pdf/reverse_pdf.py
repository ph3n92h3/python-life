from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = ''
pdf_file_reader = PdfFileReader(pdf_file_path)
pdf_file_writer = PdfFileWriter()

for page in range(pdf_file_reader.getNumPages()-1, -1, -1):
    pdf_file_writer.addPage(pdf_file_reader.getPage(page))

with open(pdf_file_path[:-4]+'_reversed.pdf', 'wb') as reversed_pdf:
    pdf_file_writer.write(reversed_pdf)
