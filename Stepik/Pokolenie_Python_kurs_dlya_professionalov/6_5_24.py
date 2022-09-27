from collections import defaultdict


def best_sender(messages: list, senders: list):
    result = defaultdict(list)
    for elm in range(len(senders)):
        result[senders[elm]].extend(messages[elm].split())
    return max([(k, v) for k, v in result.items()], key=lambda x: (len(x[1]), x[0]))[0]


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']


print(best_sender(messages, senders))
