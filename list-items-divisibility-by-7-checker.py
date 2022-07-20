#lista z 5 liczbami, niech znajdzie liczbę podzielną przez 7

list= []
counter=0

while counter<5:
    number=int(input("Enter a number: "))
    list.append(number)
    counter+=1

#resetting the counter
counter=0

while counter<5:
    if list[counter]%7==0:
        print(f"The number divisible by 7 is: {list[counter]}")
    counter+=1
