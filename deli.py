katz_deli = []
#1. line() function
def line(people_waiting):
    if len(people_waiting) > 0:
        people_string = []
        for i in range(0, len(people_waiting)):
            num = str(i + 1)
            people_string.append(num + ". " + people_waiting[i])
        people_string = " ".join(people_string)
        return "The line is currently: " + people_string
    else:
        return "The line is currently empty."

#2. take_a_number function
def take_a_number(list, name):
    list.append(name)
    katz_deli.append(name)
    place_in_line = list.index(name) + 1
    return "Welcome, " + name + ". You are number " + str(place_in_line) + " in line."

#3. now_serving() function
def now_serving(list):
    if len(list) > 0:
        return "Currently serving " + list[0] + "."
        del list[0]
    else:
        return "There is nobody waiting to be served!"
