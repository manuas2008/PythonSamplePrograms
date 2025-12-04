def unique_chars(s: str) -> bool:
    return len(set(s)) == len(s)


print(unique_chars("aabcEdfg"))
print(unique_chars("aabcEdfg"))
print(unique_chars("abcdef"))