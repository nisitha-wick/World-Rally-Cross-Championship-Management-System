# Python Coursework - Nisitha Wickramarachchi (IIT - 20210844)(RGU - 2236766)
# Data will be stored in 2 text files.

# Creation of the list to store driver details.
driverlist = [['Nisitha', 20, 'Toyota', 'Supra', 0], ['Kasundi', 21, 'Nissan', 'GTR', 0], ['Aseka', 30, 'Ferrari', 'idk', 0]]

# Creation of the list to store race details.
racelist = []

# Printing a welcome statement.
print("<<<<<<<< WELCOME TO THE WORLD RALLY CROSS CHAMPIONSHIP MANAGEMENT SYSTEM >>>>>>>>")


def print_menu():  # 1st FUNCTION - Printing user options.
    print("\nSelect an option.\n")
    print("1. Type ADD for adding driver details.")
    print("2. Type DDD for deleting.")
    print("3. Type UDD for updating driver details.")
    print("4. Type VCT for viewing the rally cross standing table.")
    print("5. Type SRR for simulating a random race.")
    print("6. Type VRL for viewing race table sorted according to the date.")
    print("7. Type STF to save current data to a text file.")
    print("8. Type RFF to load data from the saved text file.")
    print("9. Type ESC to exit the program.\n")


def add():  # 2nd FUNCTION - Adding new driver details
    print("--------------------------------------------------------------")
    driver_name = input("ENTER Driver's Full Name >>> ")
    for elements in driverlist:  # Extracting names from main list
        while driver_name in elements[0]:  # If entered name is in lists, user must enter a unique name.
            print("This Driver name seems to be in our records. Please enter a unique name.")
            driver_name = input("ENTER Driver's Full Name >>> ")

    while True:  # While True, so it'll loop if user enters wrong input.
        try:  # Exception handling to continue the code if users enters wrong inputs.
            print("--------------------------------------------------------------")
            driver_age = int(input("ENTER Driver age >>> "))
            break
        except ValueError:
            print("ERROR! Please ENTER an integer.")

    print("--------------------------------------------------------------")
    driver_team = input("ENTER the representing Team Name >>> ")
    while len(driver_team) < 1:  # Validating inputs for driver team.
        print("Please ENTER your team name. This is a COMPULSORY.")
        driver_team = input("ENTER the representing Team Name >>> ")

    print("--------------------------------------------------------------")

    driver_car = input("ENTER Driver Car Model >>> ")
    while len(driver_car) < 1:  # Validating inputs for driver car model.
        print("Please ENTER your car model. This is COMPULSORY.")
        driver_car = input("ENTER Driver Car Model >>> ")

    while True:  # While True, so it'll loop if user enters wrong input.
        try:  # Exception handling to continue the code if users enters wrong inputs.
            print("--------------------------------------------------------------")
            driver_points = int(input("ENTER Driver's current points >>> "))
            break
        except ValueError:
            print("ERROR! Please ENTER an integer.")

    print("--------------------------------------------------------------")
    print("Driver details have been recorded.")
    print("--------------------------------------------------------------\n")
    # Appending added details to the list.
    driverlist.append([driver_name, driver_age, driver_team, driver_car, driver_points])
    print(driverlist)

    print("\nTo rectify any mistake, please use the UDD section.")

    print("--------------------------------------------------------------")


def ddd():  # 3rd FUNCTION - Deleting driver details.
    # Obtaining the name of the driver that the user would like to delete.
    driver_name = input("Enter the Full Name of the Driver to delete the relevant details >>> ")

    for details in driverlist:  # Getting the Driver's name from the driver details list.
        if driver_name in details:  # Checking whether the name is available.

            # Removing the corresponding details from the driver details list.
            driverlist.pop(driverlist.index(details))
            print(driverlist)
            print("Driver details have been successfully removed.\n")
        else:
            print("Unable to find Driver details. Please make sure to enter the correct name.\n")


