strs = ["abab","aba","abc"]
strs.sort()

n=len(strs[0])
i=0
while i < n and strs[0][i]==strs[-1][i]:
    i+=1

print(strs[0][0:i])
