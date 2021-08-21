import pdfplumber
import pandas as pd

# 'automation_pdf/extract_form/form1.pdf'
pdf_file_path = 'automation_pdf/extract_form/mixed.pdf'

with pdfplumber.open(pdf_file_path) as pdf_file:
    with pd.ExcelWriter(pdf_file_path[:-3]+'xlsx') as xlsx_writer:
        count = 1
        for page in pdf_file.pages:
            for form in page.extract_tables():
                data = pd.DataFrame(form[1:], columns=form[0])
                data.to_excel(xlsx_writer, sheet_name=f'sheet{count}')
                count += 1
