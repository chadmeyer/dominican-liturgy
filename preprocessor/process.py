# We want to have a thing here which can read in a file,
# read the text lines, and decorate the syllables as needed.
from enum import Flag, auto
def latex_add(s,c):
    return '\\'+c+'{'+s+'}'

def process_flex(l) :
    trimmed_line = l[:-1]
    ns = []
    syllables = []
    # First we "unzip" the line into words and the words into syllables
    for w in trimmed_line :
        ns.append(len(w.split('|')))
        syllables.append(w.split('|'))
    # Check for final accent
    nw = len(trimmed_line)
    found = False
    for i in range( nw - 1, -1, -1) :
        for j in range( ns[i] - 1, -1, -1) :
            #First, check for accent:
            if '^' in syllables[i][j]:
                #We found an accent
                if i == nw - 1 and j == ns[i]-1:
                    # This is really the last syllable
                    syllables[i][j] = latex_add(syllables[i][j],"flexfinalsyllableaccent")
                    if ns[i] > 1 :
                        syllables[i][j-1] = latex_add(syllables[i][j-1],"flexvirtualfinalaccent")
                    else:
                        syllables[i-1][-1] = latex_add(syllables[i-1][-1],"flexvirtualfinalaccent")
                else:
                    syllables[i][j] = latex_add(syllables[i][j], "flexfinalaccent")
                found = True
                break
            else:
                syllables[i][j] = latex_add(syllables[i][j],"flexpostaccent")
        if found : break
    # Now, zip up the string again
    ol = []
    for w in syllables :
        ol.append(''.join(w))
    out = ' '.join(ol)
    out += " \\flexsymbol"
    out = out.replace('^','')
    return out

def process(filename) :
    f = open(filename, "r")
    for line in f:
        words = line.split()
        if len(words) == 0:
            continue
        if words[-1] == '*':
            oline = process_mediant(l)
        elif words[-1] == '+':
            oline = process_flex(l)
        else : 
            oline = process_conclusion(l)
    