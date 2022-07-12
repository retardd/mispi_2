def search(a, g):
    result = [0]*(len(a) + len(g) - 1)
    for i in range(len(a)):
        for j in range(len(g)):
            result[i + j] += a[i] * g[j]
    for i in range(len(result)):
        if result[i] % 2 == 0:
            result[i] = 0
        else:
            result[i] = 1
    return result

def print_mn(r):
        result = ''
        c = 0
        for i in range(len(r)):
            if r[i] != 0:
                if i == 0:
                    result = result + '+' + str(r[i])
                elif i == 1:
                    if r[i] == 1:
                        result = result + '+' + 'x'
                    else:
                        result = result + '+' + str(r[i]) + 'x'
                else:
                    if r[i] == 1:
                        result = result + '+' + 'x^' + str(i)
                    else:
                        result = result + '+' + str(r[i]) + 'x^' + str(i)
                c += 1
        return result, c


matr2 = []
for i in range(pow(2, 4)):
    matr_buff = [0, 0, 0, 0]
    matr2.append(matr_buff)
for i in range(pow(2, 4)):
    buff = int(format(i, 'b'))
    dl2 = 3
    while buff != 0:
        matr2[i][dl2] = buff % 10
        buff = buff // 10
        dl2 -= 1

print("Введите коэффициенты для порождающего многочлена: ", end='')
kf = list(map(int, input().split()))
print("Порождающий многочлен: ", end='')
mng, count = print_mn(kf)
print(mng[1:])
print("a[i]:")

a = [0, 0, 0, 0]

for i in range(16):
    a = matr2[i]
    buff = search(a, kf)
    for char in buff:
        print(char, end='')
    print('    | ', i)
