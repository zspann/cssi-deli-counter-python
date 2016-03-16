
#1. line() function
def line(customer_list):
    if len(customer_list)==0:
        message="The line is currently empty."
    else:
        message="The line is currently:"
        for num, name in enumerate(customer_list):
            message += " {}. {}".format(num+1,name)
    return message

#2. take_a_number function
def take_a_number(customer_list, name):
  customer_list.append(name)
  return "Welcome, {}. You are number {} in line.".format(name, len(customer_list))

#3. now_serving() function
def now_serving(customer_list):
 if len(customer_list)==0:
    message= "There is nobody waiting to be served!"
 else:
    message= "Currently serving {}.".format(customer_list[0])
    del customer_list[0]
 return message
#katz_deli=["Nicki", "Rob", "Norah"]
#print line(katz_deli)
#print take_a_number(katz_deli,"Bernie")
#print now_serving(katz_deli)
#print now_serving(katz_deli)
#print katz_deli
#print now_serving(katz_deli)
