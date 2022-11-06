
# l={"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"}
def solution(l):
    parsed = [e.split(".") for e in l]
    x = [map(int, e) for e in parsed]
    y = sorted(x)
    res = [('.'.join(str(ee) for ee in e)) for e in y]
    return res
# res=[i for i in l]
# res.sort()
# final=(",").join(res)
# print(final)