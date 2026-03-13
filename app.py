import sqlite3
import json
import requests
from flask import Flask, render_template, request, jsonify
from menu_data import MENU_CATEGORIES

app = Flask(__name__)

# Telegram config
TELEGRAM_BOT_TOKEN = "8606492601:AAFT14Mmb3_KoLNZTtL7hBSOZmiy409M9Ac"
TELEGRAM_CHAT_ID = "-1003507803840"

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            customer_phone TEXT,
            items TEXT NOT NULL,
            total_price INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Check if we need to add new columns to an existing table
    cursor.execute("PRAGMA table_info(orders)")
    columns = [info[1] for info in cursor.fetchall()]
    if 'customer_name' not in columns:
        cursor.execute("ALTER TABLE orders ADD COLUMN customer_name TEXT")
    if 'customer_phone' not in columns:
        cursor.execute("ALTER TABLE orders ADD COLUMN customer_phone TEXT")
        
    conn.commit()
    conn.close()

init_db()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/menu')
def menu():
    return render_template('menu.html', categories=MENU_CATEGORIES)


@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.json
    cart = data.get('cart', [])
    customer_name = data.get('name', 'Не указано')
    customer_phone = data.get('phone', 'Не указано')
    
    if not cart:
        return jsonify({"success": False, "error": "Корзина пуста"}), 400
        
    total_price = sum(item['price'] * item['qty'] for item in cart)
    
    # Save to SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (customer_name, customer_phone, items, total_price) VALUES (?, ?, ?, ?)', 
                  (customer_name, customer_phone, json.dumps(cart, ensure_ascii=False), total_price))
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    
    from datetime import datetime
    import pytz
    
    tz = pytz.timezone('Asia/Bishkek')
    current_time = datetime.now(tz).strftime('%d.%m.%Y %H:%M')
    
    # Send to Telegram
    message_text = f"🔥 <b>Новый заказ #{order_id}</b>\n"
    message_text += f"🕒 <b>Время:</b> {current_time}\n\n"
    message_text += f"👤 <b>Клиент:</b> {customer_name}\n"
    message_text += f"📞 <b>Телефон:</b> {customer_phone}\n\n"
    message_text += f"🛒 <b>Корзина:</b>\n"
    for item in cart:
        message_text += f"▪️ {item['title']} - {item['qty']} шт. ({item['price'] * item['qty']} сом)\n"
    message_text += f"\n💰 <b>Итого: {total_price} сом</b>"
    
    try:
        tg_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(tg_url, json={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message_text,
            "parse_mode": "HTML"
        })
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
        
    return jsonify({"success": True, "order_id": order_id})



if __name__ == '__main__':
    app.run(debug=True)
