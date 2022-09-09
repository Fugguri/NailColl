import random
from dotenv import load_dotenv
import sqlite3
from contextlib import contextmanager

load_dotenv()


@contextmanager
def db_conn(name_db):
    conn = sqlite3.connect(name_db)
    cur = conn.cursor()
    yield cur
    conn.commit()
    conn.close()


def create_list_of_var():
    with db_conn('var.db') as cur:
        cur.execute('''CREATE TABLE IF NOT EXISTS color(
                color_id INTEGER PRIMARY KEY autoincrement ,
                color_name text NOT NULL,
                color_code text NOT NULL,
                color_rgb text NOT NULL );
                ''')
        cur.execute('''CREATE TABLE IF NOT EXISTS design(
                design_id INTEGER PRIMARY KEY autoincrement ,
                design_name text NOT NULL);
                ''')
        cur.execute('''CREATE TABLE IF NOT EXISTS shape(
                shape_id INTEGER PRIMARY KEY autoincrement ,
                shape_name text);
                ''')
        cur.execute('''CREATE TABLE IF NOT EXISTS mat(
                mat_id INTEGER PRIMARY KEY autoincrement ,
                mat_name text);
                ''')
        '''создание структуры базы данных  '''


def save_user_data(file_direction='users.txt', command='massage.from_user'):
    import datetime
    now = datetime.datetime.now()
    with open(file_direction, 'a', encoding='utf-8') as userdata:
        t = command
        userdata.write(f'{str(t)}')
        userdata.write(now.strftime("%d-%m-%Y %H:%M"))
        userdata.write('''/n
        ''')
    '''Сохранение данных пользователей для дальнейшей работы с клиентами '''


def get_random(command='bot'):
    with open('variants/colors.txt', 'r') as color_variants, \
            open('variants/mat.txt', 'r') as mat_variants, \
            open('variants/design.txt', 'r') as design_variants:
        color_list = [i.split() for i in color_variants.readlines()]
        design_list = [i for i in design_variants.readlines()]
        mat_list = [i.strip() for i in mat_variants.readlines()]

    color = random.choice(color_list)
    design = random.choice(design_list)
    mat = random.choice(mat_list)
    if command == 'bot':
        return {'color': color, 'design': design, 'mat': mat, }
    elif command == 'db':
        return color_list
    '''первоначальный вариант реализации функции случайного выбора цвета
    command - внедрение возможности вызывать команду из ботаБ пока происходила перенесение данных в SQLite
    db - для вызова в коде базы данных 
    bot - для вызова из бота напрямую'''


def get_random_color(table, title='name'):
    '''
    :param table: указание таблицы откуда берутся данные.
    :param title: наименование значения, которое нужно получить - название цвета, код цвета или RGB код.
    :return: наименование или один из двух вариантов кодировки цвета. Стандартное при code, и RGB при запросе rgb.
    '''

    with db_conn('var.db') as cur:

        if table == 'color':
            sqlite_select_query = '''
            SELECT color_name,color_code,color_rgb
            from color
            order by random()
            limit 1;
            '''
            cur.execute(sqlite_select_query)
            records = cur.fetchall()
            if title == 'name':
                return records[0][0]
            elif title == 'code':
                return records[0][1]
            elif title == 'rgb':
                return records[0][2]
            elif title == 'all':
                return records[0]
            else:
                print('''Ошибка назначения введите один из 3х аргументов "name"- наименование цвета, "code" код цвета 
                или "rgb" для RGB кодировки ''')

        elif table == 'design':
            sqlite_select_query = '''SELECT design_name FROM design
            order by random()
            limit 1;'''
            cur.execute(sqlite_select_query)
            records = cur.fetchall()

            return records[0][0]
        elif table == 'mat':
            sqlite_select_query = '''SELECT mat_name FROM mat
                    order by random()
                    limit 1;'''
            cur.execute(sqlite_select_query)
            records = cur.fetchall()
            return records[0][0]


if __name__ == "__main__":
    get_random_color('design')
