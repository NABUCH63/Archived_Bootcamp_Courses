# Module 18 Cryptocurrencies unsupervised

12JUN2022

- Initial commit of repository. Includes .ipynb file containing ETL and dataframe creation script.
- All deliverables included in one script:
    * Dataframe is created, and filtered for traded and mined crypto with no missing values. Dummies are created for text variables, and scaled.
    * PCA applied to reduce to three classes for further processing, and KMeans is applied for four clusters based on elbow diagram produced
    * Clustered dataframe created with the principal components from the PCA, the prediction classes, and the initial columns of the crytpo dataframe. 
    * visuals are created as a 2d and 3d scatter, hover text set to show coin name and algorithm.