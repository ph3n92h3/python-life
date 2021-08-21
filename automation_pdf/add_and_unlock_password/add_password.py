from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = ''
password = ''  # 这里是欲添加的密码，字符串格式

pdf_file_reader = PdfFileReader(pdf_file_path)
pdf_file_writer = PdfFileWriter()

for page in range(pdf_file_reader.getNumPages()):
    pdf_file_writer.addPage(pdf_file_reader.getPage(page))

pdf_file_writer.encrypt(password)

with open(pdf_file_path[::-4]+'_with_password.pdf', 'wb') as pdf_with_password:
    pdf_file_writer.write(pdf_with_password)

# 注：加水印和加密码经常同时操作（好像也就是调一个函数的事😂）
