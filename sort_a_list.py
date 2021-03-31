
# Python Program to Sort List in Ascending Order

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()

print("Element After Sorting List in Ascending Order is : ", NumList)
Python Program to Sort List in Ascending Order 1
Python Program to Sort List in Ascending Order without using Sort
In this program, we are using Nested For Loop to iterate each number in a List, and sort them in ascending order.

# Python Program to Sort List in Ascending Order

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for i in range (Number):
    for j in range(i + 1, Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)
