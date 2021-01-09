def quetelet(height, weight):
    bmi = weight / height ** 2
    if bmi < 20:
        return "thin"
    if bmi <= 25:
        return "normal"
    if bmi <= 30:
        return "overweight"
    return "obese"
