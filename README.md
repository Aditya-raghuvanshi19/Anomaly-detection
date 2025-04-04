# Fraud Detection Web App  

## Navigate to the project directory:  
Install the required dependencies:  
Ensure you are using Python version **3.10**.  

## Usage  

### Run the Flask application:  
```bash
python app.py
```

Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).  

Use the web interface to:  
- Input transaction data manually.  
- Upload a CSV file for testing.  
- Fetch random transaction data for testing.  

## API Endpoints  

### `/` (GET, POST)  
- **GET:** Renders the main page with the form for input.  
- **POST:** Accepts transaction data from the form, processes it using the trained model, and returns whether the transaction is fraudulent or not.  

### `/csvfile` (GET)  
Fetches random transaction data from the `creditcard.csv` file and populates the form fields dynamically.  

## Machine Learning Models  

### **Isolation Forest**  
- Detects anomalies by isolating observations.  
- Achieved the best performance in detecting fraudulent transactions.  

### **Local Outlier Factor (LOF)**  
- Computes the local density deviation of a data point compared to its neighbors.  

### **Support Vector Machine (SVM)**  
- Identifies anomalies using a one-class classification approach.  

## Results  

| Model                   | Accuracy  |
|------------------------|-----------|
| Isolation Forest        | **99.74%** |
| Local Outlier Factor    | 99.65%    |
| Support Vector Machine  | 70.09%    |

## File Structure  
```
/fraud_detection_app
│── app.py
│── templates/
│── static/
│── models/
│── creditcard.csv
│── requirements.txt
│── README.md
```

## Requirements  

The project requires the following Python libraries, as listed in `requirements.txt`:  
```plaintext
Flask==3.1.0
scikit-learn==1.6.1
pandas==2.2.3
numpy==2.2.4
matplotlib==3.10.1
seaborn==0.13.2
```

And other dependencies listed in the `requirements.txt` file.  

## Future Improvements  
- Use deep learning models for better accuracy.  
- Enhance the UI for a more seamless user experience.  
- Add support for real-time transaction monitoring.  

## Acknowledgements  
The dataset was collected and analyzed during a research collaboration between **Worldline** and the **Machine Learning Group of ULB (Université Libre de Bruxelles)**. More details can be found [here](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).  

## License  
This project is licensed under the **MIT License**.
