import sqlite3
from contextlib import contextmanager


@contextmanager
def db_conn(name_db):
    conn = sqlite3.connect(name_db)
    cur = conn.cursor()
    yield cur
    conn.commit()
    conn.close()


def get_random_color(table, title='name'):
    """
    :param table: указание таблицы откуда берутся данные.
    :param title: наименование значения, которое нужно получить - название цвета, код цвета или RGB код.
    :return: наименование или один из двух вариантов кодировки цвета. Стандартное при code, и RGB при запросе rgb.
    """

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


def get_random_design():
    with db_conn('var.db') as cur:
        sqlite_select_query = '''SELECT design_name FROM design
            order by random()
            limit 1;'''
        cur.execute(sqlite_select_query)
        records = cur.fetchall()

        return records[0][0]


def get_random_mat():
    with db_conn('var.db') as cur:
        sqlite_select_query = '''SELECT mat_name FROM mat
                            order by random()
                            limit 1;'''
        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        return records[0][0]


if __name__ == "__main__":
    get_random_color('design')