def udd():  # 4th FUNCTION - Updating driver details.
    # Creation of a list to add driver names into.
    name_list = []

    for sublist in driverlist:  # Getting the Driver's name from the driver details list.
        name_list.append(sublist[0])  # Appending the extracted names.

    print("--------------------------------------------------------------")

    # Obtaining the name of the driver that the user would like to update.
    driver_name = input("Enter the Full Name of the Driver to update the relevant details >>> ")

    if driver_name in name_list:  # Checking whether the name is available.

        # Getting the index of the nested list of the name that was entered.
        updated_index = (name_list.index(driver_name))

        print("--------------------------------------------------------------")
        upd_driver_name = input("UPDATE driver name >>> ")
        while len(upd_driver_name) < 1:  # Validating inputs for updating driver name.
            print("Please UPDATE driver's name. This is COMPULSORY.")
            upd_driver_name = input("UPDATE driver name >>> ")

        while True:  # While True, so it'll loop if user enters wrong input.
            try:  # Exception handling to continue the code if users enters wrong inputs.
                print("--------------------------------------------------------------")
                upd_driver_age = int(input("UPDATE driver age >>> "))
                break
            except ValueError:
                print("ERROR! Please enter an integer.")
        print("--------------------------------------------------------------")
        upd_driver_team = input("UPDATE driver team >>> ")
        while len(upd_driver_team) < 1:  # Validating inputs for updating driver team name.
            print("Please UPDATE driver's team name. This is COMPULSORY.")
            upd_driver_team = input("UPDATE driver team >>> ")
        print("--------------------------------------------------------------")
        upd_driver_car = input("UPDATE driver car >>> ")
        while len(upd_driver_car) < 1:  # Validating inputs for updating driver car model.
            print("Please UPDATE driver's car model. This is COMPULSORY.")
            upd_driver_car = input("UPDATE driver car >>> ")

        while True:  # While True, so it'll loop if user enters wrong input.
            try:  # Exception handling to continue the code if users enters wrong inputs.
                print("--------------------------------------------------------------")
                upd_driver_points = int(input("UPDATE driver points >>> "))
                break
            except ValueError:
                print("ERROR! Please enter an integer.")
        print("--------------------------------------------------------------")
        print("\nYour Details have been successfully updated.")
        print("--------------------------------------------------------------")

        # Creation of a list to contain the updated driver details.
        upd_driverlist = []

        # Adding the updated details into the list from the variables.
        upd_driverlist = [upd_driver_name, upd_driver_age, upd_driver_team, upd_driver_car, upd_driver_points]

        # Rewriting the old nested list with the newly made one.
        driverlist[updated_index] = upd_driverlist
        print(driverlist)

    else:
        print("ERROR! This driver does not seem to exist.")


def vct():  # 5th FUNCTION - View Championship Standing Table.
    global driverlist  # convert to global, so it can be accessed outside the while loop.

    if len(driverlist) >= 1:

        driverlistdescend = []  # Creation of a list store points in descending order.
        while len(driverlist) > 0:  # A while loop to run the sort function until driver details list is empty.

            driverpointslist = []  # Creation of a list to put driver points into.

            for sublist in driverlist:
                driverpoints = sublist[4]   # Allocating each point in the driver details list into this variable.
                driverpointslist.append(int(driverpoints))  # Appending the variable into the list.

                max_value = max(driverpointslist)  # This will collect the maximum point gained by a driver.

            for sublist in driverlist:  # To get the index of the driver who has the highest points.
                if max_value in sublist:
                    index_of_driver = driverlist.index(sublist)

            driverlistdescend.append(driverlist[index_of_driver])  # Appending the driver with the highest point.
            driverlist.pop(index_of_driver)  # Removing the driver with the highest points from the driver details list.

        driverlist = driverlistdescend  # Overwriting the old driver details list with the new list.

        # Printing the header of the table.
        print("|        DRIVER NAME        | DRIVER AGE |      DRIVER TEAM     |     CAR MODEL     | DRIVER POINTS |")

        for item in driverlist:  # Extracting the elements in driver details list.
            print("|", item[0], " " * (24-len(item[0])), "|",
                  item[1], " " * (9-len(str(item[1]))), "|",
                  item[2], " " * (19 - len(item[2])), "|",
                  item[3], " " * (16 - len(item[3])), "|",
                  item[4], " " * (12 - len(str(item[4]))), "|",
                  )  # Creating rows of the table.
        print('\n')
        stf_driverfile()
    else:
        print("ERROR! There are no drivers to be entered into the championship table.")

