import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import Error

app = Flask(__name__)

def get_connection():
    try: 
        connection = mysql.connector.connect(
            host = "tlw44.h.filess.io",
            database = "DataProduk_mineralsis",
            port = "3307",
            user = "DataProduk_mineralsis",
            password = "66d5729d92ed1cad20b08d72d53e271810fc25b2"
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

try:
    connection = get_connection()
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

def check_item_exists(item_name):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM data_barang WHERE type = %s", (item_name,))
            count = cursor.fetchone()[0]
        except Error as e:
            print("Error while deleting data:", e)
        finally:
            cursor.close()
            connection.close()
    return count

def check_unit_exists(unit_name):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM data_barang WHERE unit = %s", (unit_name,))
            count = cursor.fetchone()[0]
        except Error as e:
            print("Error while deleting data:", e)
        finally:
            cursor.close()
            connection.close()
    return count


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produk/')
def page_produk():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM data_barang")
            result = cursor.fetchall()

            # Memeriksa keberadaan setiap item
            samsung_exists = check_item_exists('Samsung')
            iphone_exists = check_item_exists('iPhone')
            oppo_exists = check_item_exists('Oppo')
            vivo_exists = check_item_exists('Vivo')
            xiaomi_exists = check_item_exists('Xiaomi')

            # Memeriksa keberadaan setiap unit
            smartphone_exists = check_unit_exists('Smartphone')
            case_exists = check_unit_exists('Case')
            charger_exists = check_unit_exists('Charger')
            tempered_exists = check_unit_exists('Tempered Glass')
        except Error as e:
            print("Error while deleting data:", e)
        finally:
            cursor.close()
            connection.close()

    return render_template('produk_page.html', 
                           hasil=result,
                           samsung_exists=samsung_exists, 
                           iphone_exists=iphone_exists, 
                           oppo_exists=oppo_exists, 
                           vivo_exists=vivo_exists, 
                           xiaomi_exists=xiaomi_exists,
                           smartphone_exists=smartphone_exists,
                           case_exists = case_exists,
                           charger_exists = charger_exists,
                           tempered_exists = tempered_exists)

@app.route('/item/<kode_barang>' , methods=['GET'])
def page_item(kode_barang):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM data_barang WHERE kode_barang = %s", (kode_barang,))
            result = cursor.fetchall()
        except Error as e:
            print("Error while deleting data:", e)
        finally:
            cursor.close()
            connection.close()
    return render_template('item_page.html', hasil=result)

if __name__ == "__main__":
    app.run(debug=True)