import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model():
    # Load dataset
    data = pd.read_csv("data.csv")
    
    # Select features and target
    X = data[['STUDY HOURS', 'SLEEP HOURS', 'PHONE HOURS', 'DISTRACTIONS']]
    y = data['PRODUCTIVITY']
    
    # Split into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Calculate accuracy
    accuracy = model.score(X_test, y_test)
    
    return model, accuracy