from xml.dom import minidom
import xml.etree.ElementTree as ET
import numpy as np

def downloadSquareFromXML():
    tree = ET.parse('square.xml')
    root = tree.getroot()
    N = 4
    square = np.zeros(N**2, dtype=int)
    for i in range(0, N**2):
        square[i] = int(root.find('a' + str(i)).text)
    square = np.reshape(square, (N, N))
    return N, square

def saveSquareInXml(N, square):
    root = ET.Element('square')
    N = 4
    sq = square.reshape(N**2)
    for i in range(0, N**2): 
        array_elem = ET.SubElement(root, 'a' + str(i))
        array_elem.text = str(sq[i])
    filename = 'square.xml'
    xml_string = ET.tostring(root).decode()

    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'w') as xml_file:
        xml_file.write(xml_prettyxml)
