import re


if __name__ == '__main__':

    # print(
    #     'OK' if re.match('(.*)\d{2}-\d{3}\s', input('POdaj kod pocztowy')
    #     else 'Nie ok'
    # )
    print(
     re.match('^\d{2}-\d{3}$', input('Podaj kod pocztowy'))
    )