# Multi-Intent-Prediction-Based-on-EMG

We have designed this work for continuous multi-intent prediction. 

Please note that the data is placed in './Dada/', while the trained model is saved in './Model/'. The 'utilities_multi' should be imported to process EMG signals to sliding windows. The 'test_result' is used to read data, load the model, and show testing results. And this testing program is carried on Tensorflow-v2.

Please run the 'test_result' to test the prediction performance of an example subject. The accuracy and R² are calculated and printed. Additionall, the comparison of true labels and prediction results are displayed on three figures and saved in 'Result_figures'.
