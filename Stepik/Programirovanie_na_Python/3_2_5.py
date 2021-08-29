def update_dictionary(d, key, value):
    # put your python code here
    if key in d:
        d[key].append(value)
        #print('ключ есть')
    elif key is not d:
        #d[2*key]=[]
        if 2*key is d:
            d[2*key].append(value)
            #print('ключ 2*key уже есть')
        elif (2*key is not d) and d.get(2*key)==None:
            d[2*key]=[]
            d[2*key].append(value)
            #print('создание ключа и + новое значение списка')
        elif (2*key is not d) and d.get(2*key)!=None:
            d[2*key].append(value)
            #print('создание ключа и + значение списка')       
    return     