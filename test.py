import unittest
from dict2 import HashTable

class unit_test(unittest.TestCase):
    
    dictn = HashTable()
    def test_a(self):
        self.dictn['a']=99
        self.dictn['c'] =34
        result = self.dictn['a']
        self.assertEqual(result,99)

    def test_g(self):
        with self.assertRaises(KeyError):
            self.dictn['b']
    
    def test_b(self):
        l1 = [el for el in self.dictn] 
        l2 =[('a', 99),('c',34)]
        for x in l2:
            self.assertIn(x ,l1)

if __name__ == '__main__':
    unittest.main()
        
