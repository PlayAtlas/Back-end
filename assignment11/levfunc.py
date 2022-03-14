def lfunc(w1, w2):
    if w1 == "":
        return len(w2)
    if w2 == "":
        return len(w1)
    if w1[-1] == w2[-1]:
        countlast = 0
    else:
        countlast = 1

    return min([lfunc(w1[:-1], w2) + 1,
               lfunc(w1, w2[:-1]) + 1, 
               lfunc(w1[:-1], w2[:-1]) + countlast])

print(lfunc('aee','bbb'))