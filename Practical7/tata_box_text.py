import re
import sys

try:
    tata_box = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
    # 将文件指针移动到文件开头
    tata_box.seek(0)
    tata_box1 = tata_box.read()
    print(len(tata_box1))
    sys.stdout.flush()
except Exception as e:
    print(f'发生异常：{e}')
finally:
    if 'tata_box' in locals():
        tata_box.close()

encodings = ['utf-8', 'gbk', 'latin1', 'utf-16']
for encoding in encodings:
    try:
        print(f"尝试使用 {encoding} 编码打开文件...")
        with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r", encoding=encoding) as tata_box:
            tata_box.seek(0)
            tata_box1 = tata_box.read()
            print(f"使用 {encoding} 编码读取内容的长度: {len(tata_box1)}")
            if tata_box1:
                print("读取到的部分内容（前 100 个字符）:")
                print(tata_box1[:100])
            sys.stdout.flush()
    except UnicodeDecodeError:
        print(f"使用 {encoding} 编码打开文件时发生解码错误。")
    except Exception as e:
        print(f"使用 {encoding} 编码打开文件时发生异常：{e}")

try:
    with open('D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical7\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("文件未找到")