a = input ("geef getal a aan: ") 
b = input ("geef getal b aan: ") 
if a>b:
    max = a
    min = b
    print("a is groter dan b")
elif a<b:
    max = b
    min = a
    print("b is groter dan a")
    print("Het maximum is: " + str(max))
    print("het minimum is: " + str(min)) 
elif a==b:
    print ("a is gelijk aan b") 

    


