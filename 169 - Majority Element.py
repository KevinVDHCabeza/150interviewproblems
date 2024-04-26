

nums = [6,5,5]
s = list(set(nums))
cont = 0
for i in range(len(s)):
   if nums.count(s[i])>nums.count(s[cont]):
       cont=i


print(s[cont])