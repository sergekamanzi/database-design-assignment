# **Database Design Assignment**

##  **Project Overview**
This project is designed to **predict Body Fat Percentage (BFP)** using machine learning and database integration. Users provide inputs such as **Weight, Height, BMI, Gender, and Age**, and the system predicts their **Body Fat Percentage** using a trained model.

The project integrates:
- **MySQL** – Storing structured user and measurement data.
- **MongoDB ** – Logging prediction results.
- **FastAPI (CRUD API)** – Providing endpoints to manage data.
- **Machine Learning Model** – Predicting BFP from user input.

## **Group Members**
- 
---

## **Features**
-  **MySQL** with users, measurements and predictions.
-  **MongoDB for NoSQL storage** (prediction logs).
-  **FastAPI-based CRUD operations** to manage user data.
-  **Machine Learning Model** to predict BFP based on user inputs.
-  **Automated Stored Procedures & Triggers** for efficient database management.

---

## **Tech Stack**
- **Databases:** MySQL & MongoDB
- **Backend API:** FastAPI (Python)
- **Machine Learning:** Scikit-Learn / Random Forest Model
- **Deployment:** Render

---

## **Database Schema**
The project consists of three key tables:
1. **Users** – Stores user details
2. **Measurements** – Stores physical attributes (Weight, Height, BMI, BFP).
3. **Predictions** – Stores the model's predicted BFP values.

 **MongoDB** is used to store logs of predictions for further analysis.

---

## **Installation & Setup**
### **Clone the Repository**
```sh
git clone https://github.com/sergekamanzi/database-design-assignment.git
cd database-design-assignment

 Set Up a Virtual Environment (Optional, Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

Install Dependencies

pip install -r requirements.txt

Set Up Databases

    Create a MySQL database (BFP_Prediction)
    Run the provided SQL schema to create tables.
    Set up a MongoDB collection for logs.

 Run FastAPI Server

uvicorn main:app --reload

FastAPI will be available at: http://127.0.0.1:8000/docs


