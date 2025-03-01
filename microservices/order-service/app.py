from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# YugabyteDB connection
conn = psycopg2.connect(
    host="yugabyte-ysql.yugabyte.svc.cluster.local",
    port=5433,
    user="yugabyte",
    password="password",
    dbname="yugabyte"
)

@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO orders (item, quantity) VALUES (%s, %s)",
                    (data['item'], data['quantity']))
        conn.commit()
    return jsonify({"message": "Order created!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
