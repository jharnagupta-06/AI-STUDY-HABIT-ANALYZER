from model import train_model
import pandas as pd

# Function to give suggestions
def get_suggestion(phone, distractions):
    if phone > 5:
        return "Try to reduce phone usage."
    elif distractions > 4:
        return "Avoid distractions while studying."
    else:
        return "Good habits! Keep it up."

def main():
    # Train model and get accuracy
    model, accuracy = train_model()
    
    try:
        # Take user input
        study = float(input("Enter study hours: "))
        sleep = float(input("Enter sleep hours: "))
        phone = float(input("Enter phone usage: "))
        distraction = float(input("Enter distraction level (1-5): "))
    except:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Convert input into DataFrame (important fix)
    input_data = pd.DataFrame(
        [[study, sleep, phone, distraction]],
        columns=['STUDY HOURS', 'SLEEP HOURS', 'PHONE HOURS', 'DISTRACTIONS']
    )
    
    # Predict productivity
    prediction = model.predict(input_data)
    score = prediction[0]
    
    # Display results
    print(f"\nPredicted Productivity: {score:.2f}%")
    print(f"Model Accuracy: {accuracy*100:.2f}%")
    
    # Productivity level classification
    if score < 40:
        print("Level: Low")
    elif score < 70:
        print("Level: Medium")
    else:
        print("Level: High")
    
    # Suggestion
    print("Suggestion:", get_suggestion(phone, distraction))

# Run the program
if __name__ == "__main__":
    main()