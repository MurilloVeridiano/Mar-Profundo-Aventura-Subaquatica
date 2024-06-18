from mysql.connector import connect, Error

def run_query(hosts, port, db_query, user, password):
    try:
        result_all = []
        for host in hosts:
            print(f'Host: {host}')
            print(f'Debug: username = {user}, password = {password}')  # Apenas para debug
            try:
                connection = connect(host=host, port=port, user=user, password=password, database='game')
                try:
                    with connection.cursor() as cursor:
                        res = cursor.execute(db_query, multi=True)
                        for result in res:
                            if result.with_rows:
                                print("Rows produced by statement '{}':".format(result.statement))
                                res_list = result.fetchall()
                                for row in res_list:
                                    print(row)
                                result_all.append(res_list)
                            else:
                                print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))
                    connection.commit()
                finally:
                    connection.close()
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
        return result_all
    except Error as e:
        print(f"Error running query: {e}")

def register_user(name, password):
    hosts = ['localhost']
    port = 3306
    user = 'user_game'
    pwd = '123'
    
    add_user_query = f"USE game; INSERT INTO score (name, hi_score, pass) VALUES ('{name}', 0, '{password}')"
    try:
        run_query(hosts, port, add_user_query, user, pwd)
    except Error as e:
        print(f"Erro: {e}")

def check_login(name, password):
    hosts = ['localhost']
    port = 3306
    user = 'user_game'
    pwd = '123'
    
    check_user_query = f"USE game; SELECT * FROM score WHERE name = '{name}' AND pass = '{password}'"
    result = run_query(hosts, port, check_user_query, user, pwd)
    if result and result[0]:
        return True
    else:
        return False

def update_hi_score(name, new_hi_score):
    hosts = ['localhost']
    port = 3306
    user = 'user_game'
    pwd = '123'
    db_query = f"USE game; UPDATE score SET hi_score = {new_hi_score} WHERE name = '{name}';"
    run_query(hosts, port, db_query, user, pwd)

def get_hi_score(name):
    hosts = ['localhost']
    port = 3306
    user = 'user_game'
    pwd = '123'
    db_query = f"USE game; SELECT hi_score FROM score WHERE name = '{name}';"
    result = run_query(hosts, port, db_query, user, pwd)
    if result and len(result) > 0 and len(result[0]) > 0:
        return result[0][0][0]
    else:
        return 0
