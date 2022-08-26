import random
from dotenv import load_dotenv
import datetime
import sqlite3
load_dotenv()
now = datetime.datetime.now()


def create_list_of_var():
    VARIANTS = sqlite3.connect('var.db')  # Соединение с базой данных для дальнейшего обращения к ней в функциях
    cur = VARIANTS.cursor()  # Текущее положение курсора в базе данных
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
    VARIANTS.commit()
    VARIANTS.close()
    '''создание структуры базы данных  '''


def save_user_data(file_direction='variants/users.txt', command='massage.from_user'):
    with open(file_direction, 'a', encoding='utf-8') as userdata:
        t = command
        userdata.write(f'{str(t)}')
        userdata.write(now.strftime("%d-%m-%Y %H:%M"))
        userdata.write('''
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


def get_random_v2(table, title='name'):
    VARIANTS = sqlite3.connect('var.db')  # Соединение с базой данных для дальнейшего обращения к ней в функциях

    cur = VARIANTS.cursor()  # Текущее положение курсора в базе данных

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
            print()
            return records[0][0]
        if title == 'code':
            return records[0][1]
        if title == 'rgb':
            return records[0][2]
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

    VARIANTS.close()

    '''table - название таблицы, из которой будут браться значение. title - введен пока только для таблицы цветовБ чтобы была возможность получать отдельно 
    названия цветов, код цвета в таблице RGB и в общей классификации '''


if __name__ == "__main__":
    get_random_v2('design')


# def update_var_color():
#     for i in get_random('db'):
#         name_color = ' '.join(i[:-4])
#         color_code = ''.join(i[-4])
#         color_rgb = ' '.join(i[-3:])
#         data = (name_color, color_code, color_rgb)
#         cur.execute("INSERT INTO color(color_name,color_code,color_rgb) VALUES( ?, ?, ?);", data)
#         VARIANTS.commit()
#     '''Перевод вариантов из текстового документа для упрощения работы бота '''
# def update_var_design():
#     with open('variants/design.txt', 'r') as design_variants:
#         design_list = [(i.replace('\n', '')) for i in design_variants.readlines()]
#         for i in design_list:
#             now = (i,)
#             cur.execute("INSERT INTO design(design_name) VALUES(?);", now)
#             VARIANTS.commit()
#     '''Перевод вариантов из текстового документа в базу данных для упрощения работы бота '''
# def clear_bugs():
#     cur.execute('delete from design   ')
#     VARIANTS.commit()
#     '''Временная функция для очистки проблемных/некорректных данных '''
