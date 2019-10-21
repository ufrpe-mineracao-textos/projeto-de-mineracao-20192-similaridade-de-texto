import xml.etree.ElementTree as ET
import sklearn.metrics.pairwise as pw
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import requests


class PreProcessamento:

    #LER ARQUIVOS
    def lerXMLEspecial(self, fname):
        print(fname)
        tree = ET.parse(fname)
        root = tree.getroot()

        print(root)
        print(root.attrib)
        filtro = "*"
        for node in root:
            print(node)
            #s_pair = node.attrib.get("pair")
            #s_entailment = node.nodeValue
            #print("entailment", s_pair)


    def lerArquivo(self, fname):
        f = open(fname, encoding="utf8")
        f.close()

    #VETORIZAÇÃO
    def vetorizar(self, file):
        tf = TfidfVectorizer()
        X = tf.fit_transform(file)
        print(tf.get_feature_names())
        print(X.shape)
        return X.shape

    #WORD EMBEDDING
    def coseno(self, x):
        coseno = pw.cosine_distances(x)
        print(coseno)