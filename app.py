from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Path to the CSV file
CSV_FILE = 'tasks.csv'

# Function to read tasks from CSV
def read_tasks():
    tasks = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
    return tasks

# Function to write tasks to CSV
def write_tasks(tasks):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['id', 'title', 'description', 'category', 'deadline', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

# Home route to display tasks
@app.route('/')
def index():
    tasks = read_tasks()
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        deadline = request.form['deadline']
        new_task = {
            'id': str(len(read_tasks()) + 1),  # Unique ID based on number of tasks
            'title': title,
            'description': description,
            'category': category,
            'deadline': deadline,
            'status': 'Pending'
        }
        tasks = read_tasks()
        tasks.append(new_task)
        write_tasks(tasks)
        return redirect(url_for('index'))
    return render_template('add_task.html')

# Route to edit an existing task
@app.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    tasks = read_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['category'] = request.form['category']
        task['deadline'] = request.form['deadline']
        write_tasks(tasks)
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

# Route to delete a task
@app.route('/delete/<task_id>')
def delete_task(task_id):
    tasks = read_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    write_tasks(tasks)
    return redirect(url_for('index'))

# Route to mark a task as completed
@app.route('/complete/<task_id>')
def complete_task(task_id):
    tasks = read_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = 'Completed'
        write_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Listen on all interfaces so Docker can route to it
    app.run(host='0.0.0.0', port=5000)

