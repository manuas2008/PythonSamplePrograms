def is_subsequence(s1: str, s2: str):
    n1 = len(s1)
    n2 = len(s2)
    for i in range(n2 - n1 + 1):
        if s2[i:].startswith(s1):
            return True
    return False