r=int(input('Podaj wielkość planszy :'));[print([' ---'*r, '|   '*(r+1)][i%2]) for i in range(r*2)]; print(' ---'*r)