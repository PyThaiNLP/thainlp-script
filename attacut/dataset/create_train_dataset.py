"""
Build dataset for attacut
write by Wannaphong Phatthiyaphaibun

V 0.2
23/10/2020
"""
import json
from pythainlp.tokenize import syllable_tokenize
def load_file(path):
    with open(path, "r", encoding= "utf-8-sig") as f:
        return f.read()
def load_dataset_txt(path):
    with open(path, "r", encoding= "utf-8-sig") as f:
        return [i.strip() for i in f.readlines()]
syll =json.loads(load_file("syllables.json"))
char =json.loads(load_file("characters.json"))

def check_char(c):
    if c not in list(char.keys()):
        return 1
    else:
        return char[c]

def check_syll(c):
    if c not in list(syll.keys()):
        return 1
    else:
        return syll[c]

def build(sent):
    if sent.endswith('|') == False:
        sent+="|"
    list_word = sent.split("|")
    temp_sent=sent.replace('|','')
    list_char = list(temp_sent)
    list_char_idx = [str(check_char(i)) for i in list_char]
    list_cut = ""
    list_syll = []
    list_syll_idx = []
    for i in list_word:
        temp = ""
        for t,j in enumerate(list(i)):
            if t == 0:
                temp+="1"
            else:
                temp+="0"
        list_cut+=temp
        cut_syll=syllable_tokenize(i, engine="ssg")
        for i in cut_syll:
            check=str(check_syll(i))
            for j in i:
                list_syll_idx.append(check)
        #list_syll.extend()
    #list_syll_idx = [str(check_syll(i)) for i in list_syll]
    r = list_cut+"::"+' '.join(list_char_idx)+"::"+' '.join(list_syll_idx)
    return r

#dataset = [build(i) for i in load_dataset_txt("wisesight-1000-samples-tokenised.label")]
def build_dataset(txt):
    return '\n'.join([build(i) for i in load_dataset_txt(txt)])
