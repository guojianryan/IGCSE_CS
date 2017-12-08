car_spots = [""] * 10
larger_spots = [""] *5

while True:
    type_of_op = -1

    while type_of_op not in range(1,4):
        type_of_op = int(input("What is happening [1:entry, 2: exit, 3:stop]"))
    
    spots = car_spots

    #get the plate number and the type of the vehicle 
    if(type_of_op == 1 or type_of_op == 2):
        plate_number = input("What is the plate number?")
        type_of_vehicle = -1 
        while type_of_vehicle not in range(1, 3):
            type_of_vehicle = int(input("1: car, 2: larger vihecle"))
        #full
        if type_of_vehicle == 2:
            spots = larger_spots
    #entrance
    if type_of_op == 1:
        for idx in range(len(spots)):
            if spots[idx] == "":
                spots[idx] = plate_number
                break
        else:
            print("The carpark is full. No Entrance.")
    #exit
    elif type_of_op == 2:
        for idx in range(len(spots)):
            if spots[idx] == plate_number:
                spots[idx] = ""
                break
    #stop the program
    else:
        break

    print(car_spots)
    print(larger_spots)