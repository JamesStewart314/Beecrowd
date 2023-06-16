N = float(input())
c100 = N//100
N -= c100*100
c50 = N//50
N -= c50*50
c20 = N//20
N -= c20*20
c10 = N//10
N -= c10*10
c5 = N//5
N -= c5*5
c2 = N//2
N -= c2*2
c100 = int(c100)
c50 = int(c50)
c20 = int(c20)
c10 = int(c10)
c5 = int(c5)
c2 = int(c2)
print(f'''NOTAS:
{c100} nota(s) de R$ 100.00
{c50} nota(s) de R$ 50.00
{c20} nota(s) de R$ 20.00
{c10} nota(s) de R$ 10.00
{c5} nota(s) de R$ 5.00
{c2} nota(s) de R$ 2.00''')
N = 100*N
m1 = N//100
N -= m1*100
m50 = N//50
N -= m50*50
m25 = N//25
N -= m25*25
m10 = N//10
N -= m10*10
m5 = N//5
N -= m5*5
m1 = int(m1)
m50 = int(m50)
m25 = int(m25)
m10 = int(m10)
m5 = int(m5)
N = int(N)
print(f'''MOEDAS:
{m1} moeda(s) de R$ 1.00
{m50} moeda(s) de R$ 0.50
{m25} moeda(s) de R$ 0.25
{m10} moeda(s) de R$ 0.10
{m5} moeda(s) de R$ 0.05
{N} moeda(s) de R$ 0.01''')
