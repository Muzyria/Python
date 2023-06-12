def is_context_manager(obj):
    return '__enter__' in dir(obj) and '__exit__' in dir(obj)


print(is_context_manager(open('output.txt', mode='w')))
