from PyPDF2 import PdfFileReader, PdfFileWriter  # pdf文件读写工具
from reportlab.pdfbase import pdfmetrics  # 注册字体
from reportlab.pdfbase.ttfonts import TTFont  # 字体
from reportlab.pdfgen import canvas  # 创建pdf文件
from copy import copy

# 以下先生成pdf格式的水印
pdfmetrics.registerFont(
    TTFont('font_name', 'automation_pdf\pdf_watermark\Latin.ttf'))  # 注册字体

pdf_watermark_file_creater = canvas.Canvas(
    'automation_pdf/pdf_watermark/watermark.pdf')  # 创建空白pdf文件

pdf_watermark_file_creater.setFont('font_name', 80)  # 设置字体，字号
pdf_watermark_file_creater.setFillColorRGB(
    0.9, 0.9, 0.9, 0.5)  # 使用RGB调色设置文字颜色，透明度
pdf_watermark_file_creater.rotate(55)  # 设置旋转角度（角度制）

pdf_watermark_file_creater.drawString(100, 0, 'watermark by python')  # 渲染文字

pdf_watermark_file_creater.save()  # 保存水印文件

# 其实可以直接拿任意pdf页面直接往源文件上糊

pdf_source_reader = PdfFileReader(
    'automation_pdf/pdf_watermark/source.pdf')  # 读取源文件

watermark_page = PdfFileReader(
    'automation_pdf/pdf_watermark/watermark.pdf').getPage(0)  # 读取水印文件，并直接提取出页面

pdf_result_writer = PdfFileWriter()  # 创建写对象

for index in range(pdf_source_reader.getNumPages()):
    page = copy(watermark_page)
    page.mergePage(pdf_source_reader.getPage(index))  # 合并两页面
    # 欲源文件在下而水印在上则创建水印文件时需要生成多个页面，同时这里将源文件逐页面页叠加在水印文件上
    # 注意，现在程序生成的文件已经是水印在下源文件在上了，这里使用的是copy()方法，相当于在另一个地址制作一个拷贝
    pdf_result_writer.addPage(page)  # 将合并出的页面写入文件

pdf_result_writer.write(
    open('automation_pdf/pdf_watermark/result.pdf', 'wb'))  # 保存结果文件
