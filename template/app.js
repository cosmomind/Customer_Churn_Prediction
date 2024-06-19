
    function onClickedPredictChurn() {
      console.log("Predict button clicked");
      var tv = document.getElementById("uitv");
      var movie = document.getElementById("uimovie")
      var age = document.getElementById("uiage")
      var bill = document.getElementById("uibill");
      var contract = document.getElementById("uicontract");
      var service = document.getElementById("uiservice");
      var download = document.getElementById("uidownload");
      var usage = document.getElementById("uiusage");
      var ct = document.getElementById("uict");

      var res = document.getElementById("uiEstimatedChurn");



    
      var url = "http://127.0.0.1:5000/predict_churn"; 
      $.post(url, {
        tv: tv.value,
        movie:movie.value,
        age: parseFloat(age.value),
        bill: bill.value,
        contract :parseFloat(contract.value),
        service: service.value,
        download: download.value,
        usage: parseFloat(usage.value),
        ct: ct.value
      },function(data, status) {
          console.log(data.estimated_churn);
          res.innerHTML = "<h4>" + data.estimated_churn.toString() + "</h4>";
          console.log(status);
      });
    }
    
    