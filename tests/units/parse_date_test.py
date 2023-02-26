import unittest

from src.date import Date
from src.parse_date import parse_date


class ParseDate(unittest.TestCase):

    def test__parse_date(self):

        def return_good_date_when_year_month_day_noise():
            dates = [
                "a_-./;,ab_-20220226a_-./;,ab_-",
                "a_-./;,ab_-2022.02.26a_-./;,ab_-",
                "a_-./;,ab_-2022-02-26a_-./;,ab_-",
                "a_-./;,ab_-2022_02_26a_-./;,ab_-",
                "a_-./;,ab_-2022/02/26a_-./;,ab_-",

                "a_-./;,ab_-26022022a_-./;,ab_-",
                "a_-./;,ab_-26.02.2022a_-./;,ab_-",
                "a_-./;,ab_-26-02-2022a_-./;,ab_-",
                "a_-./;,ab_-26_02_2022a_-./;,ab_-",
                "a_-./;,ab_-26/02/2022a_-./;,ab_-",
            ]

            for date in dates:
                self.assertEqual(parse_date(date), Date(2022, 2, 26))

        def return_good_date_when_year_month_noise():
            dates = [
                "a_-./;,ab_-202202a_-./;,ab_-",
                "a_-./;,ab_-2022.02a_-./;,ab_-",
                "a_-./;,ab_-2022-02a_-./;,ab_-",
                "a_-./;,ab_-2022_02a_-./;,ab_-",
                "a_-./;,ab_-2022/02a_-./;,ab_-",

                "a_-./;,ab_-022022a_-./;,ab_-",
                "a_-./;,ab_-02.2022a_-./;,ab_-",
                "a_-./;,ab_-02-2022a_-./;,ab_-",
                "a_-./;,ab_-02_2022a_-./;,ab_-",
                "a_-./;,ab_-02/2022a_-./;,ab_-",
            ]
            for date in dates:
                self.assertEqual(parse_date(date), Date(2022, 2))

        def return_good_date_when_decis():
            dates = [
                "a_-./;,ab_-202202262359599a_-./;,ab_-",
                "a_-./;,ab_-2022.02.26.23.59.59.9a_-./;,ab_-",

                "a_-./;,ab_-959592326022022a_-./;,ab_-",
                "a_-./;,ab_-9.59.59.23.26.02.2022a_-./;,ab_-",
            ]

            for date in dates:
                self.assertEqual(parse_date(date), Date(2022, 2, 26,
                                                        23, 59, 59, 9))

        def return_good_date_when_centis():
            dates = [
                "a_-./;,ab_-2022022623595999a_-./;,ab_-",
                "a_-./;,ab_-2022.02.26.23.59.59.9.9a_-./;,ab_-",

                "a_-./;,ab_-9959592326022022a_-./;,ab_-",
                "a_-./;,ab_-9.9.59.59.23.26.02.2022a_-./;,ab_-",
            ]

            for date in dates:
                self.assertEqual(parse_date(date), Date(2022, 2, 26,
                                                        23, 59, 59, 9, 9))

        def return_good_date_when_millis():
            dates = [
                "a_-./;,ab_-20220226235959999a_-./;,ab_-",
                "a_-./;,ab_-2022.02.26.23.59.59.9.9.9a_-./;,ab_-",

                "a_-./;,ab_-99959592326022022a_-./;,ab_-",
                "a_-./;,ab_-9.9.9.59.59.23.26.02.2022a_-./;,ab_-",
            ]

            for date in dates:
                self.assertEqual(parse_date(date), Date(2022, 2, 26,
                                                        23, 59, 59, 9, 9, 9))

        def return_good_date_when_micros():
            dates = [
                "a_-./;,ab_-20220226235959999999a_-./;,ab_-",
                "a_-./;,ab_-2022.02.26.23.59.59.999999a_-./;,ab_-",

                "a_-./;,ab_-99999959592326022022a_-./;,ab_-",
                "a_-./;,ab_-999999.59.59.23.26.02.2022a_-./;,ab_-",
            ]

            for date in dates:
                self.assertEqual(parse_date(date), Date(2022, 2, 26, 23, 59,
                                                        59, 9, 9, 9, 9, 9, 9))

        return_good_date_when_year_month_day_noise()
        return_good_date_when_year_month_noise()
        return_good_date_when_decis()
        return_good_date_when_centis()
        return_good_date_when_millis()
        return_good_date_when_micros()
