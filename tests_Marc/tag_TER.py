import re
import treetaggerwrapper

tagger = treetaggerwrapper.TreeTagger(TAGLANG="fr") ## appelle classe TreeTagger

tweet_count = 0
word_count = 0
nom_fichier = "test_TER" ## nom du fichier à traiter sans l'extension ".txt"
## regex_bruit = "@\w+:*|RT|https:.+|([0-9]+h[0-9]*)|[\^\{\}\[\]#=@\*\<\>]"

with open("fichiers_bruts/" + nom_fichier + ".txt", "r", encoding='UTF8') as infile: ## ouverture en UTF8 du fichier en ENTREE
    with open("fichiers_traites/" + nom_fichier + "_TRAITE.txt", "a+", encoding='UTF8') as outfile: ## ouverture en UTF8 du fichier en SORTIE
        for line in infile: ## pour chaque ligne du fichier en ENTREE (fonctionnement inStream-outStream)
            tags = tagger.tag_text(line) ## tag les mots du tweet
            for tag in tags:
                outfile.write(tag + '\n') ## écrit le mot + ses tags dans le fichier en SORTIE
                word_count += 1

print("{}{}".format("Tweets : ", tweet_count))
print("{}{}".format("Mots : ", word_count))
