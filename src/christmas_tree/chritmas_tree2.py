# def branch(n):
#     for i in range(n):
#         print(' ' * (n - i) + '*' * (1 + (i - 1)* 2) + ' ' * (n - i))
# if __name__ == '__main__':
#     n = int(input('Podaj liczbę gałęzi choinki: '))
#     branch(n)


def choinka(n):
    [print(' ' * (n-galaz) + '*' * (galaz * 2 - 1)) for galaz in range(0, n+1)]
if __name__ == '__main__':
    n = int(input('Ile galezi: '))
    choinka(n)

