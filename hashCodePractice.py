def maximize(arr):
    dic = {'2':0, '3':0, '4':0}
    dicArr = {'2':[], '3':[], '4':[]}

    for i in range(2**len(arr)):

        t = [arr[j] for j in range(len(arr)) if(i & (1<<j))]
        res = []

        if(len(t)==2):
            for j in t:
                for k in j:
                    if(k not in res):
                        res.append(k)
            if len(res)>dic['2']:
                dic['2'] = len(res)
                dicArr['2'] = t

        elif(len(t)==3):
            for j in t:
                for k in j:
                    if(k not in res):
                        res.append(k)
            if len(res)>dic['3']:
                dic['3'] = len(res)
                dicArr['3'] = t

        elif(len(t)==4):
            for j in t:
                for k in j:
                    if(k not in res):
                        res.append(k)
            if len(res)>dic['4']:
                dic['4'] = len(res)
                dicArr['4'] = t

    return dic,dicArr

def maxPizzas(M,T2,T3,T4,pizzas):
    print('maxpizzas executing')
    if(len(pizzas)==0):
        return
    score,scoresArr = maximize(pizzas)

    print(score,scoresArr)
    print('pizzas is : ',pizzas)

    # remove the pizzas from the array which has been already ordered

    if(score['4']>=score['3'] and score['4']>=score['2']):
        if( T4>0 and ((M%4)==0 or ((M%4)%3 == 0 and T3>0) or ((M%4)%2 == 0 and T2>0))):
            print('executed for 4 M=',M)
            for i in scoresArr['4']:
                pizzas.remove(i)
            MaxResultScore[0] += score['4']**2
            maxPizzas((M-4),T2,T3,T4-1,pizzas)
            return

    if(score['3']>=score['4'] and score['3']>=score['2']):
        if( T3>0 and ((M%3)==0 or ((M%3)%2 == 0 and T2>0))):
            print('executed for 3')
            for i in scoresArr['3']:
                pizzas.remove(i)
            MaxResultScore[0] += score['3']**2
            print('MaxResultScore is : ',MaxResultScore[0])
            maxPizzas((M-3),T2,T3-1,T4,pizzas)
            return

    if(score['2']>=score['3'] and score['2']>=score['4']):
        if( T2>0 and ((M%2)==0 or (T3>0 and T4>0 and M>=5))):
            print('executed for 2')
            for i in scoresArr['4']:
                pizzas.remove(i)
            MaxResultScore[0] += score['2']**2
            print('MaxResultScore is : ',MaxResultScore[0])
            maxPizzas((M-2),T2-1,T3,T4,pizzas)
            return

    print(pizzas)
    print(maximize(pizzas))

# Driver code :

test_case = open('D:/Interview preparation/algorithms/practice/b_little_bit_of_everything.txt','r')

counter = 0
pizzas = []
MaxResultScore = [0]

M = T2 = T3 = T4 = 0
for i in test_case.readlines():
    print('started',counter+1)
    if counter==0:
        M,T2,T3,T4 = tuple(i.split())
    else:
        arr = i.split()
        pizzas.append(arr[1:])
    counter += 1

# performing the function :
maxPizzas(int(M),int(T2),int(T3),int(T4),pizzas)

# printing the final result :
print('Final Maximised result is :',MaxResultScore[0])


