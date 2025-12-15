# Census Income Prediction Model Card

## Model Details
This Random Forest Classifier model is called Census Income Predictor. It is trained on the publicly available Census Bureau dataset to classify users into two groups based on their salary. The threshold salary used is $50,000. See Data.
As of December 14, 2025, the model is trained using the Scikit-Learn package with 100 estimators and random_state=42. 



import json
import requests

url = "http://127.0.0.1:8000/data/"
sample = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States"
}
headers = {"Content-type": "application/json"}
response = requests.post(url, data=json.dumps(sample), headers=headers)
print(response.status_code, response.json())


## Intended Use
Census Income Predictor is developed for research and analytical purposes. It should not be used for employment, lending, or other high-stakes decisions affecting individuals’ rights or finances.

## Data
The publicly available Census Bureau dataset is used. Features included:
    • age
    • capital-gain
    • capital-loss
    • education-num
    • education
    • fnlwgt
    • hours-per-week
    • marital-status
    • native-country
    • occupation
    • race
    • relationship
    • sex
    • workclass
Dataset size: 32,561 observations, with 20% reserved for evaluation.

## Metrics
Overall performance on the test dataset:
    
    | Metric    | Value |
    |---------- |-------|
    | Precision | 0.74  |
    | Recall    | 0.63  |
    | Fbeta     | 0.68  |


## Ethical Considerations
Bias may exist in race, sex, and native-country categories. Monitor behavior continuously, particularly on intersections of these features. Use this model responsibly, and avoid deployment in high-stakes scenarios without fairness evaluation.

## Caveats and Recommendations
    • This model is not guaranteed to be fit for production.
    • Bias mitigation checks are recommended upstream of any decisions.
    • Model outputs probabilistic estimates, not guaranteed outcomes.
    • Review slice metrics regularly to monitor fairness.

## Github URL:  https://github.com/harrieyw/Deploying-a-Scalable-ML-Pipeline-with-FastAPI
