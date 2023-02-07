import config

import spacy
nlp = spacy.load("en_core_web_sm")

import cv2 as cv
import pandas as pd
from lxml import etree
from PIL import Image
import numpy as np
import pickle

from general_utils import parse_annotation


# SPaCY TAGS
# this is from: https://stackoverflow.com/questions/58215855/how-to-get-full-list-of-pos-tag-and-dep-in-spacy
TAG_LIST = np.unique(np.append(['$', "''", ',', '-LRB-', '-RRB-', '.', ':', 'ADD', 'AFX', 'CC',
        'CD', 'DT', 'EX', 'FW', 'HYPH', 'IN', 'JJ', 'JJR', 'JJS', 'LS',
        'MD', 'NFP', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP',
        'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD',
        'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', 'XX', '_SP',
        '``'],[":",".",",","-LRB-","-RRB-","``","\"\"","''",",","$","#","AFX","CC","CD","DT","EX","FW","HYPH","IN","JJ","JJR","JJS","LS","MD","NIL","NN","NNP","NNPS","NNS","PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","SP","SYM","TO","UH","VB","VBD","VBG","VBN","VBP","VBZ","WDT","WP","WP$","WRB","ADD","NFP","GW","XX","BES","HVS","_SP"])).tolist()
POS_LIST = np.unique(np.append(['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM',
        'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SPACE', 'SYM', 'VERB',
        'X'],["ADJ", "ADP", "ADV", "AUX", "CONJ", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X", "SPACE"])).tolist()
DEP_LIST = np.unique(np.append(['ROOT', 'acl', 'acomp', 'advcl', 'advmod', 'agent', 'amod',
        'appos', 'attr', 'aux', 'auxpass', 'case', 'cc', 'ccomp',
        'compound', 'conj', 'csubj', 'csubjpass', 'dative', 'dep', 'det',
        'dobj', 'expl', 'intj', 'mark', 'meta', 'neg', 'nmod', 'npadvmod',
        'nsubj', 'nsubjpass', 'nummod', 'oprd', 'parataxis', 'pcomp',
        'pobj', 'poss', 'preconj', 'predet', 'prep', 'prt', 'punct',
        'quantmod', 'relcl', 'xcomp'],["ROOT", "acl", "acomp", "advcl", "advmod", "agent", "amod", "appos", "attr", "aux", "auxpass", "case", "cc", "ccomp", "compound", "conj", "cop", "csubj", "csubjpass", "dative", "dep", "det", "dobj", "expl", "intj", "mark", "meta", "neg", "nn", "npmod", "nsubj", "nsubjpass", "oprd", "obj", "obl", "pcomp", "pobj", "poss", "preconj", "prep", "prt", "punct",  "quantmod", "relcl", "root", "xcomp", "nummod"])).tolist()

# options for angles
angles = np.array([0, 90, 180, 270]) #options
steps = round(256./len(angles))


    
    
