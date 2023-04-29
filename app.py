from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_items = []

@app.route('/')
def index():
    return render_template('index.html', todo_items=todo_items)

@app.route('/add', methods=['POST'])
def add():
    text = request.form['text']
    todo_items.append(text)
    return redirect(url_for('index'))

@app.route('/toggle/<int:index>')
def toggle(index):
    todo_items[index] = f'<del>{todo_items[index]}</del>'
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    del todo_items[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
