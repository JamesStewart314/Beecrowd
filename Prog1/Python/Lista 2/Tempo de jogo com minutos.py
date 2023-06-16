hi, mi, hf, mf = map(int, input().split())
if hf == hi and mf == mi:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    if hf > hi:
        sum = (hf-hi)*60 + mf - mi
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(sum//60, sum - (sum//60)*60))
    if hf == hi and mf > mi:
        print('O JOGO DUROU 0 HORA(S) E {} MINUTO(S)'.format(mf - mi))
    if hf == hi and mf < mi:
        print('O JOGO DUROU 23 HORA(S) E {} MINUTO(S)'.format(60 - (mi - mf)))
    if hf < hi and mf >= mi:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 - (hi - hf), mf - mi))
    if hf < hi and mf < mi:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(23 - (hi - hf), 60 - mi + mf))
