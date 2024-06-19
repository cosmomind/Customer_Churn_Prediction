from flask import Flask,request,jsonify,render_template
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/predict_churn',methods =['GET','POST'])
def predict_home_price(): 
    try:  
        
        tv = int(request.form['is_tv_subscriber'])
        movie = int(request.form['is_movie_package_subscriber'])
        age = float(request.form['subscription_age'])
        bill = int(request.form['bill_avg'])
        contract = float(request.form['remaining_contract'])
        service = int(request.form['service_failure_count'])
        download = int(request.form['download_over_limit'])
        usage = float(request.form['total_usage'])
        ct = int(request.form['is_contract'])
       
       
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