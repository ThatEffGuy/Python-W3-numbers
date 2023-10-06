#Number inputs & 1st answer

num1 = int(input("input first number  "))
num2 = int(input("input second number "))
num3 = int(input("input third number  "))
num4 = int(input("input fourth number "))
num5 = int(input("input fifth number  "))

ans = (num1 + num2 + num3 + num4 + num5)

print ("Answer =", ans)

#Average

avr = ans / 5

print ("Average Answer =", avr)


numbers = [num1, num2, num3, num4, num5]
max_num = 0
for i in numbers:
    if i > max_num:
        max_num = i
print("Largest number = ", max_num)

numbers = [num1, num2, num3, num4, num5]
min_num = 1
for i in numbers:
    if i < min_num:
        min_num = i
print("Smallest number = ", min_num)

#Highest number & lowest
#if numbers greater than X move on

if (num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5):
    largest = num1
elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4) and (num2 >= num5):
   largest = num2
elif (num3 >= num1) and (num2 >= num2) and (num2 >= num4) and (num2 >= num5):
   largest = num3
elif (num4 >= num1) and (num2 >= num2) and (num2 >= num3) and (num2 >= num5):
   largest = num4
elif (num5 >= num1) and (num2 >= num2) and (num2 >= num3) and (num2 >= num4):
   largest = num5

#print("The largest number is", largest)


#lownum = num1, num2, num3, num4, num5
#highnum = num, num2, num3, num4, num5