from src.utils.PreProcessamento import PreProcessamento
import pandas as pd
import os

pp = PreProcessamento()


fname = '..\\Dataset\\assin-ptpt-train.xml'

arquivo = pp.lerXMLEspecial(fname)

print(arquivo)

#print(arquivo)

teste = ["pau", "no", "seu", "cu", "seu", "arrombado", "de","merda","babacão","do", "caralho"]


