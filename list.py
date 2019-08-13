def Split(mix): 
    ev_li = [] 
    od_li = [] 
    for i in mix: 
        if (i % 2 == 0): 
            ev_li.append(i) 
        else: 
            od_li.append(i) 
    print("Even lists:", ev_li) 
    print("Odd lists:", od_li) 
mix=[1,2,3,4,6]
Split(mix)
