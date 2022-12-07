def GetCoef():
    from random import randint
    k = randint(1, 10)
    coeff = {}
    for i in range(k + 2):
        coeff[i] = randint(-10, 10)
    return coeff

def polynomial(coeff):
    k = len(coeff)
    result = ''
    for i in range(k-1, -1, -1):
        if coeff[i] != 0:
            if result == '':
                if coeff[i] < 0:
                    result += '-'
            else:
                if coeff[i] < 0:
                    result += ' - '
                else:
                    result += ' + '
            if i == 0 or abs(coeff[i]) != 1:
                result += str(abs(coeff[i]))
            if i > 1:
                if abs(coeff[i]) != 1:
                    result += "*"
                result += "x**" + str(i)
            elif i == 1:
                if abs(coeff[i]) != 1:
                    result += "*"
                result += "x"
    result += ' = 0'
    return result

def coefficients(p):
    coeff = {}
    max_st = 0
    p = p.replace(' ', '')[:-2]
    p = p.replace('-', '+-')
    p = p.split('+')
    for i in p:
        if i == '':
            continue
        if not ('x' in i):
            coeff[0] = int(i)
        elif not ('**' in i):
            i = i.split('x')
            if i[0] == '':
                coeff[1] = 1
            elif i[0] == '-':
                coeff[1] = -1
            else:
                coeff[1] = int(i[0][:-1])
        else:
            i = i.split('**')
            st = int(i[1])
            max_st = max(max_st, st)
            i = i[0].split('x')
            if i[0].find('*') != -1:
                coef = int(i[0][:-1])
            elif i[0].find('-') != -1:
                coef = -1
            else:
                coef = 1
            coeff[st] = coef
    return coeff, max_st

def summa(p1, p2):
    coeff1, max1 = coefficients(p1)
    coeff2, max2 = coefficients(p2)

    maxk = 0
    poly = {}
    if max1 > max2:
        max_k = max1
        poly1 = coeff1
        poly2 = coeff2
    else:
        max_k = max2
        poly1 = coeff2
        poly2 = coeff1

    for i in range(max_k, -1, -1):
        if poly1.get(i) and poly2.get(i):
            poly[i] = poly1.get(i) + poly2.get(i)
        elif poly1.get(i):
            poly[i] = poly1.get(i)
        elif poly2.get(i):
            poly[i] = poly2.get(i)
    result = polynomial(poly)
    return result


# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
f1 = open('polynomial1.txt', 'w')
f2 = open('polynomial2.txt', 'w')
f1.write(polynomial(GetCoef()))
f2.write(polynomial(GetCoef()))
f1.close()
f2.close()


# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
f1 = open('polynomial1.txt', 'r')
f2 = open('polynomial2.txt', 'r')
polynom1 = f1.readline()
polynom2 = f2.readline()
f1.close()
f2.close()

f = open('sum_of_polynomials.txt', 'w')
f.write(summa(polynom1,polynom2))
f.close()