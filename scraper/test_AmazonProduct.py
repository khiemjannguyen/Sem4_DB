import unittest
from AmazonProduct import *

class Test_AmazonProduct(unittest.TestCase):
    url1 = "https://www.amazon.de/Samsung-MU-PA1T0B-EU-Portable-Kabel/dp/B074M774TW/?_encoding=UTF8&pd_rd_w=l7mCN&pf_rd_p=4f36a2ac-16fe-4a2a-a875-9a9ac12f9041&pf_rd_r=GXM3CM87QAX521QKM1WH&pd_rd_r=ce39a955-9f89-4159-88b2-278a4df7de77&pd_rd_wg=mn7D7&ref_=pd_gw_ci_mcx_mr_hp_d"
    url2 = "https://www.ebay.de/itm/324203357789?epid=25032156863&hash=item4b7c06a65d:g:0OoAAOSwnv9e7HXe"
    product_correct = AmazonProduct(url1)
    product_error = AmazonProduct(url2)

    def test_set_title(self):
        self.assertEqual(self.product_correct.title, "Samsung MU-PA1T0B/EU Portable SSD T5 1 TB USB 3.1 Externe SSD Schwarz")
        self.assertEqual(self.product_error.set_title(), None)

    def test_set_product_id(self):
        self.assertEqual(self.product_correct.product_id, "B074M774TW")
        self.assertEqual(self.product_error.set_product_id(), None)

    def test_get_price(self):
        # not constant: self.assertEqual(self.product_correct.get_price(), None)
        self.assertEqual(self.product_error.get_price(), None)

    def test_get_currency(self):
        self.assertEqual(self.product_correct.get_currency(), "€")
        self.assertEqual(self.product_error.get_currency(), None)

    def test_get_review_starsRate(self):
        # not constant: self.assertEqual(self.product_correct.get_review_starsRate(), None)
        self.assertEqual(self.product_error.get_review_starsRate(), None)

    def test_get_numberOfReviews(self):
        # not constant: self.assertEqual(self.product_correct.get_numberOfReviews(), None)
        self.assertEqual(self.product_error.get_numberOfReviews(), None)

if __name__ == '__main__':
    unittest.main()
