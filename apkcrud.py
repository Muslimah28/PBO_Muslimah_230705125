import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
     user= "root",
    password="",
    database="myDB"
)
cursor = connection.cursor()

def insert_data (connection) :
    name = input ("Masukkan Nama : ")
    address = input ("Masukkan Alamat ")
    cursor = connection.cursor()

    query = "INSERT INTO customers (name, address) VALUES ('"+name+"', '"+address+"')"
    cursor.execute(query) #menjalankan
    connection.commit() #menyimpan
    print ("{} Data Berhasil disimpan". format(cursor.rowcount))

def show_data(connection) :
    cursor = connection.cursor()
    sql = "SELECT *FROM customers"
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount < 0 :
        print ("Tidak ada data")
    else :
        for data in result :
            print(data)

def update_data (connection) :
    cursor = connection.cursor()
    show_data(connection)
    customer_id = input("Pilih id customer >")
    name = input ("Nama baru: ")
    address = input ("Alamat baru: ")

    sql = "UPDATE customers SET name = '"+name+"', address= '"+address+"' WHERE customer_id = '"+customer_id+"'"
    cursor.execute(sql)
    connection.commit()
    print("{}Data berhasil diubah".format(cursor.rowcount))

def delete_data (connection) :
    cursor = connection.cursor()
    show_data(connection)
    customer_id = input("pilih customer id yang ingin dihapus > ")
    sql = "DELETE FROM customers WHERE customer_id='"+customer_id+"'"
    cursor.execute(sql)
    connection.commit()
    print("{}Data berhasil dihapus".format(cursor.rowcount))
           
def search_data(connection) :
    cursor = connection.cursor()
    keyword = input ("kata kunci :")
    sql = "SELECT * FROM customers WHERE nama LIKE '"+"%{}%".format(keyword)+"' OR address LIKE '"+"%{}%".format(keyword)+"'"
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount < 0:
        print("tidak ada data")
    else:
        for data in result:
            print(data)

def show_menu(connection):
    print("=== app database python sederhana ===")
    print("1. insert data")
    print("2. show data")
    print("3. update data")
    print("4. delete data")
    print("5. search data")
    print("-------------------------------------")
   
    menu = input("select menu > ")

    if menu == "1":
        insert_data(connection)
    elif menu =="2":
        show_data(connection)
    elif menu =="3":
        update_data(connection)
    elif menu == "4":
        delete_data(connection)
    elif menu == "5":
        search_data(connection)
    elif menu == 0:
        exit()
    else:
        print("menu tidak tersedia")
        
if __name__ == "__main__":
    while(True) :
        show_menu (connection)