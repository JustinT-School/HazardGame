# Name: Justin Tuder
# Assignment: Final Project
# Description: Design an approved project. In this case, I was approved to make the game Hazard.
#               It is an old English dice game with slightly confusing rules and is the precursor
#               to the modern game of craps.
#
# Revision: 1	Date: 12/04/2021		Initials: JT	Description of Changes: Initial setup
# Revision: 2   Date: 12/06/2021        Initials: JT    Description of Changes: Project cleanup

# Imports
from guizero import *
import random


def main():  # Main Function
    def select_main():  # Shows the window that allows you to pick your number
        start_game_button.enabled = False  # Disable the start new game button

        intro_window.visible = False  # Hide the intro window
        game_window.visible = False  # Make sure the game window is hidden if starting a new game after playing one
        result_window.visible = False  # Make sure the results window is hidden if starting a new game after playing one
        main_select.visible = True  # Show the window that allows you to pick your number

    def start_game(number: int):  # Takes the number you select and sets it
        main_select.visible = False  # Hide the window that lets you pick your number
        game_window.visible = True  # Show the actual game window

        roll_button.visible = True  # Show the button that allows you to roll

        result_spacing.visible = True  # Used for layout spacing to make things look better
        results.visible = True  # Shows the helper text at the top of the screen
        results.value = "Please roll the dice!"  # Sets the helper text

        main_text.value = f"Main: {number}"  # Shows the Main value to the player to make things easier
        chance_text.value = "Chance: "  # Shows the Chance value as empty because it has not been filled yet

        first_throw.value = "True"  # Sets first throw to true

        caster.value = str(number)  # Sets the value selected and converts it to a string

    #   The roll_dice function is where the game itself is run. It generates the dice rolls and uses those
    #   to determine what to do next. This will continue every time the roll dice button is pressed until the game
    #   is won or lost.
    def roll_dice():  # Randomly selects two numbers, each between 1 and 6 to simulate rolling six-sided dice
        roll_one = random.randint(1, 6)  # Randomly picks number for first dice
        roll_two = random.randint(1, 6)  # Randomly picks number for second dice
        number_rolled = roll_one + roll_two  # Adds both numbers together for total rolled

        dice_one.value = str(roll_one)  # Converts the first number rolled to a string and sets the value of dice_one
        dice_two.value = str(roll_two)  # Converts the second number rolled to a string and sets the value of dice_two

        def update_dice_image(roll: int, image: dice_one_image):  # Changes the images of the dice
            #   Dictionary of images to use for different values rolled
            image_select = {1: 'images/dice1.png',
                            2: 'images/dice2.png',
                            3: 'images/dice3.png',
                            4: 'images/dice4.png',
                            5: 'images/dice5.png',
                            6: 'images/dice6.png'}

            image.image = image_select[roll]    # Sets the image for the corresponding dice

        update_dice_image(roll_one, dice_one_image)  # Updates the first dice image
        update_dice_image(roll_two, dice_two_image)  # Updates the second dice image

        def win_game():  # Called when the game is won
            result_window.visible = True  # Shows the window that tells you that you've won
            game_window.visible = False  # Hides the game window
            play_again.value = f"You rolled {number_rolled}, you win!"  # Updates text shown
            start_game_button.enabled = True  # Enables the start new game button

        def lose_game():  # Called when the game is lost
            result_window.visible = True  # Shows the window that tells you that you've won
            game_window.visible = False  # Hides the game window
            play_again.value = f"You rolled {number_rolled}, you lose!"  # Updates the text shown
            start_game_button.enabled = True  # Enables the start new game button

        if first_throw.value == "False":  # For rolls after your first throw
            if str(number_rolled) == chance.value:  # Checks to see if the number you rolled is the same as the previous
                print("You win!")  # Prints to the terminal for debug
                win_game()  # Calls the function for a win
            elif str(number_rolled) == caster.value:  # Checks if the number rolled is the same as the number selected
                print("You lose!")  # Prints to the terminal for debug
                lose_game()  # Calls the function for a loss
            else:  # If you neither won nor lost
                print(number_rolled)  # Prints to the terminal for debug
                results.value = f"You rolled {number_rolled}, please roll again."  # Updates the result text

        if first_throw.value == "True":  # Checks to see if this is your first roll
            chance.value = str(number_rolled)  # Sets the player's chance to the first number rolled

            if chance.value == caster.value:  # Checks to see if the number rolled is the same as the number chosen
                print("You win!")  # Prints to the terminal for debug
                win_game()  # Calls the function for a win
            elif (caster.value == "6" or caster.value == "8") and (chance.value == "12"):
                print("You rolled a 12, you win!")  # Prints to the terminal for debug
                win_game()  # Calls the function for a win
            elif (caster.value == "7") and (chance.value == "11"):
                print("You rolled an 11, you win!")  # Prints to the terminal for debug
                win_game()  # Calls the function for a win
            else:  # Runs if you do not win on the first throw
                print(chance.value)  # Prints to the terminal for debug
                print("You Lost! Roll again.")  # Prints to the terminal for debug
                results.value = f"You rolled {number_rolled}, please roll again."  # Updates results text
                chance_text.value = f"Chance: {number_rolled}"  # Updates chance value on screen
                first_throw.value = "False"  # Sets first throw to false

    def display_rules():  # Called to open rules window
        rules_window.visible = True  # Makes rules window visible

    def close_rules():  # Called to close rules window
        rules_window.visible = False  # Hides rules window

    #   Set App variable and application title
    app = App(title="Hazard")

    #   Default values to be modified during the game
    first_throw = Text(app, "True", visible=False)  # First throw default is true
    dice_one = Text(app, "1", visible=False)  # Dice one default is one
    dice_two = Text(app, "1", visible=False)  # Dice two default is one
    chance = Text(app, "12", visible=False)  # Chance default is 12
    caster = Text(app, "5", visible=False)  # Caster default is 5

    #   ** Phase 1 **
    #   Startup Screen
    layout_box = Box(app, height=500, width=500, border=5)  # Creates layout for the window
    game_window = Box(layout_box, align="top", height="fill", width="fill", visible=False)  # Creates Game Window
    main_select = Box(layout_box, align="top", height="fill", width="fill", visible=False)  # Creates Main Select Window
    result_window = Box(layout_box, align="top", height="fill", width="fill", visible=False)  # Creates Result Window
    intro_window = Box(layout_box, align="top", height="fill", width="fill")  # Creates Introduction Window
    buttons_background = Box(layout_box, align="bottom", height=50, width=500, border=2)  # Creates Button Tray
    buttons_box = Box(buttons_background, align="bottom")  # Creates box for button organization

    Box(intro_window, height=150, width=500, align="top")  # Used for spacing in Intro Window
    #   Welcome/Introduction Text
    Text(intro_window, "Welcome to Hazard! \n\nThis game is based on an early English dice game.\n\n"
                       "The rules can be slightly confusing.\n\nIf you are new or you would like a "
                       "refresher,\nplease click the rules button.\n\n"
                       "Enjoy the game!", size=16, width="fill")

    #   ** Phase 2 **
    #   Select main buttons
    #   Shown via select main function and hidden once the game starts
    Text(main_select, "Please select your number.", size=20, height=3, width="fill")  # Helper text
    PushButton(main_select, command=start_game, args=[5], text="5", height="fill", width="fill")  # Five button
    PushButton(main_select, command=start_game, args=[6], text="6", height="fill", width="fill")  # Six button
    PushButton(main_select, command=start_game, args=[7], text="7", height="fill", width="fill")  # Seven button
    PushButton(main_select, command=start_game, args=[8], text="8", height="fill", width="fill")  # Eight button
    PushButton(main_select, command=start_game, args=[9], text="9", height="fill", width="fill")  # Nine button

    #   ** Phase 3 **
    #   Used to actually play the game
    result_spacing = Box(game_window, width=10, height=25, align="top", visible=False)  # Used for spacing
    #   Helper text to instruct the player what to do next
    results = Text(game_window, "Please roll the dice!", size=20, align="top", visible=False, width="fill")
    Box(game_window, width="fill", height=25, align="top")  # Used for spacing
    main_text = Text(game_window, text=" ", size=16, align="top")  # Text to remind player what they picked
    chance_text = Text(game_window, text=" ", size=16, align="top")  # Text to remind player of their first roll
    Box(game_window, align="left", width=100, height=10)  # Used for spacing
    dice_one_image = Picture(game_window, image="images/dice1.png", align="left")  # Visual picture of dice
    Box(game_window, align="right", width=100, height=10)  # Used for spacing
    dice_two_image = Picture(game_window, image="images/dice2.png", align="right")  # Visual picture of dice
    #   Used to call the roll dice function
    roll_button = PushButton(game_window, command=roll_dice, text="Roll Dice", align="bottom", visible=False)
    #   Called to see if the player would like to continue playing
    play_again = Text(result_window, "Would you like to play again?", size=20, width="fill", height="fill")

    #   Control buttons on bottom
    start_game_button = PushButton(buttons_box, command=select_main, text="Start New Game", align="left")
    PushButton(buttons_box, command=display_rules, text="Rules", align="left")  # Button used to display rules
    PushButton(buttons_box, command=exit, text="Exit Game", align="left")  # Button used to exit game

    #   Window for displaying the rules of the game
    #   This window can be opened at any time
    rules_window = Window(app, title="Rules", visible=False)
    rules_layout = Box(rules_window, height=500, width=500, border=5)  # Creates layout for rules screen
    rules_textbox = Box(rules_layout, height="fill", width="fill", align="top")  # Box to house rules text
    Box(rules_textbox, height=75, width="fill", align="top")  # Used for spacing
    #   Describes the rules to the player
    Text(rules_textbox, text="Welcome to Hazard!\n\nFirst, you will pick a number between 5 and 9. This is called the "
                             "main.\n\nIf you roll the main on your first throw, you win!\nIf you picked 6 or 8 and "
                             "roll a 12 on your first throw, you still win.\nIf you picked a 7 and roll an 11 on your "
                             "first throw, you also win.\n\nIf you do not win on your first throw,\nthe number you "
                             "rolled becomes the chance.\nYou then have to roll again.\n\nOn any roll after your first "
                             "throw, if you roll the chance, you win.\nHowever, if you roll the main, "
                             "you lose.\n\nYou must then continue rolling until you either win or lose.", size=16)
    close_box = Box(rules_layout, align="bottom", height=50, width=500, border=2)  # Box for housing the close button
    PushButton(close_box, command=close_rules, text="Close", align="bottom")  # Closes the rules window

    #   Called to display the application
    app.display()


if __name__ == '__main__':  # Tell the Python interpreter to execute this main()
    main()
