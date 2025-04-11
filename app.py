from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clue1_sdfs9d8f7s98d7fs89d')
def clue1():
    return render_template('clue1.html')

@app.route('/clue2_sd98f7s89df798sd7f')
def clue2():
    return render_template('clue2.html')

@app.route('/clue3_mq3bmn4b23m4b2mn34bm')
def clue3():
    return render_template('clue3.html')

@app.route('/clue4_mn34b5mn3b45mnbmnb23423')
def clue4():
    return render_template('clue4.html')

@app.route('/clue5_zsd987s89d798s7df89s7df9')
def clue5():
    return render_template('clue5.html')

@app.route('/clue6_s98df798sd7f89sd7f66876sdf')
def clue6():
    return render_template('clue6.html')

@app.route('/clue7_3nmb45nb34mn5bmn345bnm')
def clue7():
    return render_template('clue7.html')

@app.route('/final_clue_xcv987xc89v798xc7v9')
def final_clue():
    return render_template('final-clue-1.html')

@app.route('/final_clue_mnbm2n3b4mn2b34mn2b3m4n')
def final_clue2():
    return render_template('final-clue-2.html')

@app.route('/final_clue_mnbw3mn4bnm34bmn23b4nm')
def final_clue3():
    return render_template('final-clue-3.html')

@app.route('/final_clue_zx7c6x876cx87c6v87xcv')
def final_clue4():
    return render_template('final-clue-4.html')

@app.route('/final_clue_mn23b4mn2b34n2b3m4')
def final_clue5():
    return render_template('final-clue-5.html')

@app.route('/final_clue_9x87c89x7cvq3478')
def final_clue6():
    return render_template('final-clue-6.html')

@app.route('/final_clue_mne4b5n3b4n53b4nm5b3m') 
def final_clue7():
    return render_template('final-clue-7.html')

@app.route('/final_clue_mnbqnb34mnb34mn2b3n4')
def final_clue8():
    return render_template('final-clue-8.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
