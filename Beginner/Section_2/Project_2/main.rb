#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

puts "Welcome to the tip calculator!"
print "What was the total bill? "
bill = gets.chomp.to_f

print "How much tip would you like to give? 10, 12, or 15? "
tip = gets.chomp.to_f

print("How many people to split the bill? ")
people = gets.chomp.to_f

amount_paid = (bill * (1 + tip / 100)) / people
amount = amount_paid.round(2)
puts "Each person should pay: $" << amount.to_s