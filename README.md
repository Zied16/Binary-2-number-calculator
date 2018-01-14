# Binary-2-number-calculator
When i was a student in high school studying binary code i used to get stuck sometimes figuring out how to add 2 numbers
or how to substract them so when i got i little comfortable with python i tried to create a calculator that can do it for
me. This may be already done or there are apps available that can do it for you but i wanted one that is my own so i searched for
a tutoriel that could help me and just did it.
For the time being it can just handle 2 numbers and it can do addition and substraction.
The addition is straight forward you just enter 2 number and it gives you the binary sum.
The substraction was the difficult part for me i had to implement the strategie i own which takes 2 numbers changes one of them
(each 0 is converted to a 1 and each 1 to a 0) adds 1 to that number and adds it to the remaining one. You read the result as
usual expect that there is an entry that tells if the number is negative or positive which is before the last entry from the left.
The way to code works:
You enter 2 numbers seperated by + or - like in a normal calculator depending on the seperated an addiction or a substraction 
function is activated.
The numbers are read as a string then converted to a list using 'split' the each part of the list represent the first number and 
the second one.
Transforms each to a number number list( for example ['101'] would become ['1','0','1']) that converts each part to an integer.
Reverses the two lists so that a normal for loop would do the sum same as you would do it on paper.
Does the same addition as you would do by hand and adds the results in a newer list each created with the same length as the
starting numbers.
when you reach the end you either append if you still have 1 to add or you are done.
converts the result into a string and prints in the display.
During this project a got frustrated as some actions would work normally in the shell but not in the script.
