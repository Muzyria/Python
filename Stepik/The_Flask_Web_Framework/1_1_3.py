import re


def solution(s):
    words = re.findall(r'[А-Яа-я]+ [А-Яа-я]+', s)
    print(*words if words else ["Мало слов!"], sep='\n')


solution(input())

