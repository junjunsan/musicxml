import xml.etree.ElementTree as ET

tree=ET.parse('./9-008ab_n_C.musicxml')
root=tree.getroot()
for node in root.iter():
    if(node.tag=="text"):
         print(node.tag,node.attrib,node.text)
        