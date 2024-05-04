from datetime import date
import sqlite3

def main():
    with sqlite3.connect('ice_cream.db') as connection:
        cursor = connection.cursor()

        # Создание таблицы
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ice_cream (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_ice TEXT NOT NULL,
            data_delivery TEXT,
            sepl TEXT
        )
        ''')

        # Функция для ввода данных пользователем
        def input_date():
            lst = []
            name_ice = input("Введите название мороженого: ")
            lst.append(name_ice)
            data_delivery = date.today()
            # Конвертируем объект date в строку
            lst.append(data_delivery.isoformat())
            sepl = input("Введите поставщика: ")
            lst.append(sepl)
            return lst

        # Функция для добавления данных в таблицу
        def addendum_data(ice_cream_data):
            name_ice, data_delivery, sepl = ice_cream_data
            sql = ''' 
            INSERT INTO Ice_cream (name_ice, data_delivery, sepl)
            VALUES (?, ?, ?)
            '''
            cursor.execute(sql, (name_ice, data_delivery, sepl))
            connection.commit()

        # Получение данных от пользователя и добавление в базу
        data_ice_cream = input_date()
        addendum_data(data_ice_cream)

        # Выполнение запроса SELECT для проверки данных
        cursor.execute('''
        SELECT * FROM Ice_cream
        ''')
        print(cursor.fetchall())

if __name__ == '__main__':
    main()