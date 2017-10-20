import time
def time_me(funct):
    def f(*args, **kw):
        print(f"running {funct.__name__}({args})")
        t = int(round(time.time() * 1000))
        funct(*args, **kw)
        t2 = int(round(time.time() * 1000))
        print(f"took {float(t2-t)/1000}s")

    return f


def swap(arr, i, j):
    a = arr[i]
    arr[i] = arr[j]
    arr[j] = a


@time_me
def bubblesort(tosort):
    change = 0  # starts
    while True:  # iterate until we actually have 0 changes in
        i = 0
        while i < len(tosort) - 1:
            if tosort[i] > tosort[i + 1]:
                swap(tosort, i, i + 1)
                change += 1
            i += 1
        if change == 0:
            return tosort
        else:
            change = 0


def test(testfunction, testsets):
    for test in testsets:
        testfunction(test)
        print (f"sorted {test}")

def main():
    testdata = (
        [5, 2, 3, 1, 4],
        [1, 2, 3, 4, 5],
        [5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 45, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4,5, 2, 3, 1, 4]
    )
    test(bubblesort, testdata)


if __name__ == "__main__":
    main()
