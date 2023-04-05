
tic = 'QAN.AX'


str1= """John said, "Let's learn Python together". """              #triple quotes for quoting conversation
print(str1)

f = 0.2 + 0.2 + 0.2
print(f)
print(f==0.6)                                       #ans = 0.600000001 =/= 0.6 > false

print(1==1)
print(1=1)                #error

print(3*3)
print('3'*3)                             #333

print

x = str('abc')
xup = str.upper(x)
print(xup)

weird_case = "My fUnNy tYpEcAsE sTrInG"

weird_case_upper = weird_case.upper()       # --> "MY FUNNY TYPECASE STRING"

print(weird_case_upper)

x = 56 * 33 * 30.5
print(f"The volume of the box is {x} cubic centimeters.")

# to select the main domain from the sentence
str1 = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
str1 = str1.split()[1].split('@')[1]
print(str1)

#str1 = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
#str1 = str1.split()[1].split('@')[1] (split into list first and choose [1] first index and split at @ and choose [1])
#print(str1)

s = set()
s.add("QAN.AX")   # s is {"QAN.AX"}
s.add("WES.AX")   # s is {"QAN.AX", "WES.AX"}
s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"}
s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"} (so no change)

print("e")


