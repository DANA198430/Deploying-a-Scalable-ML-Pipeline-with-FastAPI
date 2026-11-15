# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This project uses a Random Forest Classifier to predict whether an individual's annual income is greater than $50,000 or less than or equal to $50,000.

The model was developed using Python and scikit-learn. It uses 100 decision trees, a random state of 42, and a minimum of 2 samples required to split an internal node.

Categorical features are processed using Scikit-learn's OneHotEncoder, and the target variable is transformed using LabelBinarizer.

## Intended Use

The intended use of this model is to demonstrate machine learning classification techniques using census income data.

It can be used for educational purposes, experimentation, and evaluating model performance across different demographic and employment-related categories.

This model should not be used to make actual employment, lending, financial, or other high-impact decisions about individuals.

## Training Data

The model was trained using the 1994 Census Income dataset (`data/census.csv`).

The dataset contains 32,561 records and 15 columns, including age, workclass, education, marital status, occupation, relationship, race, sex, hours worked per week, native country, and salary.

The salary column is the prediction target. The categorical features were encoded using OneHotEncoder.

The dataset was divided into 80% training data and 20% testing data using a random state of 42. Stratified sampling was used to preserve the salary distribution in both datasets.

Unknown categorical values represented by "?" were retained as categories during preprocessing.

## Evaluation Data

The model was evaluated using the 20% test portion of the dataset that was not used during training.

The test dataset was processed using the encoder fitted on the training dataset. This ensured that the same categorical encoding was applied consistently during evaluation.

The model was also evaluated across individual categories of each categorical feature to examine differences in performance across data slices.

## Metrics

The model was evaluated using precision, recall, and F1 score.

The evaluation results on the test dataset were:

- Precision: 0.7353
- Recall: 0.6378
- F1 Score: 0.6831

Precision measures how many of the individuals predicted to earn more than $50,000 actually belong to that category.

Recall measures how many of the actual individuals earning more than $50,000 were correctly identified.

The F1 score represents the balance between precision and recall.

Categorical slice performance was also calculated for each unique value of every categorical feature. The results were saved in `slice_output.txt`.

## Ethical Considerations

The dataset contains sensitive demographic and socioeconomic attributes, including race, sex, age, marital status, and native country.

Predictions based on historical census data may reflect existing social and economic inequalities. Differences in model performance across demographic groups could lead to unfair outcomes if the model were used in real-world decision-making.

The model should not be used to determine an individual's financial worth, employment eligibility, or access to services.

The categorical slice evaluation provides additional information about performance differences across groups, but it does not establish that the model is fair or free from bias.

## Caveats and Recommendations

The model is trained on historical 1994 census data and may not accurately represent current economic conditions or income patterns.

The model's performance is limited by the quality, completeness, and representativeness of the original dataset.

The overall F1 score of 0.6831 indicates that there is room for improvement. Further work could include hyperparameter tuning, testing additional classification algorithms, addressing class imbalance, and investigating differences in performance across demographic groups.

The model should be used for educational and experimental purposes only. Additional validation, fairness testing, and updated data would be necessary before considering any real-world application.
