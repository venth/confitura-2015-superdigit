__author__ = 'venth'


def calc(number):

    calculated = reduce(
        lambda current, digit: dict(no = current['no'] + 1, sum=current['sum'] + digit),
        _DigitizingIterator(number=number),
        dict(no=0, sum=0),
    )

    reduced_to_one_digit = calculated['no'] == 1
    if reduced_to_one_digit:
        return calculated['sum']
    else:
        return calc(calculated['sum'])


class _DigitizingIterator(object):
    def __init__(self, number):
        if number < 0:
            self.sign = -1
            self._number = -number
        else:
            self.sign = 1
            self._number = number

    def next(self):
        digit = self._number % 10

        all_digits_extracted = self._number == -1
        if all_digits_extracted:
            raise StopIteration

        self._number /= 10

        need_to_be_stopped = self._number == 0
        if need_to_be_stopped:
            self._number = -1

        return self.sign * digit

    def __iter__(self):
        return self
