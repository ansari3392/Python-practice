"""
 class should return the count of all numbers except numbers with a 5 in it.
1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
"""
class DontGiveMeFive:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def _process(self) -> None:
        my_list = []
        for i in range(self.start, self.end + 1):
            if '5' not in str(i):
                my_list.append(i)
        n = len(my_list)
        print(n)

    def __call__(self, *args, **kwargs):
        self._process()


if __name__ == '__main__':
    dont_give_me_five = DontGiveMeFive(10, 80)
    dont_give_me_five()


