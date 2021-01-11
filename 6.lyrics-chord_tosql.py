import pandas as pd
import re
import os
import MeCab
import xml.etree.ElementTree as ET
import sqlite3

tmpdf = pd.read_csv(os.path.join(os.getcwd(), 'csv', 'lyricsSample.csv'), encoding='utf_8')
wcols = ['通し番号', 'ID', '曲名', 'アーティスト', '作曲', '作詞', '発表年', '巻', '番号', 'XML', 'Wikipediaジャンル', '歌手性別',
'表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活⽤形', '活⽤型', '原形', '読み', '発音']
ccols = ['XML', '歌詞', 'コード']
dbfile = os.path.join(os.getcwd(), 'csv', 'outputLyrics.db')
if os.path.exists(dbfile):
    os.remove(dbfile)
conn = sqlite3.connect(dbfile)

for i in range(len(tmpdf)):
    wcoldatal = []
    wdf = pd.DataFrame(index=[], columns=wcols)
    cdf = pd.DataFrame(index=[], columns=ccols)
    for j in range(len(tmpdf.columns)):
        if j == 9:
            for filename in os.listdir(os.path.join(os.getcwd(), 'xml')):
                if filename.startswith(tmpdf.iat[i, j]) and filename.endswith('musicxml'):
                    tree = ET.parse(os.path.join(os.getcwd(), 'xml', filename))
                    root = tree.getroot()
                    rs = ''
                    ra = ''
                    kd = ''
                    bs = ''
                    for node in root.iter():
                        if(node.tag == 'harmony'):
                            rs = ''
                            ra = ''
                            kd = ''
                            bs = ''
                        elif(node.tag == 'root-step'):
                            rs = node.text
                        elif(node.tag == 'root-alter'):
                            ra = '#'
                        elif(node.tag == 'kind'):
                            if 'text' in node.attrib:
                                kd = node.attrib['text']
                        elif(node.tag == 'bass-step'):
                            bs = node.text
                        elif(node.tag == 'text'):
                            nodeText = list(node.text)
                            for txt in nodeText:
                                data = []
                                if bs == '':
                                    data.append(filename)
                                    data.append(node.text)
                                    data.append(rs+ra+kd)
                                else:
                                    data.append(filename)
                                    data.append(node.text)
                                    data.append(rs+ra+kd)
                                record = pd.Series(data, index=cdf.columns)
                                cdf = cdf.append(record, ignore_index=True)
        if j == 12:
            mark_regex = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]')
            tmp = tmpdf.iat[i, j].replace('　', ' ')
            tmp = ' '.join(tmp.splitlines())
            tmp = mark_regex.sub(' ', tmp)
            tmp = tmp.replace('¥s+', ' ')
            m = MeCab.Tagger("-Ochasen")
            m.parse('')
            node = m.parseToNode(tmp)
           
            while node:
                wcoldatar = []
                word = node.surface
                wclass = node.feature.split(',')
                if word != '':
                    if len(wclass) == 7 or len(wclass) == 9:
                        wcoldatar.append(word)
                        for k in range(len(wclass)):
                            wcoldatar.append(wclass[k])
                        if len(wclass) == 7:
                            wcoldatar.pop()
                            wcoldatar.extend([word, word, word])
                if len(wcoldatar) > 0:
                    wcoldata = []
                    wcoldata.extend(wcoldatal)
                    wcoldata.extend(wcoldatar)
                    record = pd.Series(wcoldata, index=wdf.columns)
                    wdf = wdf.append(record, ignore_index=True)
                node= node.next
        else:
            wcoldatal.append(tmpdf.iat[i,j])
            
    wdf.to_sql("Lyrics",conn,if_exists="append",index=None)
    cdf.to_sql("Code",conn,if_exists="append",index=None)     
conn.close()