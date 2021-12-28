# Создание класса Stack с требуемыми методами
class Stack:
    def __init__(self):
        self.initial_stack = []

    def isEmpty(self):
        return self.initial_stack == []

    def push(self, item):
        self.initial_stack.append(item)

    def pop(self):
        return self.initial_stack.pop()

    def peek(self):
        return self.initial_stack[len(self.initial_stack) - 1]

    def size(self):
        return len(self.initial_stack)


# Создание функции по проверке строки
def checkBrackets(str):
    # Задание возможных вариантов представления скобок
    open_brackets = ['(', '[', '{']
    closed_brackets = [')', ']', '}']
    # Инициализация объекта Stack
    stack = Stack()

    # Если в строке нечетное кол-во символов, она несбалансирована
    if len(str) % 2 == 0:
        # Анализ каждого символа строки в цикле
        for char in str:
            if char in open_brackets:
                stack.push(char)
            elif char in closed_brackets:
                # Проверка на сочетание открывающей и закрывающей скобок
                index = closed_brackets.index(char)
                if not(stack.isEmpty()) and open_brackets[index] == stack.peek():
                    stack.pop()
                else:
                    return 'Несбалансированно'
        if stack.isEmpty():
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'
    else:
        return 'Несбалансированно'


# Ввод интересующего значения строки для проверки и осуществление этой проверки
check_str = input('Введите строку, которую хотите проверить: ')
print(checkBrackets(check_str))
