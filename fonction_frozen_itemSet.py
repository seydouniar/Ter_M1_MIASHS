from pymining import itemmining
from pymining import seqmining
import codecs
def sequenes_frequents(input_file):
    input_file = codecs.open(input_file,'r','utf-8')
    txt = input_file.read()
    sequences = txt.split('.')
    freq_seq = seqmining.freq_seq_enum(sequences,20)
    print(freq_seq)

sequenes_frequents("Sans_titre.txt")