python automation: pdf

记录了一些比较容易实现的 pdf 自动化操作

对哔哩哔哩的孙兴华老师表示感谢，因为大部分操作都是从他的视频中学到的。

# 功能
添加/解除密码

提取表格/图片/文字

合并/拆分

制作并添加水印

页面倒序

页面旋转

# 相关库
fitz: https://github.com/pymupdf/PyMuPDF

os

pandas as pd: https://pandas.pydata.org/

pdfplumber: https://github.com/jsvine/pdfplumber

PyPDF2: https://pythonhosted.org/PyPDF2/

re

reportlab: https://www.reportlab.com/dev/docs/

字体：Windows系统预装的 ARLRDBD.TTF （实际上是我随便选的一个）

# 我参考的资料

main: https://www.bilibili.com/video/BV1YK411n7od

水印的制作与添加：https://www.bilibili.com/video/BV1w7411f76u

# 我使用的测试文件

'automation_pdf\extract_form\form1.pdf' 是孙兴华老师的，因为我实在没有仅含表格的pdf文件

其他的文件是我自己之前写的笔记

# 其他
这里想说一下pdf图片的提取，孙兴华老师的视频是2020年6月发布的，我在2021年8月已经无法使用，因为所引用的库已经发生了较大的变化，尽管对 python 语言研究的并不深入，我只好硬着头皮去一点一点查官方文档。值得兴奋的是，我从官方文档中，以至于从这件事中学到了很多。但是值得思考的是，技术不断积累的今天，若某个工具不时就有如此的巨大变化，这种更新又何尝不是一件事倍功半而吃力不讨好的事情？（也可能就是我太菜了🙄（逃