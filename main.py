# main.py
import os
from utils.data_collection import collect_data
from utils.data_preprocessing import preprocess_data
from utils.feature_engineering import engineer_features
from utils.model_training import train_model
from dotenv import load_dotenv

load_dotenv()

def main():
    # Set the API key, stock symbol, start date, and end date
    api_key = os.getenv("API_KEY")
    symbol = "AAPL"
    start_date = "2021-01-01"
    end_date = "2021-12-31"

    # Step 1: Collect Data
    data = collect_data(api_key, symbol, start_date, end_date)
    if data is None:
        print("Data collection failed. Exiting...")
        return

    # Step 2: Data Preprocessing
    preprocessed_data = preprocess_data(data)

    # Step 3: Feature Engineering
    feature_engineered_data = engineer_features(preprocessed_data)

    # Step 4: Model Training
    features = feature_engineered_data.drop("target", axis=1)
    target = feature_engineered_data["target"]

    model, train_score, test_score = train_model(features, target)
    print("Model Training Scores:")
    print(f"Train Score: {train_score}")
    print(f"Test Score: {test_score}")

    # Step 5: Model Evaluation and Prediction (if needed)

if __name__ == "__main__":
    main()
