from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input values from the form
        input_data = [float(request.form.get(field, default_values[field]) )]
        input_data = np.array(input_data).reshape(1, -1)

        # Predict whether the transaction is fraudulent
        prediction = model.predict(input_data)
        result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)