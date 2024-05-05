from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import date

# Создаем базу данных и таблицу
def init_db():
    connection = sqlite3.connect('db_1.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Shashlik
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name_shashlik TEXT NOT NULL,
         supplier TEXT,
         date_delivery DATE,
         price_per_tonn INTEGER)
    ''')
    connection.commit()
    connection.close()

# Функция добавления данных в таблицу
def add_row_in_table():
    name_shashlik = entry_name.get()
    supplier = entry_supplier.get()
    date_dev = date.today()
    price = int(entry_price.get())

    connection = sqlite3.connect('db_1.db')
    cursor = connection.cursor()
    sql = '''
        INSERT INTO Shashlik(name_shashlik, supplier, date_delivery, price_per_tonn)
        VALUES (?, ?, ?, ?)
    '''
    cursor.execute(sql, (name_shashlik, supplier, date_dev, price))
    connection.commit()
    connection.close()
    update_treeview()  # Обновляем таблицу в интерфейсе после добавления данных

    # Очистка полей после ввода
    entry_name.delete(0, END)
    entry_supplier.delete(0, END)
    entry_price.delete(0, END)

# Функция для обновления данных в Treeview
def update_treeview():
    for i in tree.get_children():
        tree.delete(i)
    connection = sqlite3.connect('db_1.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Shashlik")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)
    connection.close()

# Создаем основное окно приложения
root = Tk()
root.title("Shashlik Database Interface")
root.iconbitmap("barbecue (2).ico")
# Создаем виджеты для ввода данных
Label(root, text="Название шашлыка:").grid(row=0, column=0)
entry_name = Entry(root)
entry_name.grid(row=0, column=1)

Label(root, text="Поставщик:").grid(row=1, column=0)
entry_supplier = Entry(root)
entry_supplier.grid(row=1, column=1)

Label(root, text="Стоимость за кг:").grid(row=2, column=0)
entry_price = Entry(root)
entry_price.grid(row=2, column=1)

# Кнопка для добавления данных
button_add = Button(root, text="Добавить в базу", command=add_row_in_table)
button_add.grid(row=3, column=1, pady=10)

# Treeview для отображения данных из базы
tree = ttk.Treeview(root, columns=('ID', 'Name', 'Supplier', 'Date', 'Price'), show='headings')
tree.grid(row=4, column=0, columnspan=2)

tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Supplier', text='Supplier')
tree.heading('Date', text='Date')
tree.heading('Price', text='Price')

# Инициализация базы данных и интерфейса
init_db()
update_treeview()

# Запуск главного цикла Tkinter
root.mainloop()