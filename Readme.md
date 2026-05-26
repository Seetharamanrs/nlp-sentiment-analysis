#  NLP Sentiment Analysis

## Project Overview

This project is an end-to-end Natural Language Processing (NLP) application that predicts whether a movie review is positive or negative using Machine Learning techniques.

The IMDB movie review dataset was cleaned and preprocessed using multiple NLP techniques such as HTML removal, punctuation cleaning, tokenization, stopword removal, lemmatization, and TF-IDF vectorization. The processed text data was then used to train and evaluate sentiment classification models.

The project also includes a Flask REST API that allows users to send movie reviews and receive real-time sentiment predictions.


## Objectives
- Predict movie review sentiment as positive or negative
- Perform text preprocessing and NLP cleaning techniques
- Convert raw text into numerical vectors using TF-IDF
- Train and compare multiple NLP classification models
- Evaluate model performance using classification metrics
- Deploy the model using a Flask API on AWS
- Build a reusable preprocessing pipeline using Python modules

## Dataset

The dataset contains:

- 50,000 movie reviews
- 25,000 training reviews
- 25,000 testing reviews
- Binary sentiment labels:
  - Positive
  - Negative

Reviews are labeled only when:

- Positive review score ≥ 7/10
- Negative review score ≤ 4/10

This makes the sentiment classification task more reliable and less ambiguous.

## NLP Preprocessing Pipeline

The raw text reviews were cleaned using multiple NLP preprocessing techniques.

### Text Cleaning Steps
- HTML tag removal
- Punctuation removal
- Lowercase conversion
- Tokenization
- Stopword removal
- Lemmatization

The preprocessing logic was modularized inside:

`preprocessing.py`

## TF-IDF Vectorization

After preprocessing, the cleaned text was converted into numerical vectors using:

 `TF-IDF Vectorization`

This helps Machine Learning models understand textual data mathematically by assigning importance scores to words.

## Models Used
### Logistic Regression
- Achieved 89% accuracy
- Main sentiment classification model
- Performed better compared to Naive Bayes
### Multinomial Naive Bayes
- Baseline NLP classification model
- Used for comparison and evaluation

## Model Evaluation

The models were evaluated using:

- Accuracy Score
- Confusion Matrix
- Unseen Test Dataset

The Logistic Regression model performed better overall for sentiment classification.

## API Development

The trained model was deployed using Flask REST API.

### Endpoint
`POST /predict`

Request Example
``` 
{
    "review": "This movie was amazing"
} 
```

Response Example
```
 {
    "Prediction": "positive"
} 
```   



## Tech Stack
- Python
- Pandas
- NLTK
- Scikit-learn
- Flask
- Joblib
## Key Learnings
- Understanding core NLP preprocessing techniques
- Text cleaning and normalization
- TF-IDF vectorization
- Sentiment classification using Machine Learning
- Building reusable preprocessing pipelines
- Model serialization using Joblib
- Creating REST APIs using Flask
- Real-world NLP workflow implementation
## Future Improvements
- FastAPI implementation
- Docker containerization
- Streamlit frontend
- AWS deployment
- Transformer-based NLP models
- Hugging Face integration

## Author 

Seetharaman Radhakrishnan