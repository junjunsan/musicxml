

#sekai chord_seq = ["A","D","E","F","A","D","E","F","A","D","E","F","A","D","E","F","A","D","E","D",
#             "A","D","E","C#","F#","D","B","E","E","A","D","E","C#","F#","D","E7","A",
#             "A","D","E","C#","F#","D","B","E","E","A","D","E","C#","F#","D","E7","A",
#             "G","D","G","D","E","E","A","B","E7","Bm7","C#","D","A","D","E","C#",
#             "F#","B7","E7","A","D","E","C#","F#","B7","Bm7","E7","E","A"]

#aog chord_seq = ["D","A7","D","G","C#","D","G","D","Em7","A","D",
#             "A7","D","G","C#","D","D#","Em","D","A7","D",
#             "D7","G","D","G","D","E7","A","A7",
#             "A7","D","A","D","D7","G","G","C#","D","A7","D",
#            "A7","D","G","C#","D","G","D","Em7","A","D",
#             "A7","D","G","C#","D","D#","Em","D","A7","D",
#             "D7","G","D","G","D","E7","A",
#             "A7","D","A","D","D7","G","G","C#","D","A7","D",
#             "Em7","D","D7","G","Em7","A7","D"]
#chord_seq = ["C","G","Am7","F","C","G","Am7","F","G","C",
#             "C","G","Am7","F","C","G","Am7","F","G","C"]
#chord_seq = ["F","Gm","F","C","F","Gm","F","C7","F","C","C","F","Bb","C","F","Gm","F","G7","F"]
# chord_seq = ["Am","Dm","Am","Am","Dm","E7","Am","Am","Dm7","Am","Dm","Dm","Am","Am","Dm","E7","Am"]
# chord_seq = ["C","F","C","F","C","F","C","Dm7","G7","C","G","C","F","C","C","G7","C"]
#chord_seq = ["CM7","G7","CM7","G7","CM7","G7","Dm7","G7","CM7","G7","FM7","Em7","G7",
 #            "CM7","G7","Dm7","G7","CM7"]

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
    if chord.endswith('m7'):
        chord_new = change_fifth_simple(chord[:-2], key)
        chord = chord_new + chord[-2]
    elif chord.endswith('7') or chord.endswith('m'):
        chord_new = change_fifth_simple(chord[:-1], key)
        chord = chord_new + chord[-1]
    
    else:
        chord = change_fifth_simple(chord, key)
    return chord

def transpose(chord_seq, key):
    return [change_fifth(chord, key) for chord in chord_seq]

print(transpose(chord_seq,3))

seq = transpose(chord_seq,3)

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
    result=find_pattern(seq,pattern)
    print(pattern,result)