a = int(input())
b = int(input())
c = int(input())
day = 21
month = 9
year = 2019

if c < year and b >= month and a > day:
    print(year - c - 1)
elif c < year:
    print(year - c)
