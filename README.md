# Metadata-Enhanced DistilBERT for Skincare Review Recommendation Prediction

## Project Overview

This project investigates transformer-based deep learning for skincare review recommendation prediction using the Sephora Products and Skincare Reviews dataset.

Traditional machine learning baselines based on TF-IDF representations were compared with a fine-tuned DistilBERT model and a metadata-enhanced hybrid architecture.

The aim was to evaluate whether lightweight skincare-review metadata such as skin type and review length could improve recommendation prediction performance.

---

## Dataset

Dataset source:

Sephora Products and Skincare Reviews Dataset (Kaggle)

After preprocessing:

- 2,224 skincare products
- 227,643 reviews
- 192,080 recommended reviews
- 35,563 not recommended reviews

The dataset was split using stratified sampling into training, validation and testing subsets.

---

## Models Evaluated

1. TF-IDF + Logistic Regression
2. TF-IDF + Linear SVM
3. DistilBERT
4. Metadata-only baseline
5. Hybrid DistilBERT + Metadata

---

## Results

| Model | Accuracy | F1-score |
|---------|---------|---------|
| Logistic Regression | 0.888 | 0.931 |
| Linear SVM | 0.902 | 0.941 |
| DistilBERT | 0.947 | 0.969 |
| Metadata Only | 0.651 | 0.778 |
| Hybrid DistilBERT + Metadata | 0.941 | 0.965 |

DistilBERT achieved the strongest overall performance.

---

## Repository Contents

- Deep Learning Report (PDF)
- Jupyter Notebook (.ipynb)
- Experimental Results
- Figures and Tables

---

## Requirements

Python libraries used:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- transformers
- datasets
- torch

---

## Running the Project

1. Open the notebook in Google Colab.
2. Install required libraries.
3. Load the Sephora dataset.
4. Execute cells sequentially.
5. Review generated evaluation metrics and figures.

---

## Author

Raeesa Amir

Student ID: 21336123

Manchester Metropolitan University
