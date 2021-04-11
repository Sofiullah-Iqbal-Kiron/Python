# Acceped in C, C++, Java and Python.

ih, im, fh, fm = list(map(int, input().split()))
h, m = 0, fm-im
if ih < fh:
    h = fh - ih
elif ih == fh and im == fm:
    h = 24
elif m < 0 and ih == fh:
    h = 24
elif ih > fh:
    h = (24 - ih) + fh
if m < 0:
    h -= 1
    m += 60
print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")
