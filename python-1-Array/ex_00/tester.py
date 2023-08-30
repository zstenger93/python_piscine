from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15, 1.71, 1.15, 1.90]
weight = [165.3, 38.4, 165.3, 80, 90.5]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# If your BMI is less than 18.5, it falls within the underweight range.
# If your BMI is 18.5 to <25, it falls within the healthy weight range.
# If your BMI is 25.0 to <30, it falls within the overweight range.
# If your BMI is 30.0 or higher, it falls within the obesity range.
