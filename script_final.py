import psycopg2
import configparser
import pandas as pd
from zapytania_sql import *

def create_database():
    '''
    - Tworzy i łączy się z bazą danych sales_data
    - Zwraca połączenie i kursor do bazy danych sales_data
    '''
    # Read the parameters from the config file
    config = configparser.ConfigParser()
    config.read('private.cfg')
    DB_NAME_DEFAULT = config.get('SQL', 'DB_NAME_DEFAULT')
    DB_USER = config.get('SQL', 'DB_USER')
    DB_PASSWORD = config.get('SQL', 'DB_PASSWORD')
    
    # Connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname={} user={} password={}".format(DB_NAME_DEFAULT, DB_USER, DB_PASSWORD))
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # Create sales_data database
    cur.execute('DROP DATABASE IF EXISTS sales_data')
    cur.execute("CREATE DATABASE sales_data WITH ENCODING 'utf8' TEMPLATE template0")
    
    # Close connection to default database
    conn.close()
    
    # Connect to sales_data database
    conn = psycopg2.connect('host=127.0.0.1 dbname=sales_data user={} password={}'.format(DB_USER, DB_PASSWORD))
    cur = conn.cursor()
    
    return cur, conn

def drop_table(cur, conn):
    '''
    - Usunięcie tabeli orders jeśli już wcześniej była utworzona
    '''
    cur.execute(drop_orders_table)
    conn.commit()

def create_table(cur, conn):
    '''
    - Stworzenie tabeli orders
    '''
    cur.execute(create_orders_table)
    conn.commit()

def insert_table(cur, conn):
    '''
    - Wypełnienie wartości tabeli orders z pliku sales_data_sample.csv
    '''
    df = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE']).dt.date
    for i, row in df.iterrows():
        cur.execute(insert_orders_table, row.tolist())
        conn.commit()

def main():
    '''
    - Usuwa (jeśli istnieje) i tworzy bazę danych sales_data
    - Nawiązuje połączenie i ustawia na nim kursor
    - Usuwa tabelę orders (jeśli już istnieje)
    - Tworzy tabelę orders
    - Wypełnia wartości tabeli orders z pliku sales_data_sample.csv
    - Zamyka połączenie z bazą danych
    '''
    cur, conn = create_database()
    
    drop_table(cur, conn)
    create_table(cur, conn)
    insert_table(cur, conn)
    
    conn.close()
    
# Wywołuje funkcję main() tylko wtedy, gdy ten plik jest uruchamiany jako główny skrypt, a nie importowany jako moduł.
if __name__ == '__main__':
    main()

    
    