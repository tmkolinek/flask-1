from unittest import TestCase
from main import app

class testCases(TestCase):
    def test_conversion(self):
        with app.test_client as client:
            res = client.post('/currencyConversion', data= {'from': 'USD', 'to': 'USD', 'amount': 1})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>The result is $ 1</h1>', html)
            self.assertEqual(res.data['from'], 'USD')
            self.assertEqual(res.data['to'], 'USD')
            self.assertIsInstance(res.data['amount'], float)
            