import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch
from PIL import Image as PILImage
from os.path import exists
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def create_pdf(filename, product_name, size, pack, retail_upc, expire_date, quantity, product_image):
    # Create PDF document
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create content list
    story = []
    
    # Add product image
    img = PILImage.open(product_image)
    img.thumbnail((200, 200))  # Resize image
    img.save("temp.png")  # Save temporary file
    story.append(Image("temp.png", width=2*inch, height=2*inch))
    story.append(Spacer(1, 12))  # Add spacing
    
    # Add product name
    story.append(Paragraph("Product Name: {}".format(product_name), styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Add size
    story.append(Paragraph("Size: {}".format(size), styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Add pack
    story.append(Paragraph("Pack: {}".format(pack), styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Add retail UPC
    story.append(Paragraph("Retail UPC: {}".format(retail_upc), styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Add expire date
    story.append(Paragraph("Expire Date: {}".format(expire_date), styles['BodyText']))
    story.append(Spacer(1, 12))
    
    # Add quantity
    story.append(Paragraph("Quantity: {}".format(quantity), styles['BodyText']))
    
    # Generate PDF
    pdf.build(story)

# 使用文件选择对话框选择图片
Tk().withdraw()  # 隐藏Tkinter主窗口
product_image = askopenfilename(
    title="选择产品图片",
    filetypes=[
        ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),  # 支持多种图片格式
        ("All Files", "*.*")  # 可选：支持所有文件
    ]
)

if not product_image:
    print("未选择图片文件，程序退出。")
else:
    # 用户输入其他信息
    product_name = input("Enter Product Name: ")
    size = input("Enter Size: ")
    pack = input("Enter Pack: ")
    retail_upc = input("Enter Retail UPC: ")
    expire_date = input("Enter Expire Date: ")
    quantity = input("Enter Quantity: ")

    # 生成PDF文件名
    pdf_filename = f"{product_name}.pdf"

    # 生成PDF
    create_pdf(pdf_filename, product_name, size, pack, retail_upc, expire_date, quantity, product_image)
    print(f"PDF '{pdf_filename}' 生成成功！") 