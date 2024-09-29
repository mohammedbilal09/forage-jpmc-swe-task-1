import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'top_bid': {'price': 117.87, 'size': 81}, 'stock': 'DEF'}
        ]
        
        # Expected outputs
        expected_results = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        
        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual((stock, bid_price, ask_price, price), expected_results[i])

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'top_bid': {'price': 117.87, 'size': 81}, 'stock': 'DEF'}
        ]
        
        # Expected outputs
        expected_results = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
        ]
        
        for i, quote in enumerate(quotes):
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual((stock, bid_price, ask_price, price), expected_results[i])

    def test_getRatio(self):
        self.assertEqual(getRatio(100, 50), 2)
        self.assertEqual(getRatio(50, 100), 0.5)
        self.assertEqual(getRatio(0, 100), 0)
        self.assertEqual(getRatio(100, 0), float('inf')) # Test division by zero

if __name__ == '__main__':
    unittest.main()
