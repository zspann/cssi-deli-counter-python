# Deli Counter - Take a Number

## Objectives
1. Practice building functions that use iteration and controlling their return values.
2. Practice manipulating lists (adding elements, removing elements, etc.).

## Instructions

The local deli is putting in a new computerized queue to keep track of their customers and improve productivity. At the beginning of the day, the deli is empty so the queue should be represented by an empty list:

```python
katz_deli = []
```

Write all of your code in `deli.py`


1. Build the `line` function that shows everyone their current place in the line. If there is nobody in line, it should say `"The line is currently empty."`.

2. Build a function that a new customer will use when entering the deli. The `take_a_number` function should accept two arguments, the list for the current line of people (`katz_deli`), and a string containing the name of the person wishing to join the line. The function should return the person's name along with their position in line. **Top-Tip:** *Remember that people like to count from* `1`*, not from* `0` *("zero") like in Python.*

3. Build the `now_serving` function which should call out (i.e. `print`) the next person in line and then remove them from the front. If there is nobody in line, it should call out (`print`) that `"There is nobody waiting to be served!"`.


Example usage:

  ```print
  katz_deli = []

  take_a_number(katz_deli, "Jerry") #=> 1
  take_a_number(katz_deli, "Elaine") #=> 2
  take_a_number(katz_deli, "George") #=> 3

  line(katz_deli) #=> "The line is currently: 1. Jerry 2. Elaine 3. George"

  now_serving(katz_deli) #=> "Currently serving Jerry."

  line(katz_deli) #=> "The line is currently: 1. Elaine 2. George"

  take_a_number(katz_deli, "Kramer") #=> 3

  line(katz_deli) #=> "The line is currently: 1. Elaine 2. George 3. Kramer"

  now_serving(katz_deli) #=> "Currently serving Elaine."

  line(katz_deli) #=> "The line is currently: 1. George 2. Kramer"
  ```
