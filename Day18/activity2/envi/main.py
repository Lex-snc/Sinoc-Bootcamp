from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database configuration for XAMPP MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',  # Default XAMPP MySQL user
    'password': '',   # Default XAMPP MySQL password (update if set)
    'database': 'pharmacy_management'
}

# Function to get database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        return None

# Route 1: List Medicines with Supplier Details (GET /medicines/suppliers)
@app.route('/medicines/suppliers', methods=['GET'])
def list_medicines_with_suppliers():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT 
        m.med_id,
        m.medicine_name,
        m.unit_price,
        m.stock_quantity,
        m.date_of_expiration,
        s.supp_name,
        s.supp_phone
    FROM 
        medicines m
    INNER JOIN 
        suppliers s ON m.supplier_id = s.supplier_id
    """
    cursor.execute(query)
    medicines = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify({'medicines': medicines}), 200

# Route 2: List Customers with Their Prescriptions (GET /customers/prescriptions)
@app.route('/customers/prescriptions', methods=['GET'])
def list_customers_with_prescriptions():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT 
        c.customer_id,
        c.first_name,
        c.last_name,
        p.prescription_id,
        p.quantity,
        p.prescription_date,
        m.medicine_name
    FROM 
        customers c
    LEFT JOIN 
        prescriptions p ON c.customer_id = p.customer_id
    LEFT JOIN 
        medicines m ON p.med_id = m.med_id
    """
    cursor.execute(query)
    customers = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify({'customers': customers}), 200

# Route 3: List Medicines and Their Prescription Counts (GET /medicines/prescription-counts)
@app.route('/medicines/prescription-counts', methods=['GET'])
def list_medicines_prescription_counts():
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT 
        m.med_id,
        m.medicine_name,
        m.stock_quantity,
        COUNT(p.prescription_id) AS prescription_count
    FROM 
        medicines m
    LEFT JOIN 
        prescriptions p ON m.med_id = p.med_id
    GROUP BY 
        m.med_id, m.medicine_name, m.stock_quantity
    """
    cursor.execute(query)
    medicines = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify({'medicines': medicines}), 200

if __name__ == '__main__':
    app.run(debug=True)