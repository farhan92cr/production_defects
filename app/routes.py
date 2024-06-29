# routes.py

from flask import render_template, request, redirect, url_for, session, flash
from app import app, mongo
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from bson.objectid import ObjectId

app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('dashboard'))
        
        flash('Invalid credentials')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_defect', methods=['GET', 'POST'])
def add_defect():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        model = request.form.get('model')
        if model == 'other':
            model = request.form.get('other_model')

        defect_type = request.form.get('defect_type')
        if defect_type == 'other':
            defect_type = request.form.get('other_defect')

        imei = request.form.get('imei')
        line = request.form.get('line')
        entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        existing_defect = mongo.db.defects.find_one({'imei': imei})
        if existing_defect:
            flash('IMEI already exists')
            return redirect(url_for('dashboard'))

        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join('app/static/images', filename)
            
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            image.save(image_path)
        else:
            filename = None

        defect = {
            'model': model,
            'defect_type': defect_type,
            'imei': imei,
            'line': line,
            'entry_time': entry_time,
            'image': filename
        }

        mongo.db.defects.insert_one(defect)
        flash('Defect added successfully')
        return redirect(url_for('dashboard'))
    
    return render_template('add_defect.html')

@app.route('/all_defects', methods=['GET'])
def all_defects():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    defects = mongo.db.defects.find()
    return render_template('all_defects.html', defects=defects, str=str)

@app.route('/delete_defect/<id>', methods=['GET'])
def delete_defect(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    mongo.db.defects.delete_one({'_id': ObjectId(id)})
    flash('Defect deleted successfully')
    return redirect(url_for('all_defects'))

@app.route('/search_defect', methods=['GET', 'POST'])
def search_defect():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        imei = request.form.get('imei')
        defect = mongo.db.defects.find_one({'imei': imei})
        if defect:
            return render_template('search_result.html', defect=defect, str=str)
        flash('Defect not found')
        return redirect(url_for('search_defect'))
    
    return render_template('search_defect.html')


