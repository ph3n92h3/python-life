import pdfplumber
import PyPDF2

pdf_file_path = 'automation_pdf/extract_text/text.pdf'

with pdfplumber.open(pdf_file_path) as pdf_file:
    print('（提取程序显示）文件', pdf_file_path[-pdf_file_path[::-1].find('/'):], '共',
          PyPDF2.PdfFileReader(open(pdf_file_path, 'rb')).getNumPages(), '页')

    text = '（提取程序显示）文件 '+str(pdf_file_path[pdf_file_path.find('/')+1:])+' 共 '+str(
        PyPDF2.PdfFileReader(open(pdf_file_path, 'rb')).getNumPages())+' 页'
    for page in range(len(pdf_file.pages)):
        print('\n（提取程序显示）##### 第', page+1, '页 ######\n')
        text += '\n\n（提取程序显示）##### 第 ' + str(page+1) + ' 页 ######\n' + \
            pdf_file.pages[page].extract_text()

    print('\n（提取程序显示）##### 提取结束 ######')
    text += '\n\n（提取程序显示）##### 提取结束 ######'

    open(pdf_file_path[:-3]+'txt', 'w').write(text)
