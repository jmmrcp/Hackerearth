texto = raw_input()
sol = ""
for letra in texto:
    sol = letra + sol
# print sol
if texto == sol:
    print "YES"
else:
    print "NO"
