import unittest
import itemSet_TreeTag as itm
import fonctions as fct
import resultImport


class Test_module(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module "projet"""
    def setUp(self):
        """initialisation des tests."""
        self.text_tag = "c'est un texte en français."
        self.patern = "g:PRO:PER,m:est,g:ADV"
        self.patern = self.patern.split(',')
        self.morceau = [('il', 'il', 'PRO:PER'),
                        ('est', 'être', 'VER:pres'),
                        ('assez', 'assez', 'ADV'),
                        ('difficile', 'difficile', 'ADJ'),
                        ("d'", 'de', 'PRP'),
                        ('ajouter', 'ajouter', 'VER:infi'),
                        ('des', 'du', 'PRP:det'),
                        ('lignes', 'ligne', 'NOM'),
                        ('concernant', 'concerner', 'VER:ppre'),
                        ('2001', '@card@', 'NUM'),
                        (',', ',', 'PUN'), ("l'", 'le', 'DET:ART'),
                        ('Odyssée', 'Odyssée', 'NAM'),
                        ('de', 'de', 'PRP'),
                        ("l'", 'le', 'DET:ART'),
                        ('espace', 'espace', 'NOM')]
        self.a=5
        self.corpus = resultImport.result_item_set

    def test_item_etiquete(self):
        """test des etiquettes de la fonction itemSet_treetagger"""

        l=itm.extract_etq(self.text_tag)
        self.assertEqual(l[0][0][2],'PRO:DEM')
        self.assertEqual(l[0][1][2],'VER:pres')
        self.assertEqual(l[0][2][2],'DET:ART')
        self.assertEqual(l[0][3][2],'NOM')
        self.assertEqual(l[0][4][2],'PRP')
        self.assertEqual(l[0][5][2],'ADJ')
        self.assertEqual(l[0][6][2],'SENT')
        #test lemme
        self.assertEqual(l[0][0][1],'ce')
        self.assertEqual(l[0][1][1],'être')
        self.assertNotEqual(l[0][1][1],'est')
        self.assertEqual(l[0][2][1],'un')
        self.assertEqual(l[0][3][1],'texte')
        self.assertEqual(l[0][4][1],'en')
        self.assertEqual(l[0][5][1],'français')
        self.assertEqual(l[0][6][1],'.')

    def test_type(self):

        """Test typage de pattern """
        l=['m','l','g']

        self.assertIn('m',l)
        self.assertIn('l',l)
        self.assertIn('g',l)
        self.assertNotIn('p',l)

    def test_possiblement_correct(self):
        """test de la fonction possibilté recherche correct"""

        self.assertEqual(fct.possiblement_correct(self.morceau,self.patern),
                         (True, [('il', 'il', 'PRO:PER'), ('est', 'être', 'VER:pres'),
                                 ('assez', 'assez', 'ADV')]))

    def test_recherche_phrase(self):
        """test de la fonction recherche phrase"""

        self.assertEqual(fct.recherche_phrase(self.morceau,self.patern),[('il', 'il', 'PRO:PER'),
                                                                         ('est', 'être', 'VER:pres'),
                                                                         ('assez', 'assez', 'ADV')])
    def test_recherche_corpus(self):
        """Test de la fnction recherche corpus"""

        a = [0, [('il', 'il', 'PRO:PER'), ('est', 'être', 'VER:pres'), ('assez', 'assez', 'ADV')],
             1, [('il', 'il', 'PRO:PER'), ('est', 'être', 'VER:pres'), ('assez', 'assez', 'ADV')]]
        self.assertEqual(fct.recherche_corpus(self.corpus,self.patern),a)
    def test_pattern_research(self):
        """Test de la fonction de recherche pattern"""
        
        a = [0, [('il', 'il', 'PRO:PER'), ('est', 'être', 'VER:pres'), ('assez', 'assez', 'ADV')],
             1, [('il', 'il', 'PRO:PER'), ('est', 'être', 'VER:pres'), ('assez', 'assez', 'ADV')]]
        self.assertEqual(a,fct.pattern_research(self.corpus,"g:PRO:PER,m:est,g:ADV"))

if __name__=="__main__":
    unittest.main()



