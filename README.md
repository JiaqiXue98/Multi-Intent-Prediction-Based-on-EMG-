# Multi-Intent-Prediction-Based-on-EMG

We have designed this work for continuous multi-intent prediction. 

# File Description 
Testing set including 5 trails for subject5 is placed in './Dada/'. 

The trained model is saved in './Model/'. 

The 'utilities_multi' can process EMG signals to sliding windows. 

The 'test_result' is used to read data, load the model, and show testing results. 

# Usage
This testing script is carried on Tensorflow-v2.

Run the script 'test_result' to test the prediction performance of an example subject. 

The accuracy and R² are calculated and printed. 

The comparison of true labels and prediction results are displayed on three figures and saved in 'Result_figures'.
