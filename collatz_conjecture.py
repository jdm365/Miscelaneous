import time
import numpy as np
import sys

class Collatz:
    def __init__(self, limit=1e6):
        self.mem_dict = {1: 0}
        self.count = 0
        self.overall_count = 2
        self.limit = limit

    def iter_num(self, num):
        if num % 2 == 0:
            self.count += 1
            return num // 2
        self.count += 2
        return (3*num + 1) // 2

    def add_num(self):
        done = False
        num = self.overall_count
        while not done:
            val = self.mem_dict.get(num)
            if val is not None:
                self.mem_dict[self.overall_count] = self.count + val
                self.overall_count += 1
                done = True
            else:
                num = self.iter_num(num)
                self.mem_dict[self.overall_count] = self.count
        self.count = 0
        
    def execute(self):
        while self.overall_count < self.limit:
            self.add_num()
        return self.mem_dict

if __name__ == '__main__':
    tree = Collatz(limit=1e6)
    initial = time.time()
    final_tree = tree.execute()
    print(f'Tree size: {np.round(sys.getsizeof(final_tree) // 1e6, 2)} MB')
    print(f'Time taken: {np.round(time.time() - initial, 2)} seconds')
    print(f'Max value: (Number: {max(final_tree, key=final_tree.get)}, Steps: {max(final_tree.values())})')
    while True:
        x = input('Enter number: ')
        if not x.isnumeric():
            print(f'Wrong type! Please type integer between 1 and {int(tree.limit)}')
            continue
        x = int(x)
        if x > tree.limit:
            print(f'Number too large! Please type integer between 1 and {int(tree.limit)}')
            continue
        print(final_tree[x])