def srr():  # 6th FUNCTION - Simulating a random race.
    if len(driverlist) >= 3:  # There should be 3 or more drivers to simulate a race.

        print("SIMULATION IN PROGRESS....")

        namelist = []  # Creating a list to put extracted names into.
        for sublist in driverlist:  # For loop used to extract driver names.
            driver = sublist[0]  # Allocating the names into this variable.
            namelist.append(driver)  # Appending the variable into the list.

            import random  # Used to simulate the race.
            random.shuffle(namelist)  # Used to shuffle the names inside the list.

        position_list = []  # Creation of a list to store positions of drivers.
        for sublist in driverlist:
            position_list.append(driverlist.index(sublist)+1)

        points_list = [10, 7, 5]
        for sublist in driverlist:
            points_list.append(0)
        points_list.pop()
        points_list.pop()
        points_list.pop()

        # Allocating players from the shuffled list into variables.
        place1 = namelist[0]
        place2 = namelist[1]
        place3 = namelist[2]

        for sublist in driverlist:  # Getting the driver's initial points.
            if place1 in sublist:
                current_points = driverlist[driverlist.index(sublist)][4]
                new_points = int(current_points) + 10  # Adding the new points to the current points into the variable.

                # Rewriting the current points with the new points.
                driverlist[driverlist.index(sublist)][4] = new_points

        for sublist in driverlist:  # Getting the driver's initial points.
            if place2 in sublist:
                current_points = driverlist[driverlist.index(sublist)][4]
                new_points = int(current_points) + 7  # Adding the new points to the current points into the variable.

                # Rewriting the current points with the new points.
                driverlist[driverlist.index(sublist)][4] = new_points

        for sublist in driverlist:  # Getting the driver's initial points.
            if place3 in sublist:
                current_points = driverlist[driverlist.index(sublist)][4]
                new_points = int(current_points) + 5  # Adding the new points to the current points into the variable.

                # Rewriting the current points with the new points.
                driverlist[driverlist.index(sublist)][4] = new_points

        import random
        race_locations = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]

        # A random location will be chosen and be stored in the variable.
        todays_location = random.choice(race_locations)

        import datetime
        year_of_race = 2022  # All the races will happen in 2022.
        day_of_race = random.randrange(1, 31)  # Chooses a random number from 1 to 31
        month_of_race = random.randrange(1, 12)  # Chooses a random number from 1 to 12

        # Will output the dates in an orderly manner.
        race_date = datetime.date(year_of_race, month_of_race, day_of_race)

        # Appending all the variables into a list, so it can be accessed in other functions.
        racelist.append([todays_location, race_date, position_list, namelist, points_list])
        print(racelist)

        # Printing the Leaderboard.
        print(" < < < < < Today's Leaderboard > > > > > ")
        print("Location of the race : ", todays_location)
        print("Date of the race : ", race_date)
        print("First place  : ", place1)
        print("Second place : ", place2)
        print("Third place  : ", place3)

    else:
        print("SIMULATION FAILED. 3 or more drivers are required to run a simulation.")


def vrl():  # 7th FUNCTION - Viewing race details.

    global racelist  # Giving access to race details.

    updated_racelist = []  # Creation of a list to store the details sorted by date.

    import datetime

    temp_date = datetime.date(2022, 1, 1)  # Will act as an object to be compared with the entered dates.

    while len(racelist) > 0:  # A while loop to run the sort function until race details list is empty.
        for sublist in racelist:
            print(sublist)
            race_date = sublist[1]  # Extracting the dates from the race details list.
            if race_date > temp_date:  # Comparing the two dates.
                temp_date = race_date  # If new date is higher than temp date, new date will replace the temp date.

        for sublist in racelist:
            if temp_date in sublist:
                date_index = racelist.index(sublist)  # Finding the index of the element with the latest date.
                updated_racelist.append(racelist[date_index])
                racelist.pop(date_index)
                temp_date = datetime.date(2022, 1, 1)  # Resetting the temp_date.

    racelist = updated_racelist  # Rewriting the old list with the sorted list.

    for sublist in racelist:
        print("Location of the Race : ", sublist[0])
        print("Date of the Race : ", sublist[1])
        print("\n")

        print("| DRIVER POSITION |       DRIVER NAME        | DRIVER POINTS |")  # For the header of the table.

        for item in racelist: # Extracting the elements into a new list.
            list1 = item[2]
            list2 = item[3]
            list3 = item[4]

        for pos, name, point in zip(list1, list2, list3):  # Looping parallely through 3 lists
            print("|", pos, " " * (14 - len(str(pos))), "|", name, " " * (23 - len(name)), "|", point, " " *
                  (12 - len(str(point))), "|")

        print("\n")

        stf_racefile()


