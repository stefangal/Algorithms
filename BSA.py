import matplotlib.pyplot as plt
import timeit

class BS:

    def __init__(self):
        self.cycle = 0
        self.data = []
        self.counter = 0

    def get_list(self, start):
        self.cycle += start+1
        self.cycle += 2
        self.data = [*range(start, self.cycle)]
        self.target = self.data[-1]
        return self.data

    def get_target(self):
        return self.target

def BinarySearch(lst, targ):
    low = lst[0]
    high = lst[-1]
    mid = len(lst)//2

    if low > high:
        return False
    if targ == lst[mid]:
        return True
    elif targ < lst[mid]:
        return BinarySearch(lst[:mid-1], targ)
    elif targ > lst[mid]:
        return BinarySearch(lst[mid+1:], targ)


if __name__ == "__main__":
    bs = BS()
    X, Y = [], []

    for start in range(10,800):
        st, end, time = 0,0,0

        data = bs.get_list(start)
        target = bs.get_target()

        st = timeit.default_timer()
        BinarySearch(data, target)
        end = timeit.default_timer()
        tm = (end-st) *1000000
        plt.scatter(len(data), tm)
        plt.pause(0.005)
    plt.show()
