def canJump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

if __name__ == "__main__":
    nums = [2, 5, 0, 0]
    print(canJump(nums)) 