from string import ascii_lowercase as ascii

print(alphabet := {k: v for v, k in enumerate(ascii, 1)})
