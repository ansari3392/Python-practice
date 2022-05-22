"""
reduce function example
"""
from functools import reduce


class SpendSummation:

    def _process(self):
        def reduceFunction(initialValue, user_dict: dict) -> dict:
            initialValue += user_dict.get('spend')
            return initialValue
        print(reduce(reduceFunction, [{'id': '4', 'name': 'fatemeh', 'spend': 80},  {'id': '5', 'name': 'mahtab', 'spend': 100}], 0))

    def __call__(self, *args, **kwargs):
        self._process()


if __name__ == "__main__":
    spend_summation = SpendSummation()
    spend_summation()
