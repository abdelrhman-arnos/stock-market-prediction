import pandas as pd
from sklearn.preprocessing import LabelEncoder

def handle_categorical_variables(data):
    # Assuming 'categorical_column' is the column name of the categorical variable
    label_encoder = LabelEncoder()
    data['categorical_column'] = label_encoder.fit_transform(data['categorical_column'])

    return data
