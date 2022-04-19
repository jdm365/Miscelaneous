import time
import numpy as np
import sys

class Collatz:
    def __init__(self, treebase_size=1e6):
        self.mem_dict = {1: 0}
        self.count = 0
        self.overall_count = 2
        self.treebase_size = treebase_size

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
        
    def create_treebase(self):
        while self.overall_count < self.treebase_size:
            self.add_num()
    
    def calc_new(self, num):
        done = False
        key = num
        while not done:
            val = self.mem_dict.get(num)
            if val is not None:
                value = self.count + val
                done = True
            else:
                num = self.iter_num(num)
            self.count = 0
        return key, value

    

if __name__ == '__main__':
    tree = Collatz(treebase_size=1e6)
    initial = time.time()
    tree.create_treebase()
    print(f'Time taken: {np.round(time.time() - initial, 2)} seconds')
    while True:
        x = input('Enter number: ')
        if x == '':
            break
        if not x.isnumeric():
            print(f'Wrong type! Please enter integer.')
            continue
        x = int(x)
        key, val = tree.calc_new(x)
        print(f'Number: {key} \nSteps needed: {val}')
