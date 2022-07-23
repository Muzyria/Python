def hide_card(value):
    value = value.replace(" ", '')
    return f"************{value[12:]}"


card = '905 678123 45612 56'

print(hide_card(card))   
