import treetaggerwrapper
#from stanfordcorenlp import StanfordCoreNLP
#import treetagger langages fr
tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
#nlp = StanfordCoreNLP(r'/home/seydou/Bureau/TER_DOC/stanford-corenlp-full-2017-06-09/',lang='fr')
#init list word
tous_mots=[]

#extract itemSet function words
def extract_etq(corpus):
    list_phrase=corpus.split(".")
    for phrase in list_phrase:
        phrase+="."
        tag_phrase_tmp = tagger.tag_text(phrase)
        tag_phrase = treetaggerwrapper.make_tags(tag_phrase_tmp)

        #les mot d'une phrase
        mots =[]
        for tag in tag_phrase:
            #tuple item for word
            etq=()
            etq += (tag.word,tag.lemma,tag.pos)
            mots.append(etq)
        tous_mots.append(mots)
        return tous_mots







