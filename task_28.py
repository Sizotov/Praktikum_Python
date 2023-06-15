


a = int(input('Введите первое неотрицительное число: '))
b = int(input('Введите второе неотрицательно число: '))
def sums(a, b):
    if a == 0:
        return b
    else:
        return sums(a-1, b+1)
print(sums(a, b))