def get_name():
    names = []
    while True:
        x = input("enter 5 elements in the first row : ").lower()
        if x in names:
            print(x.upper(), "has already been entered")
        elif x == " ":
            print("The space is not allowed")
        elif len(names) <= 5:
            names.append(x)
            print(names)
            print(len(names))
    return()

elements_list = []
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements.txt
elements = open('elements.txt', 'r')
elements.readline().lower()

for x in elements:
    elements_list.append(x)
count = 0
for x in elements_list:
    elements_list[count] = x[:-1]
    count += 1
print(elements_list)
get_name()

incorrect_ansers = []
correct_ansers = []
for x in names:
    if x in element_list:
        incorrect_ansers.append(x)
    else:
        correct_ansers.append(x)

cor = len(correct_ansers)

cor1 = cor / 5
cor2 = cor1 * 100

print('Your score is %', cor2)
print("Not Found : ", incorrect_ansers)
print('Found : ', correct_ansers)

