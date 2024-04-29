def january():
    return "January"
def february():
    return "February"
def march():
    return "March"
def april():
    return "April"
def may():
    return "May"
def june():
    return "June"
def july():
    return "July"
def august():
    return "August"
def september():
    return "September"
def default():
    return "Нет такого"
switch_case = {
    1: january,
    2: february,
    3: march,
    4: april,
    5: may,
    6: june,
    7: july,
    8: august,
    9: september,
}
def switch(x):
    return switch_case.get(x, default)()
print(switch(1))
