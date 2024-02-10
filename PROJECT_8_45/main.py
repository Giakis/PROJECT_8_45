import math
def divisors(n):
    divs = []
    for i in range(1, n+1):
        if n % i == 0:
            divs.append(i)
    return divs

#Παιρνουμε στην λίστα μας όλους τους περιττούς αριθμούς.
#Ξεκιναμε την for μας από 3 καθώς ο αριθμός 2 δεν είναι περιττός,
#Και ο αριθμός 1 στον παρονομαστή μας κάνει 0,ln(ln(1))=0.
n=[]
for num in range(3, 1048576):
    #Checking condition
    if num % 2 != 0:
        n.append(num)

temp = False
for i in range(len(n)):
    divisors_list = divisors(n[i])
    sum = 0
    for j in range (len(divisors_list)):
        sum += divisors_list[j]
    #Βρισκω τον αριθμό του Euler ο οποίος είναι το άθροισμα όλων των περιττών
    Euler = 0
    for z in range (1, n[i]):
        Euler += (1 / z)
    #Υλοποιώ τον τύπο αλλά πρώτα σπάω σε μικρότερα κομμάτια τις πράξεις
    A = (math.exp(Euler)) // 2
    B = math.log(math.log(n[i]))
    G = 0.74 // math.log(math.log(n[i]))
    Total = A * B + G
    if ((sum / n[i]) < Total ):
        temp = True
    else:
        temp = False
        break

print(temp)
