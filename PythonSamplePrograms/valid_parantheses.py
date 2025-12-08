def is_valid_parantheses(s: str)->bool:
    p_stack = []
    p_hash = {"]":"[", "}":"{", ")":"("}
    for para in s:
        if para in p_hash.values():
            p_stack.append(para)
        else:
            if len(p_stack) != 0:
                if p_hash[para] != p_stack.pop():
                    return False
            else:
                return False
    return len(p_stack) == 0


print(is_valid_parantheses("){"))
print(is_valid_parantheses("(]"))
print(is_valid_parantheses("([])"))
print(is_valid_parantheses("([)]"))