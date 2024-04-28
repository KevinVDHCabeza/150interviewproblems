class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(len(s)-1,-1,-1):
            valor=roman_to_int[s[i]]
            if i < len(s) -1 and valor < roman_to_int[s[i+1]]:
                total-=valor
            else:
                total+=valor
        return total        