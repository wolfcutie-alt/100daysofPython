rock = <<-TEXT
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
TEXT

paper = <<-TEXT
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
TEXT

scissors = <<-TEXT
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
TEXT

#Write your code below this line 👇

choices_list = [rock, paper, scissors]

puts "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
user_choice = gets.chomp.to_i
puts "You choose: "
puts choices_list[user_choice]

computer_choice = Random.rand(1...3)
puts "Computer choice: \n" << choices_list[computer_choice]

if user_choice == computer_choice
    puts "Draw"
else
    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1)
            puts "User Win!"
    else
        puts "Computer Win!"  
    end   
end