"""
reduce function example
"""
from functools import reduce


class RemoveDuplicate:

    def _process(self):
        def reduceFunction(initialDictionary, user_dict: dict) -> dict:
            initialDictionary[user_dict.get('id')] = user_dict
            return initialDictionary
        print(reduce(reduceFunction, [{'id':'4', 'name': 'fatemeh'}, {'id':'4', 'name': 'fatemeh'}, {'id':'5', 'name': 'mahtab'}], {}))

    def __call__(self, *args, **kwargs):
        self._process()


if __name__ == "__main__":
    remove_duplicate = RemoveDuplicate()
    remove_duplicate()
