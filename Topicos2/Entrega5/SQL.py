from getpass import getpass
from mysql.connector import connect, Error

def run_query(hosts, port, db_query):
    try:
        result_all = []
        for host in hosts:
            print(f'Host: {host}')
            username = "user_game"  # input("Enter username: ")
            password = "123"  # getpass("Enter password: ")
            print(f'Debug: username = {username}, password = {password}')  # Apenas para debug
            try:
                with connect(host=host, port=port, user=username, password=password) as connection:
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
                                print("Number of rows affected by statement '{}': {}".format(
                                    result.statement, result.rowcount))
                    connection.commit()
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
        return result_all
    except Error as e:
        print(f"Error running query: {e}")

def update_hi_score(new_hi_score):
    hosts = ['localhost']
    port = 3306
    db_query = f"USE game; UPDATE score SET hi_score = {new_hi_score} WHERE idscore = 1;"
    run_query(hosts, port, db_query)
