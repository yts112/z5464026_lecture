lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new_lst = [x**2 for x in lst if x**2 > 150]
print(f'the new list with value of square greater than 150 is {new_lst}')

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]


def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic

print(tic)

#Function

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

tic = "WES.AX"            # (5)
print(tic)                # (6)

qan_tic()                 # (7)



test_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]

def is_even_number(lis):
    evennum=()
    for n in lis:
        evennum.append(n)
    return evennum

is_even_number(test_list)

