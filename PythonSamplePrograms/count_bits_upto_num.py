def count_bits_upto_num(num: int) -> list[int]:
    result = []
    for i in range(num + 1):
        curr_num_bit_count = 0
        curr_num = i
        while curr_num > 0:
            curr_num_bit_count += curr_num & 1
            curr_num >>= 1
        result.append(curr_num_bit_count)
    return result


print(count_bits_upto_num(8))
