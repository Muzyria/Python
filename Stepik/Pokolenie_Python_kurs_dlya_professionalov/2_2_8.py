
n = int(input())
lst_email = {}
for _ in range(n):
    email = input()
    name_email, mail = email.split('@')
    number = ''
    name = ''
    for i in name_email:
        if i.isdigit():
            number += i
        else:
            name += i
    lst_email[name] = lst_email.get(name, []) + [number]
# print(lst_email)

m = int(input())
for _ in range(m):
    new_name = input()
    if new_name not in lst_email:
        lst_email[new_name] = lst_email.get(new_name, []) + ['']
        print(f"{new_name}@beegeek.bzz")
    else:
        if '' in lst_email[new_name]:
            for j in range(1, 100):
                if str(j) not in lst_email[new_name]:
                    lst_email[new_name] = lst_email.get(new_name, []) + [str(j)]
                    print(f"{new_name}{j}@beegeek.bzz")
                    break
        else:
            lst_email[new_name] = lst_email.get(new_name, []) + ['']
            print(f"{new_name}@beegeek.bzz")


print(lst_email)
