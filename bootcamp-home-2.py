from shared import mock

def amp(a):
    return abs(a[2]-a[1])

def findextreems(list):
    minamp = None
    maxamp = None

    for d in list:
        amp_d = amp(d)
        if(minamp == None or amp(minamp) > amp_d):
            minamp = d
        if(maxamp == None or amp(maxamp) < amp_d):
            maxamp = d

    return (minamp, maxamp)

@mock.fromfile("./mock-zadanie-2.data")
def getdata():
    pass

def tostring(tuple):
    return f"{tuple[0]} --> {tuple[1]} {tuple[2]} [diff: {amp(tuple)}]"

def main():
    extreme = findextreems(getdata())
    print (f" min: {tostring(extreme[0])} max: {tostring(extreme[1])}" )


if __name__ == "__main__":
    main()
