from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


products = [
    {"name": "Laptop", "prize": 250000, "category": "Elektronika"},
    {"name": "Fotel", "prize": 50000, "category": "Bútor"},
    {"name": "Okosóra", "prize": 75000, "category": "Elektronika"},
]

adds = products.copy()

@app.route('/', methods=["GET"])
def basic():
    return render_template('index.html', adds=adds) 

@app.route('/add', methods=["GET", "POST"])
def add_order():
    if request.method == 'POST':
        _name = request.form.get('name')
        _prize = request.form.get('prize')
        _category = request.form.get('category')

        if _name and _prize and _category: 
            new_product = {
                'name': _name,
                'prize': int(_prize),
                'category': _category
            }
            adds.append(new_product)  

        return redirect(url_for('basic'))  
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
