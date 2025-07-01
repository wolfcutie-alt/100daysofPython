#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

puts "Welcome to the PyPassword Generator!"

print "How many letters would you like in your password? "
nr_letters= gets.chomp.to_i

print "How many symbols would you like? "
nr_symbols = gets.chomp.to_i

print "How many numbers would you like? "
nr_numbers = gets.chomp.to_i

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = []

# for _ in 0...nr_letters do
#   password << letters[Random.rand(nr_letters)]
# end

# for _ in 0...nr_symbols do
#   password << symbols[Random.rand(nr_symbols)]
# end

# for _ in 0...nr_numbers do
#     password << numbers[Random.rand(nr_numbers)]
# end

# puts password.join

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
hard_password = []

for _ in 0...nr_letters do
  password << letters[Random.rand(nr_letters)]
end

for _ in 0...nr_symbols do
  password << symbols[Random.rand(nr_symbols)]
end

for _ in 0...nr_numbers do
    password << numbers[Random.rand(nr_numbers)]
end

for _ in 0...password.length do
    hard_password << password[Random.rand(password.length)]
end

puts hard_password.join