def even(mix): 
    ev_li = [] 
    for i in mix: 
        if (i % 2 == 0): 
            ev_li.append(i) 
    print("Even lists:", ev_li) 
mix=[1,2,3,4,6]
even(mix)
