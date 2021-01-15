def sortPizzas(pizzas):
    for i in range(len(pizzas)-1):
        for j in range(i+1,len(pizzas)):
            if(len(pizzas[i])<len(pizzas[j])):
                pizzas[i],pizzas[j] = pizzas[j],pizzas[i]
    return pizzas

def maxPizzas(M,T2,T3,T4,pizzas):

    if(len(pizzas)==0):
        return

    pizzas = sortPizzas(pizzas)

    # for T4:
    max = 0
    initial = pizzas[0]

    team4 = [initial]

    duplicate_pizzas = [i for i in pizzas]

    # for 2nd element:
    El2 = []
    for i in range(1,len(duplicate_pizzas)):
        counter = 0
        for j in duplicate_pizzas[i]:
            if j not in initial:
                counter += 1
        if counter >= max:
            max = counter
            El2 = duplicate_pizzas[i]
    initial = initial + El2
    try:
        duplicate_pizzas.remove(El2)
    except:
        pass
    team4.append(El2)

    # for 3rd element:
    El3 = []
    max = 0
    for i in range(1,len(duplicate_pizzas)):
        counter = 0
        for j in duplicate_pizzas[i]:
            if j not in initial:
                counter += 1
        if counter >= max:
            max = counter
            El3 = duplicate_pizzas[i]
    initial = initial + El3
    try:
        duplicate_pizzas.remove(El3)
    except ValueError:
        pass
    team4.append(El3)

    # for 4th element:
    El4 = []
    max = 0
    for i in range(1,len(duplicate_pizzas)):
        counter = 0
        for j in duplicate_pizzas[i]:
            if j not in initial:
                counter += 1
        if counter >= max:
            max = counter
            El4 = duplicate_pizzas[i]
    initial = initial + El4
    try:
        duplicate_pizzas.remove(El4)
    except ValueError:
        pass
    team4.append(El4)

    print('team 4 is : ',team4)

    # for T3:
    max = 0
    initial = pizzas[0]

    team3 = [initial]
    duplicate_pizzas = [i for i in pizzas]

    # for 2nd element:
    El2 = []
    for i in range(1,len(duplicate_pizzas)):
        counter = 0
        for j in duplicate_pizzas[i]:
            if j not in initial:
                counter += 1
        if counter >= max:
            max = counter
            El2 = duplicate_pizzas[i]
    initial = initial + El2
    team3.append(El2)
    try:
        duplicate_pizzas.remove(El2)
    except ValueError:
        pass

    # for 3rd element:
    El3 = []
    max = 0
    for i in range(1,len(duplicate_pizzas)):
        counter = 0
        for j in duplicate_pizzas[i]:
            if j not in initial:
                counter += 1
        if counter >= max:
            max = counter
            El3 = duplicate_pizzas[i]
    initial = initial + El3
    team3.append(El3)
    try:
        duplicate_pizzas.remove(El3)
    except ValueError:
        pass

    print('team 3 is : ',team3)

    #for team 2 :

    max = 0
    initial = pizzas[0]

    team2 = [initial]
    duplicate_pizzas = [i for i in pizzas]

    # for 2nd element:
    El2 = []
    for i in range(1,len(duplicate_pizzas)):
        counter = 0
        for j in duplicate_pizzas[i]:
            if j not in initial:
                counter += 1
        if counter >= max:
            max = counter
            El2 = duplicate_pizzas[i]
    initial = initial + El2
    team2.append(El2)
    try:
        duplicate_pizzas.remove(El2)
    except ValueError:
        pass

    print('team 2 is : ',team2)

    # calculating scores for T4:
    teamF4 = []
    for i in team4:
        for j in i:
            if j not in teamF4:
                teamF4.append(j)
    team4score = len(teamF4)**2
    print('team 4 score is : ',team4score)

    # calculating scores for T3:
    teamF3 = []
    for i in team3:
        for j in i:
            if j not in teamF3:
                teamF3.append(j)
    team3score = len(teamF3)**2
    print('team 3 score is : ',team3score)

    # calculating scores for T2:
    teamF2 = []
    for i in team2:
        for j in i:
            if j not in teamF2:
                teamF2.append(j)
    team2score = len(teamF2)**2
    print('team 2 score is : ',team2score)

    if(team4score>=team3score and team4score>=team2score):
        if( T4>0 and ((M%4)==0 or ((M%4)%3 == 0 and T3>0) or ((M%4)%2 == 0 and T2>0))):
            print('executed for 4 M=',M)
            for i in team4:
                try:
                    pizzas.remove(i)
                except ValueError:
                    pass
            MaxResultScore[0] += team4score
            distributed[0] += 1
            maxPizzas((M-4),T2,T3,T4-1,pizzas)
            return

    if(team3score>=team4score and team3score>=team2score):
        if( T3>0 and ((M%3)==0 or ((M%3)%2 == 0 and T2>0))):
            print('executed for 3')
            for i in team3:
                try:
                    pizzas.remove(i)
                except ValueError:
                    pass
            MaxResultScore[0] += team3score
            print('MaxResultScore is : ',MaxResultScore[0])
            distributed[0] += 1
            maxPizzas((M-3),T2,T3-1,T4,pizzas)
            return

    if(team2score>=team3score and team2score>=team4score):
        if( T2>0 and ((M%2)==0 or (T3>0 and T4>0 and M>=5))):
            print('executed for 2')
            for i in team2:
                try:
                    pizzas.remove(i)
                except ValueError:
                    pass
            MaxResultScore[0] += team2score
            print('MaxResultScore is : ',MaxResultScore[0])
            distributed[0] += 1
            maxPizzas((M-2),T2-1,T3,T4,pizzas)
            return
    

test_case = open('D:/Google hashcode 2021/practice/b_little_bit_of_everything.txt','r')

counter = 0
pizzas = []
MaxResultScore = [0]

M = T2 = T3 = T4 = 0
for i in test_case.readlines():
    if counter==0:
        M,T2,T3,T4 = tuple(i.split())
    else:
        arr = i.split()
        pizzas.append(arr[1:])
    counter += 1
distributed = [0]

MaxResultScore = [0]

print(maxPizzas(int(M),int(T2),int(T3),int(T4),pizzas))
print('MaxResultScore is : ',MaxResultScore[0])
print('distributed to ',distributed[0],' teams')