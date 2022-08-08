sample_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
               {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
               {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
               {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
               {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
               {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


def check_bmi(data):
    try:
        counter = 0
        for item in data:
            bmi = item['WeightKg'] / (item['HeightCm'] / 100) ** 2
            if 25 <= bmi <= 29.9:
                counter += 1
        return counter
    except Exception as e:
        print("Exception occurred!!", e)
