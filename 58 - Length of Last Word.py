s="  moonooo fly me   to moonooao  the moon  "


s.strip().split()
print(len(s.strip().split()[-1]))

#Wrong idea
#lenword=0
#contador=0
#for i in range(len(s)):
#    if s[i]!=" ":
#        contador+=1
#        if i== len(s)-1 or s[i+1] == " ":
#            lenword=contador
#            contador=0
