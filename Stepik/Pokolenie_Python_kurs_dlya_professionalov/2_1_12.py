
def spell(*args):
    data = {}
    for word in args:
        if word[0].lower() not in data:
            data.setdefault(word[0].lower(), len(word))
        if word[0].lower() in data and data[word[0].lower()] < len(word): 
            data[word[0].lower()] = len(word)
    return data    


words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))    

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
