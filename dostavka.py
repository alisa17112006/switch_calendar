def get_case(case):
    def case_1():
        return "Стандартная доставка"
    def case_2():
        return "Экспресс доставка"
    def case_3():
        return "Самовывоз"
    def default_case():
        return "Такой доставки нет"
    if case == 1:
        return case_1
    elif case == 2:
        return case_2
    elif case == 3:
        return case_3
    else:
        return default_case
action = get_case(int(input("Введие номер = ")))
print(action())