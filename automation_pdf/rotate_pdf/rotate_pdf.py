from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = ''
pdf_file_reader = PdfFileReader(pdf_file_path)
pdf_file_writer = PdfFileWriter()

for page in range(pdf_file_reader.getNumPages()):
    pdf_file_writer.addPage(pdf_file_reader.getPage(
        page).rotateClockwise(90))  # 顺时针旋转: rotateClockwise, 逆时针: rotateCounterClockwise
# 只能旋转90的整数倍°

with open(pdf_file_path[:-4]+'_rotated.pdf', 'wb') as rotated_pdf:
    pdf_file_writer.write(rotated_pdf)
