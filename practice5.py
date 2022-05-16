"""
reduce function example
[
{'id':'4', 'name': 'fatemeh'},
{'id':'7', 'name': 'mahtab'},
]
result:
{
{'4':{'id':4, 'name': 'fatemeh'},},
{'7':{'id':7, 'name': 'mahtab'},},
}
"""
from functools import reduce


class ListToDictById:
    def __init__(self):
        self.user_count = 0
        self.user_list = []

    # def _get_user_count(self):
    #     user_count = int(input('Enter the number of users: '))
    #     self.user_count = user_count
    #
    # def _get_data(self):
    #     counter = 0
    #     for user in range(self.user_count):
    #         counter += 1
    #         user_id = input(f'Enter user {counter} id : ')
    #         user_name = input(f'Enter user {counter} name : ')
    #         self.user_dict['id'] = user_id
    #         self.user_dict['name'] = user_name
    #
    # def _get_user_list(self):
    #     self.user_list.append(self.user_dict)
    #     print(self.user_list)]

    def _process(self):
        def reduceFunction(initialDictionary, user_dict: dict) -> dict:
            initialDictionary[user_dict.get('id')] = user_dict
            return initialDictionary
        print(reduce(reduceFunction, [{'id':'4', 'name': 'fatemeh'}, {'id':'7', 'name': 'mahtab'}], {}))

    def __call__(self, *args, **kwargs):
        self._process()


if __name__ == "__main__":
    list_to_dict_by_id = ListToDictById()
    list_to_dict_by_id()
