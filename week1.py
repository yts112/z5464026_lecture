# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)  # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')   # (7)
print("hello")

print("a+1")

a=1
print(type(a))                                              #integer

a=2/1
print(type(a))                                              #float

1a= 1+2
print(1a)                                                    #cannot use number as variable name e.g. 1a

a1 = 1
a1 = 1+2
a1 = a1+5
print(a1)

print(a1==1)                                                #comparison

a2 = "2"+"3"+"5"
print(a2)

str 1= """John said, "Let's learn Python together". """
́