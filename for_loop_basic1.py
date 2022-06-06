# 1.basic
for n in range(0, 151):
    print(n)

# 2.Multiples of Five
for n in range(5, 1001, 5):
    print(n)

# 3.Counting the Dojo Way
# for n in range(1, 101):
#     if n%5 == 0:
#         print("Coding")
#     if n%10 == 0:
#         print("Coding dojo")
for n in range(1, 101):
    if n%10 == 0:
        print(str(n) + ": Coding dojo")
    elif n%5 == 0:
        print(str(n) + ": Coding")

# 4.Whoa. That Sucker's Huge
sum = 0
for n in range(1, 50000,2):
    sum += n
print(sum)


# 5. Countdown by Fours
for n in range(2018, 0, -4):
    print(n)
# 6. Flexible Counter
def mult(lowNum, highNum, mult):
    for n in range(lowNum, highNum+1):
        if n%mult == 0:
            print(n)
mult(10,100,14)