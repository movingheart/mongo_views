from settings import MYSQL_KW
import MySQLdb


def conn_mysql(**kwargs):
    conn = MySQLdb.connect(**kwargs)
    return conn


def get_data(sql, **kwargs):
    conn = conn_mysql(**kwargs)
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    num = cur.execute(sql)
    results = cur.fetchall()
    return results


if __name__ == "__main__":
    sql = "SELECT * FROM `handle_mongo` GROUP BY mongo_base,mongo_col;"
    data = get_data(sql, **MYSQL_KW)
    print data
