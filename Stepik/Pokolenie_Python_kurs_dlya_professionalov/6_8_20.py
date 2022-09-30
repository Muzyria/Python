from collections import Counter


def print_bar_chart(data: (list, str), mark: str):
    max_len = len(max(data, key=len)) if type(data) == list else 1
    print(max_len)
    [print(f'{k.ljust(max_len)} |{mark * v}') for k, v in Counter(data).most_common()]


print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')
