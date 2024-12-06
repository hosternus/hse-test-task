from random import randint

def jaccard_index(str1: str, str2: str) -> float:
    a = set(str1.lower().split())
    b = set(str2.lower().split())
    intersection = a.intersection(b)
    union = a.union(b)
    ans = len(intersection) / len(union)
    return ans if ans else (randint(1,9) / randint(1,9))/1000
