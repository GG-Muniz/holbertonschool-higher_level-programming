#!/usr/bin/env python3
"""
Task 03: Displaying Data from JSON or CSV Files in Flask
"""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_data():
    """Read data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_data():
    """Read data from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
        return products
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Items page route with dynamic content from JSON"""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    except json.JSONDecodeError:
        items_list = []
    
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    """Products page route with source parameter handling"""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    # Filter by ID if provided
    if product_id:
        filtered_products = [p for p in products_data if str(p.get('id', '')) == str(product_id)]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        products_data = filtered_products
    
    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 