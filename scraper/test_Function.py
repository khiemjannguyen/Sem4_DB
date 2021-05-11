import unittest
from Functions import *

class Test_Functions(unittest.TestCase):
    productID_correct = "B074M774TW"
    product = "product"
    productID_ = "Samsung-MU"

    def product_id_legit(self):
        # Test whether function identify legit product_id
        self.assertTrue(product_id_legit(productID_correct))
        self.assertFalse(product_id_legit(product))
        self.assertFalse(product_id_legit(productID_))


if __name__ == '__main__':
    unittest.main()
