"""
Example
For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].
Here are the number of times each digit appears in the array:
0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
The most number of times any number occurs in the array is 2,
and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].
"""

class DigitFrequency:
    def __init__(self):
        self.my_list = []
        self.digit_list = []
        self.my_dict = {}

    def _get_data(self) -> None:
        input_string = input('Enter elements of a list separated by comma: ')
        user_list = input_string.split(', ')
        for i in user_list:
            self.my_list.append(int(i))

    def _get_digits(self) -> None:
        for i in self.my_list:
            b = list(str(i))
            self.digit_list.append(b)

    def _flatten(self) -> None:
        self.digit_list = [item for sublist in self.digit_list for item in sublist]

    def _get_digit_frequency(self) -> None:
        for digit in self.digit_list:
            if digit not in self.my_dict:
                self.my_dict[digit] = 1
            else:
                self.my_dict[digit] += 1

    def _get_max_keys(self) -> None:
        highest = max(self.my_dict.values())
        print([int(k) for k, v in self.my_dict.items() if v == highest])

    def _process(self) -> None:
        self._get_digits()
        self._flatten()
        self._get_digit_frequency()
        self._get_max_keys()

    def __call__(self, *args, **kwargs):
        self._get_data()
        self._process()


if __name__ == '__main__':
    frequency = DigitFrequency()
    frequency()
