from PyPDF2 import PdfFileReader, PdfFileWriter  # pdf文件读写工具
from reportlab.pdfbase import pdfmetrics  # 注册字体
from reportlab.pdfbase.ttfonts import TTFont  # 字体
from reportlab.pdfgen import canvas  # 创建pdf文件

pdfmetrics.registerFont(
    TTFont('font_name', 'pdf_watermark/Latin.ttf'))  # 注册字体

pdf_watermark_file_creater = canvas.Canvas(
    'pdf_watermark/watermark.pdf')  # 创建空白pdf文件

pdf_watermark_file_creater.setFont('font_name', 80)  # 设置字体，字号
pdf_watermark_file_creater.setFillColorRGB(
    0.9, 0.9, 0.9, 0.5)  # 使用RGB调色设置文字颜色，透明度
pdf_watermark_file_creater.rotate(55)  # 设置旋转角度（角度制）

pdf_watermark_file_creater.drawString(100, 0, 'watermark by python')  # 渲染文字

pdf_watermark_file_creater.save()  # 保存水印文件

pdf_source_reader = PdfFileReader(
    'pdf_watermark/source.pdf')  # 读取源文件

watermark_page = PdfFileReader(
    'pdf_watermark/watermark.pdf').getPage(0)  # 读取水印文件，并直接提取出页面

pdf_result_writer = PdfFileWriter()  # 创建写对象

for index in range(pdf_source_reader.getNumPages()):
    page = pdf_source_reader.getPage(index)
    page.mergePage(watermark_page)  # 合并两页面
    # 注意，这样生成的带水印的pdf文件是源文件在下水印在上，欲源文件在下而水印在上则创建水印文件时需要生成多个页面，同时这里将源文件逐页面页叠加在水印文件上
    pdf_result_writer.addPage(page)  # 将合并出的页面写入文件

pdf_result_writer.write(open('pdf_watermark/result.pdf', 'wb'))  # 保存结果文件
