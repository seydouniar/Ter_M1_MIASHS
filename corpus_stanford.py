from pymining import itemmining
import itemSet_TreeTag as itm
from pymining import seqmining
def get_seqence(corpus):
    report = seqmining.freq_seq_enum(corpus, 1)

    return sorted(report)






