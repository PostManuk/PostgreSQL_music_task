import psycopg2
from passwordSQL import password1

conn= psycopg2.connect(database = "new_db", user = "postgres", password = password1)
with conn.cursor() as cur:
    #1 фукнция создания БД
    def create (cur):
        cur.execute("""
            DROP TABLE numbers;
            DROP TABLE clients;
            """)
                #создание таблиц
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
            phone_number VARCHAR (15);
            """)
        conn.commit()
        return f'База данных создана'

    #3Добавить номер телефона для клиента
    def insert_tel(cur, client_id, phone_number) :
        cur.execute("""
            INSERT INTO numbers( client_id, phone_number)
            VALUES (%s, %s);
            """, (client_id, phone_number))
        return ( f'Для клиента с  id - {client_id} Добавлен номер телефона-{phone_number}')



    #2 Добавить нового клиента
    def insert_client(cur, name=None, last_name=None, email=None, tel = None ):
        cur.execute("""
        	                INSERT INTO clients(name, last_name, email)
        	                VALUES (%s, %s, %s);
        	                """, (name, last_name, email))
        cur.execute("""
                SELECT id from clients
                ORDER BY id DESC
                LIMIT 1
                """)
        id = cur.fetchone()[0]
        if tel == None:
            return (f'Клиент {name} {last_name}  с мейлом {email} добавлен\n\t\t(Номер телефона не был указан)')
            # return id
        else :
            insert_tel (cur, id , tel)
            return (f'Клиент {name} {last_name}  с мейлом {email} \n\t\t Номер телефона - {tel} добавлен ')




    # 4 Функция, позволяющая изменить данные о клиенте.
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


    # 5 Функция, позволяющая удалить телефон для существующего клиента.
    def delete_phone(cur, phone_number):
        cur.execute("""
            DELETE FROM numbers
            WHERE phone_number = %s
            """, (phone_number,))
        return f'Номер телефона {phone_number} был удален'

    # 6 Функция, позволяющая удалить существующего клиента
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


    def find_client(cur, name=None,last_name=None, email=None, phone_number=None):
        if phone_number == None:
            cur.execute("""
            SELECT name,last_name,email FROM clients
            WHERE name LIKE '%s' OR last_name LIKE '%s' OR email LIKE '%s'
            """,(name,last_name,email,phone_number))
            return( name, last_name)


    #7 Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону
    def find_client(search):
        param_search=input('Введите один из параметров по которым будет производиться поиск :\n\tname\n\tlast_name\n\temail\n\ttel\n\t')
        search=input('Введите значение параметра: ')
        if param_search =='tel':
            cur.execute("""SELECT * FROM numbers
            WHERE phone_number=%s;""",(search,))
            id=cur.fetchone()[1]
            cur.execute("""SELECT * FROM clients
            WHERE id=%s;""",(id,))
            print(cur.fetchone())
        elif param_search=='name':
            cur.execute("""SELECT * FROM clients
            WHERE name=%s;""",(search,))
            print(cur.fetchall())
        elif param_search=='last_name':
            cur.execute("""SELECT * FROM clients
            WHERE last_name=%s;""",(search,))
            print(cur.fetchall())
        elif param_search=='email':
            cur.execute("""SELECT * FROM clients
            WHERE email=%s;""",(search,))
            print(cur.fetchall())
        else:
            print('Клиента с такими данными нет или данные введены некорректно')



    new_tel = insert_tel(cur, 1, '7788444')
    print(new_tel)
    client_Gary = insert_client(cur, 'Gary', 'Moore', 'stillgottheblues*mail.ru')
    client_Jimmy = insert_client(cur, 'Jimmy', 'Hendrix,', 'the_greatest_guitarist*mail.ru', '3937924')
    client_Chris = insert_client(cur, 'Chris', 'Rea', 'roadtohell*mail.ru', '112211')
    print(client_Gary)
    print(client_Jimmy)
    print(client_Chris)
    print()
    new_change1 = change_client(cur, 2, 'Janis', 'Joplin', 'mercedes*mail.ru')
    new_change2 = change_client(cur, 3, 'Chris', 'Rea', 'roadtohell*mail.ru', '111111')
    print(new_change1)
    print(new_change2)
    print()
    del_Jimmy_tel = delete_phone(cur,'3937924')
    print(del_Jimmy_tel)
    print()
    del_id = delete_client(cur, 2 )
    print(del_id)
    print()
    find_client('phone_number')


conn.close()










