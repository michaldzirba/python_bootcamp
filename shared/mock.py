def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@parametrized
def fromfile(f, file):
    # if not defined DEVELOPMENT MODE :
        # return f # no devel no mocks

    def m():
        result = []
        with open(file, "r") as fp:
            for i in fp.readlines():
                tmp = i.split(",")
                try:
                    result.append((tmp[0], float(tmp[1]), float(tmp[2])))
                except:
                    pass
        return result
    return m


def static(f):
    def m():
        return [('2011-01-02', -1, 99), ('2001-02-02', 1, 333), ('2020', 2, 999), ('2018-01-01', -1, 4),
                ('1900-08-08', 26, 34)]

    return m
