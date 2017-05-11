katz_deli = []
#1. line() function
def line(people_waiting):
    if len(people_waiting) > 0:
        people_string = "The line is currently:"
        for i in range(0, len(people_waiting)):
            people_string += " " + str(i + 1) + ". " + people_waiting[i]
        return people_string
    else:
        return "The line is currently empty."

#2. take_a_number function
def take_a_number(waiting_list, name):
    waiting_list.append(name)
    ##katz_deli.append(name)
    place_in_line = waiting_list.index(name) + 1
    return "Welcome, " + name + ". You are number " + str(place_in_line) + " in line."

#3. now_serving() function
def now_serving(waiting_list):
    if len(waiting_list) > 0:
        current_customer = waiting_list.pop(0)
        return "Currently serving " + current_customer + "."
    else:
        return "There is nobody waiting to be served!"
