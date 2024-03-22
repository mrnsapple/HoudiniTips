import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from joblib import dump

def load_and_preprocess_data(filepath):
    """
    Loads the dataset from the given filepath and preprocesses it.
    
    Parameters:
    - filepath: Path to the dataset file.
    
    Returns:
    - X: Features DataFrame.
    - y: Target variable Series.
    """
    df = pd.read_csv(filepath)
    
    X = df[['Elevation', 'Slope', 'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology']]  # Features
    scaler = MinMaxScaler()
    #Adding features togheter, there is no too much Accuracy improvements.
    #X["Elevation_Slope"] = (X['Elevation'] + X['Slope'])
    #X['Distance_To_Hydrology'] = (X['Horizontal_Distance_To_Hydrology'] + X['Vertical_Distance_To_Hydrology'])
    #X[['Height', 'Slope']] = scaler.fit_transform(X[['Elevation', 'Slope']])
    #X = df.drop(['Id', 'Cover_Type'], axis=1).values
    scaler.fit(X)
    X = scaler.transform(X)
    y = df['Cover_Type'].values.astype(int)  # Target variable
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Splits the dataset into training and test sets.
    
    Parameters:
    - X: Features DataFrame.
    - y: Target variable Series.
    - test_size: Proportion of the dataset to include in the test split.
    - random_state: Controls the shuffling applied to the data before applying the split.
    
    Returns:
    - X_train, X_test, y_train, y_test: Split datasets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    """
    Trains the RandomForestClassifier model.
    
    Parameters:
    - X_train: Training features DataFrame.
    - y_train: Training target variable Series.
    
    Returns:
    - clf: Trained model.
    """
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf

def evaluate_model(clf, X_test, y_test):
    """
    Evaluates the trained model using accuracy score.
    
    Parameters:
    - clf: Trained model.
    - X_test: Test features DataFrame.
    - y_test: Test target variable Series.
    
    Returns:
    - accuracy: Accuracy score of the model.
    """
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Example of using these functions
if __name__ == "__main__":
    # Step 1: Load and preprocess data
    project_root = os.path.abspath(__file__).rsplit("/", 2)[0]
    X, y = load_and_preprocess_data(project_root + '/data/train.csv')
    
    # Step 2: Split the data
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Step 3: Train the model
    clf = train_model(X_train, y_train)

    # Step 4: Evaluate the model
    accuracy = evaluate_model(clf, X_test, y_test)
    print(f'Accuracy: {accuracy:.2f}')

    # Step 5: Save Model
    model_path = project_root + '/models/tree_scattering.joblib'
    dump(clf, model_path)
