import xml.etree.ElementTree as ET

tree = ET.parse('./NU6-107.musicxml')
root = tree.getroot()

n=0
chord_seq=[]
for node in root.iter():
    if(node.tag == 'root-step' or node.tag == "kind" or node.tag == "root-alter"):
        if node.text == "major" or node.text == "suspended-fourth" \
            or node.text == "augmented" or node.text == "dominant-ninth":
            continue
        elif node.text == "minor":
            chord_seq[-1] = chord_seq[-1] + "m"
        elif node.text == "dominant":
            chord_seq[-1] = chord_seq[-1] + "7"
        elif node.text == "major-seventh":
            chord_seq[-1] = chord_seq[-1] + "7"
        elif node.text == "minor-seventh":
            chord_seq[-1] = chord_seq[-1] + "7"
        elif node.text == "half-diminished":
            chord_seq[-1] = chord_seq[-1] + "7"
        elif node.text == "1":
            chord_seq[-1] = chord_seq[-1] + "#"
        elif node.text == "-1":
            chord_seq[-1] = chord_seq[-1] + "b"
        else:
            chord_seq.append(node.text)
            n=n+1
            
print(n)
print(chord_seq)

def find_pattern(seq, pattern):
    n_find=0
    n_p=len(pattern)
    for n in range(len(seq) - n_p + 1):
        if pattern == seq[n:n + n_p]:
            n_find=n_find+1
    return n_find

patterns= [["C","F","G"],
           ["F","G7","Em","Am"],
           ["Am","F","G","C"],
           ["Am","Dm","G","Am"],
           ["C","Am","F","G7"],
           ["F","G","Am","Am"],
           ["C","Am","Dm","G7"],
           ["Am","Em","F","G7"],
           ["C","G","Am","Em","F","C","F","G"]]

for pattern in patterns:
    result=find_pattern(chord_seq,pattern)
    print(pattern,result)
