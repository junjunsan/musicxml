import xml.etree.ElementTree as ET
import pandas as pd
import os

tree=ET.parse(os.path.join(os.getcwd(),"xml",'./9-008ab_n_C.musicxml'))
root=tree.getroot()
rs = ''
ra = ''
kd = ''
bs = ''

data=[]

for node in root.iter():
    if(node.tag=="harmony"):
        rs = ''
        ra = ''
        kd = ''
        bs = ''
    elif(node.tag == 'root-step'):
        rs = node.text
    elif(node.tag == 'root-alter'):
        ra = node.text
    elif(node.tag == 'kind'):
        if 'text' in node.attrib:
            kd = node.attrib['text']
    elif(node.tag == 'bass-step'):
        bs = node.text
    elif(node.tag == 'text'):
        if bs == '':
            print(node.text, rs+ra+kd)
            data.append([node.text, rs+ra+kd])
        else:
            print(node.text, rs+ra+kd+'/'+bs)
            data.append([node.text, rs+ra+kd+"/"+bs])


cdf=pd.DataFrame(data)
cdf.columns=["歌詞","コード"]

cdf.to_csv("./outputCode.csv",encoding="utf_8")
