import unittest
from main import has_no_reg_dates, load_data, count_no_reg_dates, \
                 has_less_than_5_percent_null, calculate_null_percentage

class TestData(unittest.TestCase):

    def setUp(self):
         self.df_no_reg_dates = load_data('data/test_data/test_data_no_reg_every_day.csv')
         self.df_reg_every_day = load_data('data/test_data/test_data_reg_every_day.csv')
         self.df_no_null_country = load_data('data/test_data/test_data_no_null_country.csv')
         self.df_null_country = load_data('data/test_data/test_data_null_countries.csv')

    def test_no_reg_dates(self):
        self.assertTrue(has_no_reg_dates(self.df_no_reg_dates))
        self.assertEqual(count_no_reg_dates(self.df_no_reg_dates), 2)


    def test_reg_every_day(self):
        self.assertFalse(has_no_reg_dates(self.df_reg_every_day))
        self.assertEqual(count_no_reg_dates(self.df_reg_every_day), 0)

    def test_no_null_country(self):
        self.assertTrue(has_less_than_5_percent_null(self.df_no_null_country, 'country'))

    def test_null_country(self):
        self.assertFalse(has_less_than_5_percent_null(self.df_null_country, 'country'))
    
    def test_calculate_null_percentage(self):
        self.assertAlmostEqual(calculate_null_percentage(self.df_no_null_country, 'country'), 0.0, places=2)
        self.assertAlmostEqual(calculate_null_percentage(self.df_null_country, 'country'), 20.0, places=2)

if __name__ == '__main__':
    unittest.main()
