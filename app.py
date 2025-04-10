from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clue1_a23uhfbc23kjash45eu1')
def clue1():
    return render_template('clue1.html')

@app.route('/clue2_18346hhghsauhtg23h4')
def clue2():
    return render_template('clue2.html')

@app.route('/clue3_1h23jkhg23kjh23k4')
def clue3():
    return render_template('clue3.html')

@app.route('/clue4_23uy4g23hjk4g245jg')
def clue4():
    return render_template('clue4.html')

@app.route('/clue5_23h4g23h4g23h4g23')
def clue5():
    return render_template('clue5.html')

@app.route('/clue6_78347sjdhfgsjdhg7458')
def clue6():
    return render_template('clue6.html')

@app.route('/clue7_poiw354nigga3847gay879')
def clue7():
    return render_template('clue7.html')

@app.route('/final_clue_s9d87f89sdhf98sdf')
def final_clue():
    return render_template('final-clue-1.html')

@app.route('/final_clue_s9d8w3487sdhdfghdfg98sdf')
def final_clue2():
    return render_template('final-clue-2.html')

@app.route('/final_clue_dfsd9f8skdf8s7df87')
def final_clue3():
    return render_template('final-clue-3.html')

@app.route('/final_clue_9sd8f7sdf8sdf7sdf')
def final_clue4():
    return render_template('final-clue-4.html')

@app.route('/final_clue_9sd8f7sd456dfgdfg8sdf7sdf')
def final_clue5():
    return render_template('final-clue-5.html')

@app.route('/final_clue_sad89f7hsdf897sdflkj123')
def final_clue6():
    return render_template('final-clue-6.html')

@app.route('/final_clue_7') #sd0f89sd8f9fg8df7gdf7sdf
def final_clue7():
    return render_template('final-clue-7.html')

app.run(debug=True, host="0.0.0.0", port=5000)
