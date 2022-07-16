import random
import time

time.sleep(.01)
# Craig Nelson
# IT 140 J5094 Introduction to Scripting 21EW5
# MileStone Seven



# The dictionary of Rooms according to the map.
# Items will be shuffled after every restart
rooms = {
    'Entrance Way': {
        'North': 'Powder Blue Room',
        'East': 'Dark Blue Room',

        'West': 'Orange Room'},
    'Orange Room': {
        'North': 'Pink Room',
        'East': 'Entrance Way',
        'item': 'item'},
    'Pink Room': {
        'North': 'Red Room',
        'East': 'Powder Blue Room',
        'South': 'Orange Room',
        'item': 'item'},
    'Red Room': {
        'East': 'Yellow Room',
        'South': 'Pink Room',
        'item': 'item'},
    'Yellow Room': {
        'East': 'Light Green Room',
        'South': 'Powder Blue Room',
        'West': 'Red Room',
        'item': 'item'},
    'Light Green Room': {
        'South': 'Green Room',
        'West': 'Yellow Room',
        'item': 'item'},
    'Green Room': {
        'North': 'Light Green Room',
        'West': 'Powder Blue Room',
        'South': 'Dark Blue Room',
        'item': 'item'},
    'Dark Blue Room': {
        'North': 'Green Room',
        'West': 'Entrance Way',
        'item': 'item'},
    'Powder Blue Room': {
        'North': 'Yellow Room',
        'East': 'Green Room',
        'South': 'Entrance Way',
        'West': 'Pink Room',
        'item': 'item'}
}

# Why the shuffle, so the game is more fun. The villain is not located in the same room everytime.
# The 7 items will be shuffled in 9 rooms, the remaining 2 are the Entrance way and the room containing the villain.
def shuffle():
    items = ['Knapsack', 'Sword', 'Medusa', 'Helm of Darkness', 'pair of Winged sandals', 'Polished shield', 'Bow and Arrow',
             'Axe']
    random.shuffle(items)
    i = 0
    for room in rooms:
        if 'item' in rooms[room]:
            rooms[room]['item'] = items[i]
            i = i + 1


# function for displaying introduction and instructions on how to play the game. with pauses to read.

def introduction():
    print("[1;35;50m ")
    print()
    print('                   | |                 ')
    print(' _ __ ___   ___  __| |_   _ ___  __ _  ')
    print('|  _   _  / _ / _  | | | / __|/ _` | ')
    print('| | | | | |  __/ (_| | |_| __  (_| | ')
    print('|_| |_| |_|___|__,_|__,_|___/__,_| ')
    print()
    print("A Story from Greek Mythology")
    print()
    print()
    print()
    time.sleep(1.5)
    print('Hello! And Welcome to the Medusa Text Game.')
    print('Your mission is to travel to the island named Sarpedon and Enter the temple of Medusa and behead her.')
    print('Medusa is so hideous that anyone who lays eyes on her will turn to stone.')
    print('As you travel through the temple you will encounter stone statues of warriors that have tried to behead Medusa before you.')
    print()
    time.sleep(3.0)
    print('The gods have graced you by supplying you with items. Each room contains one item.')
    print('The items are:')
    print('     1.	Knapsack to hold Medusas Head.')
    print('     2.	An adamantine sword')
    print('     3.	Hades  helm of darkness – renders wearer invisible.')
    print('     4.	A pair of winged sandals')
    print('     5.	A polished shield')
    print('     6.	A bow and arrow')
    print('     7.	A Two-Headed Axe.')
    print()
    time.sleep(3.0)
    print('Play: You will start in the entrance way. You can travel North-East-West from there by entering a direction.')
    print('(i.e., North) in the prompt. Once you leave the Entrance Way.')
    print('You travel from room to room gathering items into your inventory.')
    print()
    print('Navigation: You enter in directions you want to travel, if you enter in a direction that is unavailable')
    print('the response will be : "You can’t go that way."')
    print()
    time.sleep(3.0)
    print('To Win: You must have all seven items in your inventory and then encounter Medusa and behead her.')
    print()
    print('A Loss: You encounter Medusa without having all seven items in your inventory.')
    print()
    print("Move commands: North, East, South, West")
    print("To pick up an item response is 'Y'")
    print("Type Exit to quit game")
    time.sleep(1.0)

# the main function where all the logic for the game is scripted.
def main():
    introduction()
    # Defining some variables and putting player in beginning for the directions
    directions = ['North', 'South', 'East', 'West']
    # Starting Room
    current_room = 'Entrance Way'
    # Inventory list to hold inventory as it's added in each room
    inventory = []
    # Calling shuffle function
    shuffle()
    while True:
        # display current location and inventory North
        print()
        print('You are in {}.'.format(current_room))
        print('Your current inventory: {}'.format(inventory))
        # winning logic-Does player have all items? Congrats message.
        if 'item' in rooms[current_room]:
            if rooms[current_room]['item'] == 'Medusa':
                if len(inventory) == 7:
                    print('You have collected all the items the gods have bestowed upon you!')
                    print()
                    print('You located the Medusa and beheaded her.')
                    print('Congratulations!')
                else:
                    # losing code player encountered medusa before have all items
                    time.sleep(1.0)
                    print()
                    print('You have encountered the hideous gaze of the Medusa.')
                    print()
                    print('You have been turned to Stone!!! Game Over  :(  ')
                break
            item = rooms[current_room]['item']
            if item in inventory:  # check if player already has item
                print("You already have this item", item)
            else:
                print()
                print('You see a', item)
                print('Would you like to pick it up? ')
                user_item = input('')
                if user_item.upper() == 'Y':  # the answer is y or Y
                    print('The item has been added to Inventory.')
                    inventory.append(item)
                else:
                    print('You leave the item behind.') # player may already have item

        # What direction will player go? N E S W
        command = input('What direction will you go? ').strip().capitalize()

        # Move Player in that direction
        if command in directions:
            if command in rooms[current_room]:
                current_room = rooms[current_room][command]
            else:
                # If player is unable to move in that direction
                print("You can't go that way.")
        # Allow player to Exit the game
        elif command == 'Exit':
            break
        # If Player response is not recognized
        else:
            print("That is an invalid command.")

# Calling the main function
if __name__ == '__main__':
    main()
