import unittest

from format_price import format_price

class FormatPriceTestCase(unittest.TestCase):
    def test_big_integer_price_with_zero_decimals(self):
        self.assertEqual(format_price('123456.000'), '123 456')
    
    def test_big_integer_price(self):
        self.assertEqual(format_price(987654321), '987 654 321')   
    
    def test_float_price(self):
        self.assertEqual(format_price('10.9876'),'10.99')
        
    def test_float_price_with_many_decimals(self):
        self.assertEqual(format_price(0.09876000), '0.1')
        
    def test_zero_str_price(self):
        self.assertEqual(format_price('0'),'N/A')
        
    def test_zero_int_price(self):
        self.assertEqual(format_price(0), 'N/A')
    
    def test_garbage_price(self):
        self.assertEqual(format_price('smth'),'N/A')
        
    def test_bool_price(self):
        self.assertEqual(format_price(True), 'N/A')
    
    def test_None_price(self):
        self.assertEqual(format_price(None), 'N/A')
        
    
if __name__ == '__main__':
    unittest.main()
