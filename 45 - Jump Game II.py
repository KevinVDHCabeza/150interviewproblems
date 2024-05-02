def jump(nums):
    max_reach = 0
    saltos = 0
    last_jump_index = 0

    for i, num in enumerate(nums):
        if i > max_reach:
            saltos += 1
            max_reach = last_jump_index
        last_jump_index = max(last_jump_index, i + num)

    return saltos

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(jump(nums))
