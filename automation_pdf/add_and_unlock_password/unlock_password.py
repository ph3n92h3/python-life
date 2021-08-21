# 注意，是已知密码而解除，不是未知密码而破解
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = ''
password = ''  # 这里是欲解除的密码，字符串格式

pdf_file_reader = PdfFileReader(pdf_file_path)
pdf_file_reader.decrypt(password)

pdf_file_writer = PdfFileWriter()

for page in range(pdf_file_reader.getNumPages()):
    pdf_file_writer.addPage(pdf_file_reader.getPage(page))

with open(pdf_file_path[::-4]+'_with_password.pdf', 'wb') as pdf_with_password:
    pdf_file_writer.write(pdf_with_password)
