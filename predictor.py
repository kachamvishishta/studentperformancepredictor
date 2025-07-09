def predict_performance(attendance, study_hours, assignments_done):
    if attendance >= 75 and study_hours >= 2 and assignments_done:
        return "Pass"
    elif attendance >= 60 and study_hours >= 1:
        return "Maybe Pass"
    else:
        return "Fail"

# Input
print("---- Student Performance Predictor ----")
attendance = int(input("Enter attendance percentage: "))
study_hours = float(input("Enter daily study hours: "))
assignments_done = input("Have you completed all assignments? (yes/no): ").lower() == 'yes'

# Prediction
result = predict_performance(attendance, study_hours, assignments_done)
print(f"\nPrediction: The student is likely to: {result}")
