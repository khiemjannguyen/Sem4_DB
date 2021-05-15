import unittest
from PriceTracker import *


class Test_PriceTracker(unittest.TestCase):
    url1 = "https://www.amazon.de/Samsung-MU-PA1T0B-EU-Portable-Kabel/dp/B074M774TW/?_encoding=UTF8&pd_rd_w=l7mCN&pf_rd_p=4f36a2ac-16fe-4a2a-a875-9a9ac12f9041&pf_rd_r=GXM3CM87QAX521QKM1WH&pd_rd_r=ce39a955-9f89-4159-88b2-278a4df7de77&pd_rd_wg=mn7D7&ref_=pd_gw_ci_mcx_mr_hp_d"
    product = AmazonProduct(url1)
    wish_price = 90.00
    notify_email = "yourfriendlyscraper@gmail.com"
    openInfluxDB_GUI = True
    priceTracker = PriceTracker(amazon_product=product, wish_price=wish_price,
                      notify_email=notify_email, openInfluxDB_GUI=openInfluxDB_GUI)

    def test_check_wish_price_satisfied(self):
        self.assertTrue(self.priceTracker.check_wish_price_satisfied(90.00))
        self.assertFalse(self.priceTracker.check_wish_price_satisfied(200.00))

    def test_notify_consumer(self):
        self.priceTracker.__notify_email = "fail@fail.fail"
        self.assertEqual(self.priceTracker.notify_consumer(), None)



if __name__ == '__main__':
    unittest.main()
