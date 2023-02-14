# File: addressbook.py
# Author: Sara Vanaki and Benjamin Berube
# Date: 02/26/2020
# Description: Address Book Code

import tkinter as tk

class Address:
    def __init__(self, name, street, city, state, _zip):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = _zip
       
class AddressBook:
    def __init__(self):
        """ Constructor for AddressBook class """

        # Create window.
        self.window = tk.Tk()  
        self.window.title("AddressBook") 
        self.window.geometry("650x200")
        self.DEFAULT_GREETING_STRING = "            "
        self.list = []
        self.count = 0      #this is where we will keep track of where we are in our file
        #add top frame
        self.top_frame = tk.Frame(self.window)
        self.top_frame.grid(row = 1, column =1)

        #add middle frame
        self.middle_frame = tk.Frame(self.window)
        self.middle_frame.grid(row = 2, column = 1)

        #add bottom frame
        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.grid(row = 3, column = 1)

        #add name label
        self.name_label = tk.Label(self.top_frame, text = "Name")
        self.name_label.grid(row = 1, column = 1, sticky = "W", padx = 10, pady = (10, 2))

        #add name field 
        self.name = tk.Entry(self.top_frame)
        self.name.grid(row = 1, column = 2, columnspan = 4, sticky = "W", padx = 10, pady = (10, 2))
        #add street label
        self.street_label = tk.Label(self.top_frame, text = "Street")
        self.street_label.grid(row = 2, column = 1, sticky = "W", padx = 10, pady = (10, 2))
        #add street field
        self.street = tk.Entry(self.top_frame)
        self.street.grid(row = 2, column = 2, sticky = "W", padx = 10, pady = (10, 2))
        #add city label
        self.city_label = tk.Label(self.top_frame, text = "City")
        self.city_label.grid(row = 3, column = 1, sticky = "W", padx = 10, pady = (10, 2))
        #add city field
        self.city = tk.Entry(self.top_frame)
        self.city.grid(row = 3, column = 2, sticky = "W", padx = 10, pady = (10, 2))
        #add state label 
        self.state_label = tk.Label(self.top_frame, text = 'State')
        self.state_label.grid(row = 3, column = 3, sticky = "W", padx = 10, pady = (10, 2))
        #add state field
        self.state = tk.Entry(self.top_frame)
        self.state.grid(row = 3, column = 4, sticky = "W", padx = 10, pady = (10, 2))
        #add zip label
        self.zip_label = tk.Label(self.top_frame, text = 'Zip')
        self.zip_label.grid(row = 3, column = 5, sticky = "W", padx = 10, pady = (10, 2))
        #add zip field
        self.zip = tk.Entry(self.top_frame)
        self.zip.grid(row = 3, column = 6, sticky = "W", padx = 10, pady = (10, 2))


        #add ADD button
        self.add_button = tk.Button(self.middle_frame, text = 'Add', command = self.add)
        self.add_button.grid(row = 1, column = 1, sticky = "W", padx = 10, pady = (10, 2))
        #add DELETE button
        self.delete_button = tk.Button(self.middle_frame, text = 'Delete', command = self.delete)
        self.delete_button.grid(row = 1, column = 2, sticky = "W", padx = 10, pady = (10, 2))
        #add FIRST button
        self.first_button = tk.Button(self.middle_frame, text = 'First', command = self.first)
        self.first_button.grid(row = 1, column = 3, sticky = "W", padx = 10, pady = (10, 2))
        #add NEXT button
        self.next_button = tk.Button(self.middle_frame, text = 'Next', command = self.next)
        self.next_button.grid(row = 1, column = 4, sticky = "W", padx = 10, pady = (10, 2))
        #add PREVIOUS button
        self.previous_button = tk.Button(self.middle_frame, text = 'Previous', command = self.previous)
        self.previous_button.grid(row = 1, column = 5, sticky = "W", padx = 10, pady = (10, 2))
        #add LAST button
        self.last_button = tk.Button(self.middle_frame, text = 'Last', command = self.last)
        self.last_button.grid(row = 1, column = 6, sticky = "W", padx = 10, pady = (10, 2))
        
        
        #add filename label
        self.filename_label = tk.Label(self.bottom_frame, text = 'Filename')
        self.filename_label.grid(row = 1, column = 1, sticky = "W", padx = 10, pady = (10, 2))
        
        #add filename field
        self.filename = tk.Entry(self.bottom_frame)
        self.filename.grid(row = 1, column = 2,sticky = "W", padx = 10, pady = (10, 2))
        
        #add load file button
        self.load_file = tk.Button(self.bottom_frame, text = 'Load File', command = self.load_the_file)
        self.load_file.grid(row =1, column = 3, sticky = "W", padx = 10, pady = (10, 2))
        
        #add SAVE TO FILE button
        self.save_to_file = tk.Button(self.bottom_frame, text = 'Save to File', command = self.save_file)
        self.save_to_file.grid(row = 1, column = 4, sticky = "W", padx = 10, pady = (10, 2))

        #add QUIT button
        self.quit_button = tk.Button(self.bottom_frame, text = 'Quit', command = self.quit)
        self.quit_button.grid(row =1, column = 5, sticky = "W", padx = 10, pady = (10, 2))
        
        # Start the event loop
        self.window.mainloop()

    #our methods are presented below
    def add(self):
        #print('add')
        name = self.name.get()
        street = self.street.get()
        city = self.city.get()
        state = self.state.get()
        _zip = self.zip.get()
        new_address = Address(name,street,city,state,_zip)
        self.list.append(new_address)
        
        self.name.delete(0,'end')       #delete the stuff in the entries as of rn, to add the first object in the list to show user
        self.street.delete(0,'end')
        self.city.delete(0,'end')
        self.state.delete(0,'end')
        self.zip.delete(0,'end')
        
    def delete(self):
        #get rid of info on these entries first
        self.name.delete(0,'end')       
        self.street.delete(0,'end')
        self.city.delete(0,'end')
        self.state.delete(0,'end')
        self.zip.delete(0,'end')
        #get rid of this entry from our list
        del self.list[self.count]
        self.count -= 1

        #display this info of the 'next addy' onto the entries, check if there EXISTS a next addy
        if self.count + 1 < len(self.list):
            next_address = self.list[self.count]
            self.name.insert(0,next_address.name)
            self.street.insert(0,next_address.street)
            self.city.insert(0,next_address.city)
            self.state.insert(0,next_address.state)
            self.zip.insert(0,next_address.zip)
        print('delete')
        #print(self.list)
    def first(self):
        self.name.delete(0,'end')       #delete the stuff in the entries as of rn, to add the first object in the list to show user
        self.street.delete(0,'end')
        self.city.delete(0,'end')
        self.state.delete(0,'end')
        self.zip.delete(0,'end')

        if len(self.list) > 0:
            first_address = self.list[0]
            self.count = 0          #set the count to 0 so that we have a starting point of when we iterate thru the list
            self.name.insert(0,first_address.name)
            self.street.insert(0,first_address.street)
            self.city.insert(0,first_address.city)
            self.state.insert(0,first_address.state)
            self.zip.insert(0,first_address.zip)
        #print('first')
    def next(self):
        if self.count + 1 < len(self.list):
            self.count += 1
            next_address = self.list[self.count]

            #get rid of info on these entries first
            self.name.delete(0,'end')       #delete the stuff in the entries as of rn, to add the first object in the list to show user
            self.street.delete(0,'end')
            self.city.delete(0,'end')
            self.state.delete(0,'end')
            self.zip.delete(0,'end')

            #display this info onto the entries
            self.name.insert(0,next_address.name)
            self.street.insert(0,next_address.street)
            self.city.insert(0,next_address.city)
            self.state.insert(0,next_address.state)
            self.zip.insert(0,next_address.zip)

        #print('next')
        
    def previous(self):
        if self.count - 1 >= 0:
            self.count -= 1
            prev_address = self.list[self.count]
            #get rid of info on these entries first
            self.name.delete(0,'end')       #delete the stuff in the entries as of rn, to add the first object in the list to show user
            self.street.delete(0,'end')
            self.city.delete(0,'end')
            self.state.delete(0,'end')
            self.zip.delete(0,'end')

            #display this info onto the entries
            self.name.insert(0,prev_address.name)
            self.street.insert(0,prev_address.street)
            self.city.insert(0,prev_address.city)
            self.state.insert(0,prev_address.state)
            self.zip.insert(0,prev_address.zip)
        #print('previous')
    def last(self):
        if len(self.list) != 0:
            self.count = len(self.list) - 1
            last_address = self.list[-1]
            #get rid of info on these entries first
            self.name.delete(0,'end')       #delete the stuff in the entries as of rn, to add the first object in the list to show user
            self.street.delete(0,'end')
            self.city.delete(0,'end')
            self.state.delete(0,'end')
            self.zip.delete(0,'end')

            #display this info onto the entries
            self.name.insert(0,last_address.name)
            self.street.insert(0,last_address.street)
            self.city.insert(0,last_address.city)
            self.state.insert(0,last_address.state)
            self.zip.insert(0,last_address.zip)
        #print('last')
    def quit(self):
        self.window.destroy()

    def load_the_file(self):
        #first you have to get the file from the entry
        the_file = self.filename.get()
        #check if they even wrote anything in the filename area
        if the_file != '':
            infile = open(the_file, 'r')
            #have to reset the list and also the counter
            self.count = 0
            self.list = []
            #Iterating through the file and stripping
            for line in infile:
                name= line
                name = name.replace("\n", '')\
                
                street = infile.readline()
                street = street.replace("\n", '')

                city = infile.readline()
                city = city.replace("\n", '')

                state = infile.readline()
                state = state.replace("\n",'')

                zipcode = infile.readline()
                zipcode = zipcode.replace("\n",'')

                new_address = Address(name,street,city,state,zipcode) 
                #Appending to the list
                self.list.append(new_address)
            infile.close()
            #now we have to put the first object(address) into the entries so the user can see they loaded the file
            first_address = self.list[0]
            self.name.insert(0,first_address.name)
            self.street.insert(0,first_address.street)
            self.city.insert(0,first_address.city)
            self.state.insert(0,first_address.state)
            self.zip.insert(0,first_address.zip)
        #print('load file')
    def save_file(self):
        filename = self.filename.get()
        if filename != "":
            the_file = open(filename, "w")
        else:
            the_file = open(filename, 'a')
            #Taking each component inside the window and writing it into an open file. When the button is clicked, the content is added line by line and it is erased from the window
        for address in self.list:
            name = address.name
            the_file.write(name + "\n")

            street = address.street
            the_file.write(street + "\n")

            city = address.city
            the_file.write(city + '\n')

            state = address.state
            the_file.write(state + '\n')

            _zip = address.zip
            the_file.write(_zip + '\n')

        self.name.delete(0,'end')       #delete the stuff in the entries as of rn, to add the first object in the list to show user
        self.street.delete(0,'end')
        self.city.delete(0,'end')
        self.state.delete(0,'end')
        self.zip.delete(0,'end')
        self.filename.delete(0,'end')
        

        the_file.close()





    
    # You will add other methods.

if __name__ == "__main__":
    # Create GUI
    AddressBook()
