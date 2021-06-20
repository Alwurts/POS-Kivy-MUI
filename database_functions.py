import psycopg2
import datetime

def get_password_with_name(name):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE user_name = '" + name + "';")
    tempTuple =cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return(tempTuple[0])


def get_users():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT user_name FROM users")
    tempTuple =cur.fetchall()
    temp=[]
    for x in tempTuple:
        temp.append(x[0])
    conn.commit()
    cur.close()
    conn.close()
    return temp

def sell_ice_block (quantity_sold, price, sold_by, client = 'unknown'):
    conn = connect_to_database()
    cur = conn.cursor()

    x = datetime.datetime.now()
    time_sale=(str(x)[:19])

    sql = """INSERT INTO ice_block_sales(quantity_sold, price, time_sale, client, sold_by)
             VALUES(""" + str(quantity_sold) + "," + str(price) + ",'" + str(time_sale) + "','" + str(client) + "','" + str(sold_by) + """');"""
    cur.execute(sql)
    '''
    cur.execute("""INSERT INTO ice_block_sales(quantity_sold, price, time_sale, sold_by)
                    VALUES (1.5, 160, '2021-06-16 20:39:17', 'Alwurts');""")
 
    '''
    conn.commit()
    cur.close()
    conn.close()

def get_items():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT time_sale,product,quantity_sold,amount_paid FROM sales_public")
    tempTuple =cur.fetchall()
    tempTuple = list(tempTuple)
    temp = []
    for i, row in enumerate (tempTuple,start=0):
        temp_x=[]
        temp_x.append( convert_date(tempTuple[i][0]))
        temp_x.append( tempTuple[i][1])
        temp_x.append( tempTuple[i][2])
        temp_x.append( tempTuple[i][3])
        temp.append(temp_x)

    conn.commit()
    cur.close()
    conn.close()
    return temp

def sell_item (product,quantity_sold, price, sold_by, client = 'unknown'):
    conn = connect_to_database()
    cur = conn.cursor()

    time_sale = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #time_sale=(str(x)[:19])

    sql = """INSERT INTO sales_public(product,quantity_sold, amount_paid, time_sale, sold_to, sold_by)
             VALUES('"""+ str(product) + "'," + str(quantity_sold) + "," + str(price) + ",'" + str(time_sale) + "','" + str(client) + "','" + str(sold_by) + """');"""
    cur.execute(sql)
    
    conn.commit()
    cur.close()
    conn.close()
    

def connect_to_database():
    try:
        conn = psycopg2.connect(
        host="purificadora-dev.cn6lcx4t4zk6.us-east-2.rds.amazonaws.com",
        database="purificadora",
        user="purificadora_dev",
        password="Purificadora2021")    
        return conn
    except:
        print ("I am unable to connect to the database")

def convert_date(date):
    temp_date_now = datetime.datetime.now()
    delta = temp_date_now - date
    if delta.days > 0: # Return days
        return str(delta.days) + " Days ago"

    else:

        temp_minutes = delta.seconds / 60
        if temp_minutes > 59: # Return Hours
            temp_hours = temp_minutes / 60
            if temp_hours > 1:
                temp_text = "Hours"
            else:
                temp_text = "Hour"
            return str(int(temp_hours)) + " " + temp_text + " ago"
        elif (temp_minutes<1):
            if delta.seconds > 1:
                temp_text = "Seconds"
            else:
                temp_text = "Second"
            return str(int(delta.seconds)) + " " + temp_text + " ago"
        else:
            if temp_minutes > 1:
                temp_text = "Minutes"
            else:
                temp_text = "Minute"
            return str(int(temp_minutes)) + " " + temp_text + " ago"

if __name__ == '__main__':
    '''
    quantity_sold = 10
    price = 160

    sold_by = 'JaiW'
    sell_item("ice block",quantity_sold, price, sold_by)
    print(datetime.datetime(2021,6,19,16,11,51))
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    '''
    temp = get_items()
    print(temp)
    
    

    