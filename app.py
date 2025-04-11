from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clue1_sd8f987sdf76876sdf')
def clue1():
    return render_template('clue1.html')

@app.route('/clue2_s89d7f87sdf67876vv')
def clue2():
    return render_template('clue2.html')

@app.route('/clue3_poi45o6i4opi56pip4o56')
def clue3():
    return render_template('clue3.html')

@app.route('/clue4_mbnwb45mnbm4b5m3nb451')
def clue4():
    return render_template('clue4.html')

@app.route('/clue5_0x90s9df0s9df989sdf')
def clue5():
    return render_template('clue5.html')

@app.route('/clue6_m2m3n42n34mn23m4nm')
def clue6():
    return render_template('clue6.html')

@app.route('/clue7_kj2k3j4234jk23h4kjhj2')
def clue7():
    return render_template('clue7.html')

@app.route('/final_clue_9s0d890s809f8s90d8f')
def final_clue():
    return render_template('final-clue-1.html')

@app.route('/final_clue_mk23n4j23n4k2n3kj42j4545')
def final_clue2():
    return render_template('final-clue-2.html')

@app.route('/final_clue_kh4k5h34kj5h34jk5hkjhk34')
def final_clue3():
    return render_template('final-clue-3.html')

@app.route('/final_clue_sd098fs90d87f09sdf')
def final_clue4():
    return render_template('final-clue-4.html')

@app.route('/final_clue_asd098a0s98da90s8d')
def final_clue5():
    return render_template('final-clue-5.html')

@app.route('/final_clue_2i3l4kj2l3j4l23j4l')
def final_clue6():
    return render_template('final-clue-6.html')

@app.route('/final_clue_2klh34kj2h34jkh23') 
def final_clue7():
    return render_template('final-clue-7.html')

@app.route('/final_clue_sd098f09s8df09sd8f809sdf')
def final_clue8():
    return render_template('final-clue-8.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
