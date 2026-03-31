# AI Study Habit Analyzer 📊

## 📌 Project Description

This project is a Machine Learning-based system that predicts a student's productivity score based on daily habits such as study hours, sleep hours, phone usage, and distractions. It helps analyze behavior patterns and provides useful suggestions to improve productivity.

---

## 🚀 Features

* Predicts productivity score (0–100)
* Displays productivity level (Low, Medium, High)
* Provides personalized suggestions
* Shows model accuracy
* Simple command-line interface

---

## 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn

---

## 📊 Dataset

The dataset used in this project is manually created based on realistic assumptions of student behavior. It contains the following features:

* Study Hours  
* Sleep Hours  
* Phone Usage  
* Distractions  
* Productivity Score  

---

## 📁 Project Structure
model.py → Machine learning model logic
main.py → Main program execution
data.csv → Dataset
requirements.txt → Required libraries
README.md → Project documentation

---

## ⚙️ Setup Instructions

1. Clone the repository:
git clone https://github.com/your-username/repo-name

cd repo-name

2. Install required libraries:
pip install -r requirements.txt

---

## ▶️ How to Run the Project

Run the following command in terminal:
python main.py

---

## ⚙️ Working of the Model

The project uses a Linear Regression model to predict productivity score based on input features like study hours, sleep hours, phone usage, and distractions. The model is trained on the dataset and then used to make predictions for new inputs.

---

## 💡 Example Output
Enter study hours: 6
Enter sleep hours: 7
Enter phone usage: 4
Enter distraction level (1-5): 3

Predicted Productivity: 72.50%
Model Accuracy: 88.30%
Level: High
Suggestion: Good habits! Keep it up.

---

## ⚠️ Limitations

* Dataset is manually created  
* Accuracy may vary with real-world data  

---

## 📈 Future Improvements

* Add graphical user interface (GUI)  
* Use real-world dataset  
* Improve model accuracy with advanced algorithms  

---

## 👩‍💻 Author

Jharna Gupta
