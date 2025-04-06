# Rock Paper Scissors Game with Scoreboard
# Developed by Sai Teja Digavalli
import random

choices = ["Rock", "Paper", "Scissor"]
player_score = 0
computer_score = 0

print("🎮 Welcome to the Rock Paper Scissors Game!")

while True:
    player_choice = input("Enter your choice (Rock, Paper, Scissor): ").capitalize()
    computer_choice = choices[random.randint(0,2)]
    
    if player_choice not in choices:
        print("❗ Invalid choice. Please choose Rock, Paper, or Scissor.")
        continue

    print(f"🧠 Computer's Choice: {computer_choice}")

    if player_choice == computer_choice:
        print("🤝 It's a TIE!")
    elif (player_choice == "Rock" and computer_choice == "Scissor") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissor" and computer_choice == "Paper"):
        print(f"🏆 You WIN! {player_choice} beats {computer_choice}")
        player_score += 1
    else:
        print(f"😞 You LOSE! {computer_choice} beats {player_choice}")
        computer_score += 1

    
    print(f"📊 Current Score — You: {player_score} | Computer: {computer_score}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("👋 Final Scores:")
        print(f"🧑 You: {player_score} | 🤖 Computer: {computer_score}")
        if player_score > computer_score:
            print("🏅 Congratulations, you won the game!")
        elif player_score < computer_score:
            print("💔 Sorry, the computer won the game!")
        else:
            print("🤝 It's a draw!")
        print("Thanks for playing! Goodbye.")
        break
