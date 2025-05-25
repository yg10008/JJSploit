def parser(res):
    try:
        data = res.json()
        if not data:
            return None
        car_info = data[0]                 
        details={
            'Vehicle_manufacturer': car_info['make'],
            'Vehicle_model': car_info['model'],
            'transmission': car_info['transmission'],
            'Vehicle_year': car_info['year'],
            'fuel_type': car_info['fuel_type'],
            'drive_type': car_info['drive'],
            'highway_mpg': car_info['highway_mpg'],
            'cylinders': car_info['cylinders'],
            'city_mpg': car_info['city_mpg'],
            'displacement': car_info['displacement'],
            'combination_mpg': car_info['combination_mpg'],
            'class': car_info['class'],
        } 
        return details
    except ValueError as e:
        print("Error parsing JSON:", e)
        return None