def stf_driverfile():  # 8th FUNCTION PART 1 - Saving driver details into a text file.

    driverfile = open("DRIVER_DETAIL_FILE.txt", 'w')  # creation of a text file.
    for sublist in driverlist:
        for x in sublist:
            driverfile.write(str(x) + ",")  # saving the information in driverlist in the text file.
        driverfile.write("\n")
    driverfile.close()

    print("DRIVER DETAILS HAVE BEEN SAVED.")


def stf_racefile():  # 8th FUNCTION PART 2 - Saving race details into a text file.

    racefile = open("RACE_DETAIL_FILE.txt", 'w')  # creation of a text file.
    for sublist in racelist:
        for x in sublist:
            racefile.write(str(x) + "|")  # saving the information in racelist in the text file.
        racefile.write("\n")
    racefile.close()

    print("RACE DETAILS HAVE BEEN SAVED.")


def rff():  # 9th FUNCTION - Loading saved race details , so it can be resumed through the program.

    from datetime import datetime  # Dates were dealt as datetime as supported by datetime library in py and not as strings.

    with open('DRIVER_DETAIL_FILE.txt') as f:  # Create text file.
        for line in f:
            x = line.strip().split(",")   # extracting information.
            x.pop(len(x)-1)
            driverlist.append(x)  # appending to the list.

    with open('RACE_DETAIL_FILE.txt') as f:
        for line in f:
            x = line.strip().split("|")   # Extracting information.
            x.pop(len(x)-1)
            points = x.pop(len(x) - 1)  # popping elements in lists.
            names = x.pop(len(x) - 1)
            positions = x.pop(len(x) - 1)
            dates = x.pop(len(x) - 1)

            points2 = points.strip("[").strip("]")  # Stripping unnecessary characters.
            m = points2.split(",")
            listpoints = [eval(i) for i in m]  # converting to integers.

            # Stripping unnecessary characters and replacing characters
            names2 = names.strip("[").strip("]").replace("'", "")
            n = names2.split(",")

            position2 = positions.strip("[").strip("]")  # Stripping unnecessary characters.
            o = position2.split(",")
            listpositions = [eval(i) for i in o]


            clock = datetime.strptime(dates, '%Y-%m-%d').date()  # converting strings into datetime object

            x.append(clock)
            x.append(listpositions)
            x.append(n)
            x.append(listpoints)  # appending extracted elements back into the race list.
            print(x)

    f.close()


while True:  # A while loop to keep the console going.

    print_menu()
    choice = input("Enter your choice >>> ")
    option = choice.upper()  # If users enters the three letters in lower case it will be turned into upper case.

    if option == "ADD":
        add()  # Calling the add driver details function.
    elif option == "DDD":
        ddd()  # Calling the delete driver details function.
    elif option == "UDD":
        udd()  # Calling the update driver details function.
    elif option == "VCT":
        vct()  # Calling the view championship table function.
    elif option == "SRR":
        srr()  # Calling the simulate random race function.
    elif option == "VRL":
        vrl()  # Calling view all the races function.
    elif option == "STF":
        stf_driverfile()  # Calling the function to create a driver details file.
        stf_racefile()   # Calling the function to create a race details file.
    elif option == "RFF":
        rff()  # Calling the function to load saved text files in to the system.
    elif option == "ESC":
        print("THANK YOU FOR USING WORLD RALLY CROSS CHAMPIONSHIP MANAGEMENT SYSTEM. HAVE A GOOD DAY! ")
        exit()  # Will quit the program.

