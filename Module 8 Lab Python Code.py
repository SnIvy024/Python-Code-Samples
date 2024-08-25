class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)


# Your Name: Ivette Mujica
# The Date: 08/24/2024
# Problem 5 - The program checks whether the game character has the necessary items and no conflicting debuffs to perform specific tasks.


def check_task_requirements(player, task_name, required_items, forbidden_debuffs):
   
    has_all_items = all(item in player.weapons for item in required_items)
    has_no_debuffs = all(debuff not in player.weaknesses for debuff in forbidden_debuffs)
    
    if has_all_items and has_no_debuffs:
        print(f"{player.nickname} can successfully perform the task: {task_name}.")
    else:
        print(f"{player.nickname} cannot perform the task: {task_name}.")
        if not has_all_items:
            print(f"Missing items: {[item for item in required_items if item not in player.weapons]}")
        if not has_no_debuffs:
            print(f"Conflicting debuffs: {[debuff for debuff in forbidden_debuffs if debuff in player.weaknesses]}")

# Define the player character

player1 = character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

# Checking if the player can perform the tasks

check_task_requirements(player1, "Climb a mountain", ['rope', 'coat', 'first aid kit'], ['slow'])
check_task_requirements(player1, "Cook a meal", ['pan', 'groceries'], ['small'])
check_task_requirements(player1, "Write a book", ['pen', 'paper', 'idea'], ['confusion'])
