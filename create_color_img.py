import sqlite3
from contextlib import contextmanager

@contextmanager
def db_conn(name_db):
    conn = sqlite3.connect(name_db)
    cur = conn.cursor()
    yield cur
    conn.commit()
    conn.close()
    
    
def select_all_colors():
    with db_conn('var.db') as cur:
        sqlite_select_query: str = '''
                SELECT *
                from color;
                '''
        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        return records

    
def create_img(list, path='images', img_format='png'):
    from PIL import Image
    for i in list:
        name, code, rgb = i[1], i[2], tuple(map(int, i[3].split(' ')))
        img = Image.new('RGB', (250, 250), rgb)
        img.save(f'{path}/{code}.{img_format}')
    print('ímages was saved success')

if __name__ == '__main__':
    create_img(select_all_colors())