def convert(number):
    return str(bin(number)).replace('0b', ''), str(oct(number)).replace('0o', ''), \
           str(hex(number)).replace('0x', '').upper()

# def convert(number: int):
#     return(f"{number:b}", f"{number:o}", f"{number:X}")


print(convert(15))
# ('1111', '17', 'F')

print(convert(-24))
# ('-11000', '-30', '-18')

print(convert(1))
# ('1', '1', '1')
