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
            dict(number=98741, superdigit=2),
            dict(number=-10, superdigit=-1),
            dict(number=-99, superdigit=-9),
            dict(number=-999, superdigit=-9),
            dict(number=-88, superdigit=-7),
            dict(number=-532, superdigit=-1),
            dict(number=-4567, superdigit=-4),
            dict(number=-98741, superdigit=-2),
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


class _DigitizingIteratorTest(unittest.TestCase):

    def test_for_given_positive_number_return_digits_as_were_predigitized(self):
        # given positive numbers
        positive_numbers = [0, 1, 100, 200, 1212312, 43543512, 123123, 4345435, 12312312, 34435435, 9234748753, sys.maxint]

        for number in positive_numbers:
            self._for_a_given_positive_number_returns_its_digit(number=number)

    def test_negative_numbers_are_digitized_with_negative_digits(self):
        # given negative numbers
        negative_numbers = [-1, -100, -200, -1212312, -43543512, -123123, -4345435, -12312312, -34435435, -12397654512, -sys.maxint]

        for number in negative_numbers:
            self._for_a_given_negative_number_returns_its_digit(number=number)

    def _for_a_given_positive_number_returns_its_digit(self, number):
        # when the given number is digitized
        digitized = list(superdigit._DigitizingIterator(number=number))

        # then the number is digitized the same as in text made from the number
        digits_from_number = list(itertools.imap(
            lambda str_digit: int(str_digit),
            str(number),
        ))
        self.assertItemsEqual(digits_from_number, digitized, 'Expected number: %s, was: %r' % (digits_from_number, digitized))

    def _for_a_given_negative_number_returns_its_digit(self, number):
        # when the given number is digitized
        digitized = list(superdigit._DigitizingIterator(number=number))

        # then the number is digitized with a negative digits
        digits_from_number = list(itertools.imap(
            lambda str_digit: -int(str_digit),
            str(-number),
        ))
        self.assertItemsEqual(digits_from_number, digitized, 'Expected number: %s, was: %r' % (digits_from_number, digitized))
