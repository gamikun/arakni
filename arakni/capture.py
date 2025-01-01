from __future__ import print_function
import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect(user='postgres',
                        password='postgres',
                        database='Animalia')

def find_by_name(name):
    cursor = conn.cursor(cursor_factory=DictCursor)
    cursor.execute('select * from "Taxonomy" where name = %s',
                   (name, )
                   )
    return cursor.fetchone()

def insert_taxonomy(name, type, parent, is_extinct=False):
    cursor = conn.cursor(cursor_factory=DictCursor)
    try:
        cursor.execute("""
            insert into "Taxonomy"
            ("name", "type", "idSuper", "isExtinct")
            values (%s, %s, %s, %s)
        """, (name, type, parent, is_extinct, ))
        conn.commit()
    except:
        conn.rollback()
        raise

types_map = [
    'Nothing',
    'Kingdom',
    'Phylum',
    'Class',
    'Order',
    'Family',
    'Genus',
    'Specie',
]

while 1:
    try:
        print('1. Kingdom')
        print('2. Phylum')
        print('3. Class')
        print('4. Order')
        print('5. Family')
        print('6. Genus')
        print('7. Specie')
        tax_type = int(raw_input('Type: '))

        while 1:
            try:
                parent_name = raw_input('Parent name: ')
                if parent_name:
                    parent = find_by_name(parent_name)
                else:
                    print('No parent found')
                    parent = None

                print("Creating {}'s at {}".format(
                    types_map[tax_type],
                    parent_name,
                ))

                while 1:
                    try:
                        name = raw_input('Name: ')

                        if '†' in name:
                            name = name.replace('†', '')
                            is_extinct = True
                        else:
                            is_extinct = False

                        insert_taxonomy(name, tax_type, parent['id'],
                                        is_extinct=is_extinct
                                        )
                    except KeyboardInterrupt:
                        break
                    except psycopg2.IntegrityError:
                        print('taxonomy already exists')
            except KeyboardInterrupt:
                break

    except KeyboardInterrupt:
        break