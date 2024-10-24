def is_context_manager(obl) -> bool:
    return hasattr(obl, '__enter__')



print(is_context_manager(open('output.txt', mode='w')))