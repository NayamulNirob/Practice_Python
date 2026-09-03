import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

cm = float(input(f'Enter height in cm: '))
weight = float(input(f'Enter weight in kg: '))


def calculate_BMI(height_cm, weight_kg):
    height_meter = height_cm / 100
    weight_kg = weight_kg
    return weight_kg / height_meter ** 2


def get_BMICategory(BMI):
    if BMI < 18.5:
        return 'Underweight', logging.WARNING
    elif BMI < 25:
        return 'Normal', logging.INFO
    elif BMI < 30:
        return 'Overweight', logging.WARNING
    elif BMI < 35:
        return 'Class 1 Obesity', logging.CRITICAL
    elif BMI < 40:
        return 'Class 2 Obesity', logging.CRITICAL
    else:
        return 'Class 3 Obesity', logging.CRITICAL


bmi = calculate_BMI(cm, weight)

category, log_level = get_BMICategory(bmi)

logging.log(
    log_level,
    f"BMI: {bmi:.3f} kg/m² | Category: {category}"
)
