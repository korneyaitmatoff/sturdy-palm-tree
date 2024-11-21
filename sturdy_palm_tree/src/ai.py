import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sturdy_palm_tree.src.api.service import StudentService
from sturdy_palm_tree.src.api.core import tables
from config import db_config
from sklearn.metrics import accuracy_score, classification_report

service = StudentService(table=tables.Students, **db_config)


def predict_alcohol_risk(age, gender, performance, stress, family_alcohol, classmates_relations):
    data = [
        {
            "age": student.age,
            "gender": 1 if student.gender == 'M' else 0,
            "performance": student.performance,
            "stress": student.stress,
            "family_alcohol": int(student.family_alcohol),
            "classmates_relations": int(student.classmates_relations),
            "alcohol_forecast": student.alcohol_forecast
        }
        for student in service.read()
    ]

    df = pd.DataFrame(data, columns=['gender', 'age', 'performance', 'stress', 'family_alcohol', 'classmates_relations',
                                     'alcohol_forecast'])
    X = df[["age", "gender", "performance", "stress", "family_alcohol", "classmates_relations"]]
    y = df["alcohol_forecast"]

    print("Start learning")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=100000)
    model.fit(X_train, y_train)
    gender = 1 if gender.upper() == 'M' else 0
    input_data = [[age, gender, performance, stress, family_alcohol, classmates_relations]]
    risk_percentage = model.predict_proba(input_data)[0][1] * 100

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Точность модели:", accuracy)

    return risk_percentage


risk = predict_alcohol_risk(18, 'M', 50, 1, 1, 1)

print(f"Риск алкогольной зависимости: {risk}%")
