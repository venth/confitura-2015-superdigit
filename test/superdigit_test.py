__author__ = 'venth'

import itertools
import sys
import unittest

import superdigit


class SuperdigitTest(unittest.TestCase):

    def test_every_single_digit_has_equal_superdigit(self):
        # given single digits
        single_digits = [digit for digit in xrange(0, 9)]

        # when super digit is calculated for every single digit
        calculated = itertools.imap(
            lambda d: (d, superdigit.calc(d)),
            single_digits,
        )

        # then every single digit is the super digit as well
        for digit, calc_superdigit in calculated:
            self.assertEqual(digit, calc_superdigit)

    def test_every_negative_single_digit_has_equal_negative_superdigit(self):
        # given single digits
        single_digits = [digit for digit in xrange(-9, -1)]

        # when super digit is calculated for every single digit
        calculated = itertools.imap(
            lambda d: (d, superdigit.calc(d)),
            single_digits,
        )

        # then every single digit is the super digit as well
        for digit, calc_superdigit in calculated:
            self.assertEqual(digit, calc_superdigit)

    def test_calculated_superdigit_for_numbers(self):
        # given numbers with pre-calculated super digits
        numbers = [
            dict(number=10, superdigit=1),
            dict(number=99, superdigit=9),
            dict(number=999, superdigit=9),
            dict(number=88, superdigit=7),
            dict(number=532, superdigit=1),
            dict(number=4567, superdigit=4),
            dict(number=-10, superdigit=-1),
            dict(number=-99, superdigit=-9),
            dict(number=-999, superdigit=-9),
            dict(number=-88, superdigit=-7),
            dict(number=-532, superdigit=-1),
            dict(number=-4567, superdigit=-4),
        ]

        # when super digit is calculated for every given number
        calculated = itertools.imap(
            lambda given: (given['superdigit'], superdigit.calc(given['number'])),
            numbers,
        )

        # then calculated superdigit is equal a given calculated by hand
        for given_superdigit, calc_superdigit in calculated:
            self.assertEqual(given_superdigit, calc_superdigit)

    def test_calculate_superdigit_for_max_positive_ends_with_calculated_superdigit(self):
        # when superdigit is calculated for max positive number
        superdigit.calc(sys.maxint)

        # then superdigit is calculated without error
        pass
