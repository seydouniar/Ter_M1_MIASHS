
def remove_all(seq, value):
    pos = 0
    for item in seq:
        if item != value:
           seq[pos] = item
           pos += 1
    del seq[pos:]
def clean_phrase(corpus):
    corpus = corpus.split('.')
    corpus_clened=[]
    for ph in corpus:
        ph= ph.replace(u'\ufeff', '')
        ph= ph.replace(u'\n', '')
        ph= ph.replace(u'\n\n', '')
        ph= ph.replace(u'\n\n\n', '')
        ph= ph.replace(u'\xa0', '')
        ph= ph.replace(u'\'', "'")
        corpus_clened.append(ph)
    return corpus_clened
