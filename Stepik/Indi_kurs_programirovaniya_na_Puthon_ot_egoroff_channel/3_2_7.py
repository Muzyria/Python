# put your python code here
s, vf, vs, tf, ts=map(int, input().split())
if s * vf + tf * 2 < s * vs + ts * 2:
    print('First')
elif s * vs + ts * 2 < s * vf + tf * 2:
    print('Second')
elif s * vf + tf * 2 == s * vs + ts * 2:
    print('Friendship')
