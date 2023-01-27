import random
lan = 0
l1=["a","s","l","m","n"]
l2=["b","g","y","e","i"]
l3=["w","d","o","u","h"]
while True :
    name = input("dakhl ismmk : ")
    for i in range(len(name)): 
        if name[i] in l1 :
            lan = lan + 10
        if name[i] in l2 :
            lan = lan + 5
        if name[i] in l3 : 
            lan = lan + 2
    y = random.randint(0,50)  
    lan = lan + y      
    if lan > 100 :
        lan = lan/10
        add = random.randint(10,50)
        lan = lan + add 

    print(f"{name} nakch binasbat : {lan} %") 
