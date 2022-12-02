from flask import Flask, request, render_template
import pickle
import numpy as np



model = pickle.load(open('bananaM.pkl','rb'))

# Declare a Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        Temp = request.form.get('Temperature')
        soilM = request.form.get('Soil')
        hum = request.form.get('Humidity')
        area = request.form.get('Area')
        arr = np.array([[Temp,soilM,hum,area]])
        predict = model.predict(arr)
        output1 = round(predict[0],2)
        return render_template("website.html", output = "The yields of banana is {}".format(output1))
        

    else:
        prediction = ""
        return render_template("website.html", output = "")
        
    

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
