import garage

print('You have these cars in your garage yugm!')
g = garage.garage()           

g.list_out_cars()

choice = int(input('1. add brand new car\n2. remove car\n3. exit\n'))
if choice == 1:
    make  = input('enter the make of the car ')
    year  = input('enter the year of the car ')
    model = input('enter the model of the car ')
    g.addNewCar(make, year, model)
elif choice == 2:
    car_name = input('enter the model name to remove ')
    g.remove_car(car_name)
elif choice == 3:
    print('thank you for using our service')
else:
    print('invalid choice')
