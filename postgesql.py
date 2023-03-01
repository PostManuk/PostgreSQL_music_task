import psycopg2
from passwordSQL import password1

def del_bd(cur):
        cur.execute("""
        DROP TABLE IF EXISTS numbers;
        DROP TABLE IF EXISTS clients;
        """)
        conn.commit()
        return print ("База данных удалена")

def create(cur):
    cur.execute("""
            CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            last_name VARCHAR (30) NOT NULL,
            email VARCHAR (128) NOT NULL );
            """)
    cur.execute("""
            CREATE TABLE IF NOT EXISTS numbers(
            id SERIAL PRIMARY KEY,
            client_id INTEGER NOT NULL REFERENCES clients(id),
            phone_number VARCHAR (15));
            """)
    conn.commit()
    return print('База данных создана')

def insert_tel(cur, client_id, tel):
    cur.execute("""
            INSERT INTO numbers( client_id, phone_number)
            VALUES (%s, %s);
            """, (client_id, tel))
    return ( f'Для клиента с  id - {client_id} Добавлен номер телефона-{tel}')

def insert_client(cur, name=None, last_name=None, email=None, tel= None ):
    cur.execute("""
        INSERT INTO clients( name, last_name, email)
        VALUES (%s, %s, %s);
        """, (name, last_name, email))
    cur.execute("""
        SELECT id from clients
        ORDER BY id DESC
        LIMIT 4
        """)
    id = cur.fetchone()[0]
    if tel == None:
        return f'Клиент {name} {last_name}  с мейлом {email} добавлен\n\t\t(Номер телефона не был указан)'
    else:
        insert_tel (cur, id , tel)
        return (f'Клиент {name} {last_name}  с мейлом {email} \n\t\t Номер телефона - {tel} добавлен ')

def change_client(cur, id, name, last_name, email, phone_number=None):
    cur.execute("""
        UPDATE clients
        SET name = %s, last_name = %s, email =%s
        where id = %s;
        """, (name, last_name, email, id))
    if phone_number == None:
        return f'Для владельца  с номером  id-{id} внесены следующие изменения' \
                f'\n\tИмя: {name}\n\tФамилия: {last_name}\n\tМейл: {email}\n\tНомер телефона не был изменен'
    else:
        cur.execute("""
            UPDATE numbers
            SET phone_number = %s
            where client_id = %s;
            """, (phone_number, id))
        return f'Для владельца  с номером  id-{id} внесены следующие изменения' \
                f'\n\tИмя: {name}\n\tФамилия: {last_name}\n\tМейл: {email}\n\tНомер телефона: {phone_number}'

def find_client(cur, name=None, surname=None, email=None, tel=None):
    if name is None:
        name = '%'
    else:
        name = '%' + name + '%'
    if surname is None:
        surname = '%'
    else:
        surname = '%' + surname + '%'
    if email is None:
        email = '%'
    else:
        email = '%' + email + '%'
    if tel is None:
        cur.execute("""
                SELECT c.id, c.name, c.last_name, c.email, n.phone_number FROM clients c
                LEFT JOIN numbers n c.id = n.client_id
                WHERE c.name LIKE %s AND c.lastname LIKE %s
                AND c.email LIKE %s
                """, (name, surname, email))
    else:
        cur.execute("""
                SELECT c.id, c.name, c.last_name, c.email, n.phone_number FROM clients c
                LEFT JOIN numbers n ON c.id = n.client_id
                WHERE c.name LIKE %s AND c.last_name LIKE %s
                AND c.email LIKE %s AND n.phone_number like %s
                """, (name, surname, email, tel))
    print('Данные о клиенте по параметрам поиска:')
    return cur.fetchall()

def delete_phone(cur, phone_number):
    cur.execute("""
        DELETE FROM numbers
        WHERE phone_number = %s
        """, (phone_number,))
    return f'Номер телефона {phone_number} был удален'

def delete_client(cur, id):
    cur.execute("""
        DELETE FROM numbers
        WHERE client_id = %s
        """, (id,))
    cur.execute("""
        DELETE FROM clients
        WHERE id = %s
        """, (id,))
    return  f'Владелец с id {id} был удален'

conn= psycopg2.connect(database="tel1", user="postgres", password=password1 )
with conn.cursor() as cur:
    del_bd(cur)
    create(cur)
    print()
    client_Gary = insert_client(cur, 'Gary', 'Moore', 'stillgottheblues*mail.ru')
    client_Chris = insert_client(cur, 'Chris', 'Rea', 'roadtohell*mail.ru', '112211')
    print(client_Gary)
    print()
    client_Jimmy = insert_client(cur, 'Jimmy', 'Hendrix,', 'the_greatest_guitarist*mail.ru', '3937924')
    print(client_Jimmy)
    print()
    new_tel = insert_tel(cur, 1, '7788444')
    print(new_tel)
    print()
    find_Jimmy = find_client(cur, 'Jimmy', 'Hendrix,', 'the_greatest_guitarist*mail.ru', '3937924')
    print(find_Jimmy)
    print()
    new_change2 = change_client(cur, 3, 'Chris', 'Rea', 'roadtohell*mail.ru', '111111')
    find_Chris = change_client(cur, 3, 'Chris', 'Rea', 'roadtohell*mail.ru', '111111')
    print(find_Chris)
    print()
    print(new_change2)
    del_Jimmy_tel = delete_phone(cur, '3937924')
    print(del_Jimmy_tel)
    print()
    del_id = delete_client(cur, 2)
    print(del_id)
    print()

conn.close()