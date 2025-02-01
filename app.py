from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Fixed admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

# In-memory data for students and teachers (for simplicity, replace with a database in real applications)
students = []
teachers = []

@app.route('/')
def index():
    return render_template('index.html')  # The homepage

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the entered credentials match the fixed admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for('admin_dashboard'))  # Redirect to the admin dashboard
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')  # Login page template

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', students=students, teachers=teachers)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']
        subject = request.form['subject']

        # Add the student to the list
        students.append({'name': name, 'roll_number': roll_number, 'subject': subject})
        flash(f'Student {name} added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('add_student.html')

@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        teacher_id = request.form['teacher_id']
        subject = request.form['subject']

        # Add the teacher to the list
        teachers.append({'name': name, 'teacher_id': teacher_id, 'subject': subject})
        flash(f'Teacher {name} added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('add_teacher.html')

if __name__ == '__main__':
    app.run(debug=True)
