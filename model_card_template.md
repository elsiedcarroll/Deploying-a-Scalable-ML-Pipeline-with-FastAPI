# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model was developed by Elsie Carroll.  It was developed on July 1st, 2026, and is currently in version 1.0.0.  It uses Random Forest Classifier for training.

## Intended Use

It is intended for use to show the FastAPI in action for Udacity's Machine Learning DevOps course.  It is also intended to classify the population segments based on salary, with a cutoff at $50,000, either less than or equal to, or greater than.

## Training Data

This has been trained off of open source census data, provided by Udacity.

## Evaluation Data

The model was evaluated off a subsection of the census data.

## Metrics

The model uses precision, recall, and F1 score to evaluate its performance.  After using a random state of 42, it performed as follows: Precision: 0.7353 | Recall: 0.6378 | F1: 0.6831

## Ethical Considerations

The data involved has been properly anonymized for open source use, and there are no ethical concerns involved with it.  Its use in training this model is in line with standard open source licensing for educational purposes.

## Caveats and Recommendations

Variability in the F1 score across a few categories indicate that there may be some underlying bias or underrepresented demographics, particularly in the Education segment.  If possible, gathering more data from underrepresented demographics would be ideal, to better train the model and make it more accurate.