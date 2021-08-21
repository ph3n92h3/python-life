from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_paths = ()  # 要合并的pdf文件的路径
pdf_merge_pdf_path = ''  # 合成的pdf文件的路径
pdf_file_writer = PdfFileWriter()

for pdf_file_path in pdf_file_paths:  # 逐个pdf
    pdf_file_reader = PdfFileReader(pdf_file_path)
    for page in range(pdf_file_reader.getNumPages()):  # 逐页
        pdf_file_writer.addPage(pdf_file_writer.getPage(page))

with open(pdf_merge_pdf_path, 'wb') as merge_path:
    pdf_file_writer.write(merge_path)
