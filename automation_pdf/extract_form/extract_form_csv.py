import pdfplumber
import pandas as pd

pdf_file_path = 'automation_pdf/extract_form/form1.pdf'

with pdfplumber.open(pdf_file_path) as pdf_file:
    for page in pdf_file.pages:
        for form in page.extract_tables():  # 读取每个表格
            data = pd.DataFrame(form[1:], columns=form[0])
            data.to_csv(pdf_file_path[:-3]+'csv', mode='a', encoding='ANSI')
