from PyPDF2 import pdf
import pdfplumber
import PyPDF2

# 可以很简单地打包成函数
pdf_path = 'pdf_get_content/source.pdf'

with pdfplumber.open(pdf_path) as pdf_file:
    print('文件', pdf_path[pdf_path.find('/')+1:], '共', PyPDF2.PdfFileReader(
        open(pdf_path, 'rb')).getNumPages(), '页')

    content = ''
    for index in range(len(pdf_file.pages)):
        print('第', index+1, '页')
        page_text_content = pdf_file.pages[index].extract_text()
        print(page_text_content)
        content += page_text_content+'\n'
