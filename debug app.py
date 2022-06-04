import parking_garage as main

a = main.Parking_Garage(20, 1.0)
on = True
while on == True:
    res = input("a: parking_spaces_list b:parking_spaces_avail c:ticketts_list d:current_ticket)\nq:quit\n e:takeTickett f:pay g:leave" ).lower()
    try:
        if res == "a":
           print(a.parking_spaces_list)
        if res == "b":
           print(a.parking_spaces_avail)
        if res == "c":
           print(a.tickets_list)
        if res == "d":
           print(a.current_ticket)
        if res == "e":
           a.takeTicket()
        if res == "f":
           a.payForParking(int(input("what is your ticket number")))
        if res == "g": 
            a.leaveGarage(int(input("what is your ticket number")))
    except:

        print("something went wrong. try again.")