# function and object oriented programming
# functions are block of code performing task
# makes programming easy to understand in large programs
# used in oop
# break program into small parts
def welcome():
    print('welcome to python functions')
    print('thank you')


welcome()


def summing(x, y):
    return x + y


a = int((input('enter x')))
b = int((input('enter x')))
print('sum is :', summing(a, b))

# define five subjects, total, average
e = int(input('enter english grade'))
k = int(input('enter kiswahili grade'))
v = int(input('enter biology grade'))
p = int(input('enter physics grade'))
c = int(input('enter chemistry grade'))


def total(m, n, l, o, p):
    return m + n + l + o + p


def average(g, h, i, j, k):
    return (g + h + i + j + k) / 5


print(total(e, k, v, p, c))
print(average(e, k, v, p, c))


def bodymassindex():
    weight = 70
    height = 2
    bmi = weight / (height * height)
    print('bmi', bmi)
    if bmi <= 17.5:
        print('underweight')
    elif 17.5 < bmi < 22.5:
        print('normal weight')
    else:
        print('overweight')


bodymassindex()


# loop function
def looped():
    h = [25, 56, 85, 96, 78]
    for l in h:
        print(l)


looped()
