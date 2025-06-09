### 8-14. Cars

def build_car(brand, model, *safety, **features):
    """Build a car"""
    features["safety"] = safety
    features['brand'] = brand
    features['model'] = model
    return features

current_car = build_car('subaru', 'outback', "abs", "asp", "traction control", color='blue', tow_package=True)
for key, value in current_car.items():
    print(key, "-", value)
