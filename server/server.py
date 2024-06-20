from flask import Flask,request,jsonify,render_template
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/predict_churn',methods =['GET','POST'])
def predict_churn(): 
    try:  
        
       

        tv = int(request.form['tv_name'])
        movie = int(request.form['movie_name'])
        age = float(request.form['age'])
        bill = float(request.form['bill'])
        contract = float(request.form['contract'])
        service = int(request.form['service'])
        download = int(request.form['download'])
        usage = float(request.form['usage'])
        ct = int(request.form['ct'])


        print(usage)
       
       
        response = jsonify({
        
        'estimated_churn': util.get_churn(tv,movie,age,bill,contract,service,download,usage,ct)
    })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500
 
        
if __name__ == '__main__':
      print("Starting Python Flask Server For Churn Prediction...")
      util.load_saved_artifacts()
      app.run()