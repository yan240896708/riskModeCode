import MySQLdb

db = MySQLdb.connect("121.196.219.74", "root", "toor", "ombp_dev", charset='utf8')

cursor = db.cursor()

cursor.execute("select Y from z_risk_mode")

item = cursor.fetchall()

a = []
for (row,) in item:

    a.append(int(row))

db.close()




def getlist1(x):
    db = MySQLdb.connect("121.196.219.74", "root", "toor", "ombp_dev", charset='utf8')

    cursor = db.cursor()

    cursor.execute("select " + x + " from z_risk_mode order by " + x)

    item = cursor.fetchall()

    a = []
    for (row,) in item:
        a.append(row)

    db.close()
    return a


def getlist2(x):
    db = MySQLdb.connect("121.196.219.74", "root", "toor", "ombp_dev", charset='utf8')

    cursor = db.cursor()

    cursor.execute("select Y from z_risk_mode order by " + x)

    item = cursor.fetchall()

    a = []
    for (row,) in item:
        a.append(int(row))

    db.close()

    return a

