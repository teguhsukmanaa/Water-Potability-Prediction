# Supervised Machine Learning for Predicting Water Potability 

Access to clean and potable water is essential for sustaining life and ensuring public health. However, with increasing industrialization and population growth, the quality of water sources suffers from contamination, posing a significant threat to human health and environmental degradation. Therefore, identifying and classifying water sources as potable or non-potable is crucial for ensuring the safety of drinking water supplies and mitigate health risks.

Recognizing the importance of this issue and the potential impact of data-driven solutions, we choose the water potability problem as the topic of our project, with the main focus on predicting the classification of potable water based on data features using supervised machine learning techniques.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [Deployment](#deployment)

## Introduction
In this project, I developed a Machine Learning model to predict water potential classification based on physicochemical parameter data. The model was built using scikit-learn by defining several algorithm models, with the best model obtained being Random Forest. The goal of this project is to assist water scientists or investigators in predicting the quality or potential viability of water for consumption.

## Dataset
The dataset used in this project was sourced from the [Kaggle platform](https://www.kaggle.com/datasets/adityakadiwal/water-potability). In general, this dataset is a compilation of water quality data from various water samples based on several parameters of characteristic and water content measurements such as, pH, Organic Content, Conductivity, Total Dissolved Solids (TDS), and others. In addition, this dataset already has a label that determines the potability class.

## Installation
To run this project locally, please follow these steps:
1. Clone this repository: `git clone git@github.com:teguhsukmanaa/Water-Potability-Prediction.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Or download the files manually.

## Usage
To use the trained model for predicting the water potability, follow these steps:
1. Load the pre-trained model weights
2. Preprocess the input data
3. Make predictions using the model

## Results
The machine learning model obtained is the Random Forest model, which achieved a prediction accuracy of 72%. In other words, by utilizing the predictions of this model, we can forecast the suitability of water for consumption with 72% accuracy.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. Let's collaborate and make this project even better!

## Deployment
I have deployed my model in Huggingface platform for prototype utilization. Try to check your water potability class!. 

Check out at this link : https://huggingface.co/spaces/teguhsukmanaa/FTDS-RMT-29-M2-teguh-sukmana 

Thank you for visiting this repository! If you have any questions or feedback, please don't hesitate to reach me out.


[teguhsukmanaa](https://github.com/teguhsukmanaa)
