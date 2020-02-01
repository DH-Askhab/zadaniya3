import string

print('Калькулятор')


def delenie(chislo1, chislo2):
    # Были и такие варианты, но, забил))
    # # if chislo1 == float(chislo1) or int(chislo1) and chislo2 == float(chislo2) or int(chislo2):
    # if chislo1 == float(chislo1) and chislo2 == float(chislo2):
    # # try:
    # #     float(chislo1)
    # #     try:
    # #         float(chislo2)
    #         i = chislo2
    #         if i != 0:
    #             resultat = chislo1 / chislo2
    #             resultat = float('{:.2f}'.format(resultat))
    #             print('{}/{} ='.format(chislo1, chislo2), resultat)
    #
    #         else:
    #             print('На 0 делить нельзя')
    # #     except ValueError:
    # #         print('Введите число!')
    # #
    # # except ValueError:
    # #     print('Введите число!')
    # else:
    #     print('Введите число!')
    if chislo2 > 0:
        resultat = chislo1 / chislo2
        resultat = float('{:.2f}'.format(resultat))
        chislo1 = str(chislo1)
        chislo2 = str(chislo2)
        print('{}/{} ='.format(chislo1, chislo2), resultat)
    else:
        print('На 0 делить нельзя')


try:
    delenie(chislo1=float(input('Введите первое число: ')), chislo2=float(input('Введите первое число: ')))
except:
    print('Ошибка, введите число')

print('второе здание')


#
def dannye(imya, familiya, gorod_rozhdeniya, gorod_prozhivaniya, mail, nomer):
    print('Ваше имя: {}, фамилия: {},'
          'город рождения: {}, город проживания: {},'
          'Контакты: {}, {}'.format
          (imya, familiya, gorod_rozhdeniya, gorod_prozhivaniya, mail, nomer))


dannye(imya=(input('Введите имя: ')),
       familiya=(input('Введите фамилию: ')),
       gorod_rozhdeniya=(input('Введите город рождения: ')),
       gorod_prozhivaniya=(input('Введите проживаеия: ')),
       mail=(input('Введите e-mail: ')),
       nomer=(input('Введите номер телефона: ')))

print('3 задание')


# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(ctifry, ctifry1, ctifry2):
    if ctifry > ctifry1 or ctifry > ctifry2:
        ctifry = ctifry
    else:
        ctifry = 0

    if ctifry1 > ctifry or ctifry1 > ctifry2:
        ctifry1 = ctifry1
    else:
        ctifry1 = 0
    if ctifry2 > ctifry or ctifry2 > ctifry1:
        ctifry2 = ctifry2
    else:
        ctifry2 = 0
    print(ctifry + ctifry1 + ctifry2)


my_func((int(input('Введите число: '))), (int(input('Введите число: '))),
        (int(input('Введите число: '))))

print('4 задание')


def my_func2(x, y):
    print(x ** y)
    kakaya_to_peremennaya = 1
    print('выполняем цикл, в соответствии с заданием')
    while (y > 0):
        kakaya_to_peremennaya *= x
        y -= 1
    print(kakaya_to_peremennaya)


my_func2((float(input('Введите число: '))), (float(input('Введите число: '))))
print('5 задание')
stroka_chisel = list(map(int, input('Введите числа через пробел: ').split()))
print("Сумма чисел равна:", sum(stroka_chisel))

print('6 задание')
def int_func3(slovo):
    print(string.capwords(slovo))


int_func3(slovo=(input('Введите слово: ')))
