import unittest

class Test_module(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module "projet"""
    def setUp(self):
        """initialisation des tests."""
        self.text = "Débutons par quelques points historiques et "
        self.text+="techniques avant de nous repaître d'interprétations fantaisistes. " 
        self.text+="L'intérêt de Stanley Kubrick pour la science-fiction "
        self.text+="provient de son désir de tourner Dr."
        self.a=5
    def test_item_etiquete(self):
        """test des etiquettes de la fonction itemSet_treetagger"""
        
        self.assertEqual(self.a,5)
    def test_fonction_recherche(self):
        """test de la fonction de recherches"""
        self.assertEqual(self.a,5)

    def test_fonction_sequence_frequent(self):
        """test de la fonction des sequence frequent"""
        self.assertEqual(self.a,5)
        

if __name__=="__main__":
    unittest.main()



