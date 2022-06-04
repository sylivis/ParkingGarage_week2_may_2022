class Parking_Garage():
                
                
    def __init__(self, parking_spaces, parking_price):
        
        self.parking_price = float(parking_price) 

        self.parking_spaces_list = [ps for ps in range(int(parking_spaces))]

        self.parking_spaces_avail = len(self.parking_spaces_list)
        
        self.tickets_list = self.parking_spaces_list.copy() 

        self.current_ticket = {self.parking_spaces_list[i]: self.tickets_list[i] for i in range(parking_spaces)}    


    def takeTicket(self):
        try:
            ticket_given = self.tickets_list.pop(0)                 #This should decrease the amount of tickets available by 1  
            spaces_unavailable = self.parking_spaces_list.pop(0)    #This should decrease the amount of parkingSpaces available by 1 
            print(f"You have ticket number {ticket_given}. Please park in space {spaces_unavailable}.")
            print("Ticket Given. Park Safley")
        except:
            print("There are no parking spaces available.")
        

    def payForParking(self, ticket_number): 
        #any implimentation of this should check that the ticket_number given does not appear on self.tickets_list
        
        amount_owed = self.parking_price

        paying = True
        while paying == True:
            try:
                paid = input(f"You Owe {str(amount_owed)}\n How much tender is accepted?")    #Display an input that waits for an amount from the user and store it in a variable
                print(f"{paid} paid")
                amount_owed -= float(paid)

                if amount_owed == 0.0:
                    #This should update the "currentTicket" dictionary key "paid" to True
                    self.current_ticket[ticket_number] = "True"
                    paying = False
                if amount_owed < 0:
                    #This should update the "currentTicket" dictionary key "paid" to True
                    print(f"Change to give back: {str(abs(amount_owed))}")
                    self.current_ticket[ticket_number] = "True"
                    paying = False

            except:
                answer = input("Are you trying to go back without paying? (y or n)").lower()
                if answer == "y":
                    paying = False

        if self.current_ticket[ticket_number] == "True":
            #If the payment variable is not empty then (meaning the ticket has been paid) 
            #display a message to the user that their ticket has been paid and they have 15mins to leave

            print("Your ticket has been paid and you have 15 mins to leave. Have a nice day!")    
        else:                                                                                     
            print("your ticket has not been paid. Be sure to pay before you leave")
        
    
    def leaveGarage(self, ticket_number):    

        #any implimentation of this should check EITHER that the ticket_number given does not appear on self.tickets_list, 
        #or that self.current_ticket[ticket_number] != ticket_number   

        if self.current_ticket[ticket_number] == "True":
            print("have a nice day!") #If the ticket has been paid, display a message of "Thank You, have a nice day"

            self.parking_spaces_list.append(ticket_number)    #Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list) 
            self.tickets_list.append(ticket_number)           #Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list) 
            
            self.current_ticket[ticket_number] = ticket_number #Resets current ticket so it may be used again

        if self.current_ticket[ticket_number] != "True":
            leaving = True
            print("You have to pay before you leave!")
            while leaving == True:
                res = input("Do you want to pay now?(y or n)").lower()
                if res == "y":
                    self.payForParking(ticket_number) #If the ticket has not been paid, display an input prompt for payment
                    if self.current_ticket[ticket_number] != "True":
                        continue
                    print("have a nice day") #Once paid, display message "Thank you, have a nice day!"
                    self.parking_spaces_list.append(ticket_number) #Update parking_spaces list to increase by 1 (meaning add to the parkingSpaces list)
                    self.tickets_list.append(ticket_number)        #Update tickets_list list to increase by 1 (meaning add to the parkingSpaces list) 
                    self.current_ticket[ticket_number] = ticket_number #Resets current ticket so it may be used again
                    leaving = False
                if res == "n":
                    print("You have not payed. You may not take your vehicle out of the garrage until you pay.")
                    leaving = False




