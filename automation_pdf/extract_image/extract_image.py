import os
import re
import fitz

# 还有一点处理不好，就是非图片的内容会在 terminal 输出一堆 mupdf: not an image，但是我今天实在是不想再去改了😒


def extract_image(pdf_file_path):
    pdf_file = fitz.open(pdf_file_path)

    images_directory_path = pdf_file_path[:-pdf_file_path[::-1].find(
        '/')]+'images_from_'+pdf_file_path[-pdf_file_path[::-1].find('/'):].replace('.', '_')

    # 下面的分支：如果存在对应的文件夹，则直接存入；否则先创建
    image_count = 1
    if os.path.exists(images_directory_path):
        for index in range(1, pdf_file.xref_length()-1):
            pix = pdf_file.extract_image(index)
            if isinstance(pix, dict):
                with open(images_directory_path+'/image_'+str(image_count)+'.'+pix['ext'], 'wb') as image_out:
                    image_out.write(pix["image"])
                image_count += 1
    else:
        os.mkdir(images_directory_path)
        for index in range(1, pdf_file.xref_length()-1):
            pix = pdf_file.extract_image(index)
            if isinstance(pix, dict):
                with open(images_directory_path+'/image_'+str(image_count)+'.'+pix['ext'], 'wb') as image_out:
                    image_out.write(pix["image"])
                image_count += 1


if __name__ == '__main__':
    pdf_file_path = ''

    extract_image(pdf_file_path)
