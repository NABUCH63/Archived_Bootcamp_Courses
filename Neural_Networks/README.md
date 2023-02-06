# Neural Network Charity Analysis

* initial commmit 19JUN2022

* updated models to save every 5 epochs, removed optimizer and used single nn model for deliverable 3. 22JUN2022

## Background

The AlphabetSoup organization wants to continue to fund various charities. In order to make the best decision of which charities to continue funding, a list of charities with their various stats was supplied to determine which are most successful.

In order to determine this, a deep learning neural network was created to input the various columns of data and find the best model to represent the data.

## Overview of the Analysis

This analysis consisted of three steps:

* clean the data and preprocess it into an appropriate number of bins, to convert categorical variables into integer values, and to remove any unnecessary columns.

* Perform an initial neural network model and save the weights per epoch and the final model outcome.

* Perform a more indepth analysis, removing additional columns to avoid confusing the model, altering the activation functions, and changing the number of iterations performed. This was done with an auto-optimization script running through more than a hundred configurations.

## Results

Data Preprocessing:

The target variables were identified to be "IS_SUCCESSFUL", a binary column identifying if the charity has been successful in the past. The features were considered to be all remaining columns not including ID, name, or index columns. "EIN" and "NAME" columns were dropped immediately. 

"CLASSIFICATION", "APPLICATION_TYPE", and "INCOME_AMT" were binned to combine groups identified based on density plots. This removed excess noise, and allowed for a more streamlined analysis. 

Variables identified to be unnecessary in addition to the "EIN" and "NAME" were found to be "STATUS" and the resultant "SPECIAL_CONSIDERATIONS_N". These were all removed from the analysis

Compiling, Training, and Evaluating the Model:

The initial model had 80 nodes in the first hidden layer, 30 in the second, and the output layer having one. The activation functions were "relu", "relu", and "sigmoid" respectively. This was to determine initial performance.

The following optimization function ran through many itterations, eventually finding the best outcome given the data setup was:

activation function: "relu"
layers:
    1: 31
    2: 11
    3: 21
    output: 1

This model had a tested accuracy of 72.9%, and did not reach the target performance of 75%. Some such steps taken to increase performance were:

* using the optimizer function to find the best configuration of nodes and hidden layers
* removed columns: SPECIAL_CONSIDERATIONS_N, STATUS, binned income amount and asking amount columns, and reclassified CLASSIFICATION and APPLICATION_TYPE columns to include more of the rare entries.

## Summary

Given the data available, it could be possible to find better parameter setup to get a better performance. Other models that may benefit similarly could include logistic regression, SVM, and other categorization methods that determine between two outcomes.



