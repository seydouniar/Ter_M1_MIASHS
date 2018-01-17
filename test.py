import unittest
import itemSet_TreeTag as itm


class Test_module(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module "projet"""
    def setUp(self):
        """initialisation des tests."""
        self.text_tag = "c'est un texte en français."

        self.a=5
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
    def test_fonction_recherche(self):
        """test de la fonction de recherches"""
        self.assertEqual(self.a,5)
    def test_type(self):
        l=['m','l','g']

        self.assertIn('m',l)
        self.assertIn('l',l)
        self.assertIn('g',l)
        self.assertNotIn('p',l)

    def test_possiblement_correct(self):
        self.assertTrue()
    def test_recherche_phrase(self):
        """test de la fonction des sequence frequent"""
        self.assertEqual(self.a,5)
    def test_recherche_corpus(self):
        self.assertEqual(self.a,5)
    def test_pattern_research(self):
        self.assertEqual(self.a,5)

if __name__=="__main__":
    unittest.main()



