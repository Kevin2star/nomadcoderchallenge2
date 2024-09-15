from flask import Flask, render_template, request
from scraper import scrape_all

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']
        jobs = scrape_all(search_term)
        return render_template('index.html', jobs=jobs, search_term=search_term)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)