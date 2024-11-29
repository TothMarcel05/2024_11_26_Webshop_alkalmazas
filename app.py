from flask import Flask, render_template

app = Flask(__name__)



@app.route('/index', methods=["GET"])
def index():
    return render_template('add.html', adds=adds)

@app.route('/add', methods=["GET", "POST"])
def add_order():
    if request.method == 'POST':
        _name = request.form.get('name')
        _prize = request.form.get('prize')
        _category = request.form.get('category')
        add = {
            'name': _name,
            'prize': _prize,
            'category': _category}
        adds.append(add)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
