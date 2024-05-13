def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """


    if "".join(letter for letter in s if letter.isalnum()).lower() == "".join(letter for letter in s if letter.isalnum()).lower()[::-1]:
        return True
    else:
        return False
if __name__ == "__main__":
        s = "A man, a plan, a canal: Panama"
        print(isPalindrome(s))