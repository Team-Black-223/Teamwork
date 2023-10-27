stack = []  # Инициализираме празен стек

n = int(input('Enter how many commands you want to enter:'))  # Четем броя на командите

for _ in range(n):
    command = input('Enter command:').split()

    if command[0] == 'Add'.lower():
        number = int(command[1])
        stack.append(number)  # Добавяме числото най-отзад на стека
    elif command[0] == 'Dell'.lower():
        if stack:
            stack.pop()  # Изтриваме числото, което е най-отгоре на стека
    elif command[0] == 'Biggest'.lower():
        if stack:
            print(max(stack))  # Извеждаме най-голямото число в стека
    elif command[0] == 'Lowest'.lower():
        if stack:
            print(min(stack))  # Извеждаме най-малкото число в стека
    elif command[0] == 'Len'.lower():
        print(len(stack))  # Извеждаме дължината на стека

# Изпразваме стека и го печатаме в обратен ред
stack.reverse()
print(', '.join(map(str, stack)))
