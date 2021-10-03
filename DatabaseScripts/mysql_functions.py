"""
MySQL Functions for Python
Updated 10/3/2021
"""

import mysql.connector


def connect_to_db(host, user, password, database, port):
    """
    :config: Dict containing
    :return: connection, cursor
    """

    conn = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
    return conn, conn.cursor()


def reconnect_to_db(conn, cursor, attempts=10, delay=1):
    """
    Tries to reconnect conn to db :attempts: number of times if disconnected (timed out).
    Otherwise returns original conn and cursor."""

    if not conn.is_connected():
        conn.reconnect(attempts=attempts, delay=delay)
        return conn, conn.cursor()
    else:
        return conn, cursor


def get_column_names(cursor, table_name):
    """Returns list of column names in table."""

    cursor.execute(f"SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` where `TABLE_NAME`='{table_name}';")
    columns = [row[0] for row in cursor.fetchall()]
    return columns


def get_db_table_data(cursor, table_name, fields, where='true'):
    """
    :param cursor: mysql.connector.connect().cursor() object
    :param table_name: string
    :param fields: list or tuple, ['field1', 'field2', ...]
    :param where: string, MySQL where clause, selects all rows by default
    :return: cursor.fetchall(), [(data1, data2), ...] list of rows (tuples) of data
    """

    cursor.execute(f'SELECT {", ".join(fields)} FROM {table_name} WHERE {where};')
    return cursor.fetchall()


def dicts_to_insert_query(dicts, table_name: str, query_lang=1):
    """
    :param dicts: list of dicts, all dicts must have the same keys (column names)
    :param table_name:
    :param query_lang:
    :return:
    """

    if isinstance(dicts, dict):  # If dict is provided instead of list of dicts, convert to list
        dicts = [dicts]

    values_str = ''
    for row in dicts:
        if len(row) == 0:  # If dict is empty, skip
            continue

        # Alphabetize to organize all dicts into same order for a single insert query
        d = dict( [(key, row[key]) for key in sorted(row)] )

        dict_values = str(tuple(d.values()))
        values_str += dict_values + ', '

        if len(d) == 1:  # If only one element in row
            # Remove ',' after element inside tuple
            values_str = values_str[:-4] + values_str[-3:]

    if not values_str:  # If all the dicts are empty
        return ''  # Executing '' does not cause MySQL error

    column_quote = '`'

    dict_keys = [column_quote + key + column_quote for key in d.keys()]
    col_names = ', '.join(dict_keys)

    values_str = values_str[:-2].replace('None', 'null')  # Replace all NoneTypes with null value

    query = f"""INSERT INTO {table_name} ({col_names}) VALUES {values_str};"""
    return query
