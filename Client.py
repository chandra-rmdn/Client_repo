from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from mysql import connector

app = Flask(__name__)

db = connector.connect(
    host ="localhost",
    user = "root",
    password = "",
    database = "db_barang"
)

if db.is_connected():
    print("MySQL Connected")



def check_item_exists(item_name):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM data_barang WHERE type = %s", (item_name,))
    count = cursor.fetchone()[0]
    cursor.close()
    print(f"Checking existence of {item_name}: {count}")
    return count

def check_unit_exists(unit_name):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM data_barang WHERE unit = %s", (unit_name,))
    count = cursor.fetchone()[0]
    cursor.close()
    print(f"Checking existence of unit {unit_name}: {count}")
    return count



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produk/')
def page_produk():
    # Mengambil semua produk untuk ditampilkan
    cursor = db.cursor()
    cursor.execute("SELECT * FROM data_barang")
    result = cursor.fetchall()
    cursor.close()

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
    cursor = db.cursor()
    cursor.execute("SELECT * FROM data_barang WHERE kode_barang = %s", (kode_barang,))
    result = cursor.fetchall()
    cursor.close()
    return render_template('item_page.html', hasil=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)