
import xml.etree.ElementTree as ET

dom=ET.parse('D:\\浙大海宁学习大一\\IBI1\\IBI1_2024-25\\IBI1_2024-25\\Practical14\\go_obo.xml')
dom=dom.getroot()
#go through(traverse) child element
for elem in dom:
    if elem.tag=="term":
        print(elem)
    break