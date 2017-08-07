# https://www.urionlinejudge.com.br/judge/pt/problems/view/1288

# Canhão de Destruição

global sumdest

# k -> indice do projetil na lista
# sumcgeneral -> carga total acumulada do canhao
# return 1 se >= hp else 0
def dp(k, sumcgeneral):
    global sumdest
    if general[k][sumcgeneral] != -1:
        return general[k][sumcgeneral]
    if k==ni:
        return 0
    if sumcgeneral+vy[k] <= c:
        general[k][sumcgeneral] = max(dp(k+1, sumcgeneral), dp(k+1, sumcgeneral+vy[k])+vx[k])
    else:
        general[k][sumcgeneral] = dp(k+1, sumcgeneral)
    return general[k][sumcgeneral]

n = int(input().strip())
for i in range(n):
    vx, vy = ([], [])
    general = [[-1 for x in range(101)] for y in range(51)]
    sumdest = 0
    ni = int(input().strip())
    for j in range(ni):
        xy = input().strip().split(' ')
        vx.append(int(xy[0]))
        vy.append(int(xy[1]))

    c = int(input().strip())
    hp = int(input().strip())

    if dp(0,0) >= hp:
        print('Missao completada com sucesso')
    else:
        print('Falha na missao')
