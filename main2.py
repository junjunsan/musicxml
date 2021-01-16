#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import pathlib

def get_chord_seq(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    #print(root)
    n=0
    chord_seq=[]
    for node in root.iter():
        if(node.tag == "fifths"):
            key = node.text
        if(node.tag == 'root-step' or node.tag == "kind" or node.tag == "root-alter"):
            if node.text == "major" or node.text == "suspended-fourth" \
                or node.text == "augmented" or node.text == "dominant-ninth"\
                or node.text == "major-ninth" or node.text == 'diminished'\
                or node.text == 'major-sixth' or node.text == 'major-minor':
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
            elif node.text == "none":
                continue
            elif node.text == "other":
                continue
            elif node.text == "power":
                continue
            else:
                chord_seq.append(node.text)
                n=n+1
    #print(n)
    return chord_seq, int(key)

def one_up(chord):
    if chord == 'C':
        #print('converting C to G')
        return 'G'
    elif chord == 'G':
        #print('converting G to D')
        return 'D'
    elif chord == 'D':
        #print('converting D to A')
        return 'A'
    elif chord == 'A':
        #print('converting A to E')
        return 'E'
    elif chord == 'E':
        return 'B'
    elif chord == 'B':
        return 'F#'
    elif chord == 'F#':
        return 'C#'
    elif chord == 'C#':
        return 'Ab'
    elif chord == 'Ab':
        return 'Eb'
    elif chord == 'Eb':
        return 'Bb'
    elif chord == 'Bb':
        return 'F'
    elif chord == 'F':
        return 'C'
    elif chord == 'Gb':
        return 'Db'
    elif chord == 'Db':
        return 'Ab'
    elif chord == 'G#':
        return 'Eb'
    
def one_down(chord):
    if chord == 'C':
        return 'F'
    elif chord == 'F':
        return 'Bb'
    elif chord == 'Bb':
        return 'Eb'
    elif chord == 'Eb':
        return 'Ab'
    elif chord == 'Ab':
        return 'Db'
    elif chord == 'Db':
        return 'Gb'
    elif chord == 'Gb':
        return 'B'
    elif chord == 'B':
        return 'E'
    elif chord == 'E':
        return 'A'
    elif chord == 'A':
        return 'D'
    elif chord == 'D':
        return 'G'
    elif chord == 'G':
        return 'C'
    elif chord == 'C#':
        return 'F#'
    elif chord == 'F#':
        return 'B'
    elif chord == 'G#':
        return 'C#'
    elif chord == 'Cb':
        return 'E'
    elif chord == 'D#':
        return 'Ab'
    elif chord == 'A#':
        return 'Eb'

def change_fifth_simple(chord, key): # no minor or 7th code
    if key > 0:
        chord = one_down(chord)
        key = key - 1
        return change_fifth_simple(chord, key)
    elif key < 0:
        chord = one_up(chord)
        key = key + 1
        return change_fifth_simple(chord, key)
    else:
        return chord

def change_fifth(chord, key):
    if chord.endswith('7') or chord.endswith('m'):
        chord_new = change_fifth_simple(chord[:-1], key)
        chord = chord_new + chord[-1]
    else:
        chord = change_fifth_simple(chord, key)
    return chord

def transpose(chord_seq, key):
    return [change_fifth(chord, key) for chord in chord_seq]

def main():
    p = pathlib.WindowsPath('.')
    #p = pathlib.Path('.')
    for tune in p.glob("*.musicxml"):
    #for tune in p.glob("NU7-73.musicxml"):
        print(tune)
        chord_seq, key = get_chord_seq(tune)
        print(chord_seq, key)
        chord_seq = transpose(chord_seq, key)
        print(chord_seq)

if __name__ == '__main__':
    main()
    
'''
n=0
chord_seq=[]
for node in root.iter():
    if(node.tag == 'root-step' or node.tag == "kind" or node.tag == "root-alter" or node.tag == "key"):
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
'''
