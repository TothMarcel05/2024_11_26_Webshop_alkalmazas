from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tabla')
def tabla():
    plants = [
        {"name": "Monstera", "type": "Szobanövény", "feature": "Nagyméretű levelek"},
        {"name": "Bambusz", "type": "Dísznövény", "feature": "Gyors növekedés"},
        {"name": "Kaktusz", "type": "Pozsgás", "feature": "Szárazságtűrő"}
    ]
    return render_template('tabla.html', plants=plants)

if __name__ == '__main__':
    app.run(debug=True)
