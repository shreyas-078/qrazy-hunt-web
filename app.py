from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clue1')
def clue1():
    return render_template('clue1.html')

@app.route('/clue2')
def clue2():
    return render_template('clue2.html')

@app.route('/clue3')
def clue3():
    return render_template('clue3.html')

@app.route('/clue4')
def clue4():
    return render_template('clue4.html')

@app.route('/clue5')
def clue5():
    return render_template('clue5.html')

@app.route('/clue6')
def clue6():
    return render_template('clue6.html')

@app.route('/clue7')
def clue7():
    return render_template('clue7.html')

@app.route('/final_clue_1')
def final_clue():
    return render_template('final-clue-1.html')

@app.route('/final_clue_2')
def final_clue2():
    return render_template('final-clue-2.html')

@app.route('/final_clue_3')
def final_clue3():
    return render_template('final-clue-3.html')

@app.route('/final_clue_4')
def final_clue4():
    return render_template('final-clue-4.html')

@app.route('/final_clue_5')
def final_clue5():
    return render_template('final-clue-5.html')

@app.route('/final_clue_6')
def final_clue6():
    return render_template('final-clue-6.html')

@app.route('/final_clue_7') 
def final_clue7():
    return render_template('final-clue-7.html')

@app.route('/final_clue_8')
def final_clue8():
    return render_template('final-clue-8.html')

app.run(debug=True, host="0.0.0.0", port=5100)
