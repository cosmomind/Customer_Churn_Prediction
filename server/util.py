import json
import pickle 
import numpy as np
import joblib

model = None
scaler = None


def get_churn(tv,movie,sub_age,bill,remain_crct,service_failure,download_over_limit,tot_usage,is_contract):
    
    res = np.zeros(9)
    res[0] = tv
    res[1] = movie
    res[2] = sub_age
    res[3] = bill
    res[4] = remain_crct
    res[5] = service_failure
    res[6] = download_over_limit
    res[7] = tot_usage
    res[8] = is_contract
    res_normalized = scaler.transform([res])
    
    return  model.predict(res_normalized)[0] 
      



def load_saved_artifacts():
      print("loading saved artifacts..")

      global model
      global scaler
      

    
      with open(r"D:\Customer_Churn\server\churn_model.pickle","rb") as f:
            model = pickle.load(f)
      
      with open(r"D:\Customer_Churn\server\scaler.pkl","rb") as f:
            scaler = joblib.load('scaler.pkl')


      print("Artifacts has been loaded")
            

if __name__ == "__main__":
      load_saved_artifacts()
      
      print(get_churn(1,0,8.91,16,0.00,0,0,14.6,0))
      print(get_churn(1,0,11.95,25,0.14,0,0,10.7,1))


