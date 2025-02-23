import pyautogui # This imports is what allows the script to click on our computer 
import time

def initial_sleep(n_seconds_to_wait: int = 5):
    """
    Description:

        This method is used so that the user has time to switch from their code editor/IDE
        to their game and position the mouse if need be.

    Args:

        n_seconds_to_wait (int, optional): The number of seconds the script waits before starting. Defaults to 5.

    """
    for x in range(n_seconds_to_wait, 0, -1):
        print("The script will start in " + str(x) + "!")
        time.sleep(1)
    print("It will now start!")

# O "tempo_entre_crafts" deve ser o tempo que a craft demorou 
# arredondado ao inteiro superior mais proximo mais 3.
# Ex 1 : se uma craft demorou 31,73 seg , então tempo_entre_crafts = 32,00 (31,73 arredondado ao inteiro superior mais proximo) + 3 = 35  
# Ex 2 : se uma craft demorou 10,30 seg , então tempo_entre_crafts = 11,00 (10,30 arredondado ao inteiro superior mais proximo) + 3 = 14  
def craft_recipe(n_crafts: int, time_each_craft_takes: int):
    """ 
        The main function of the script. It clicks your mouse the same place twice per craft
        (the first is to select the craft and the second one is to execute the macro/action).
        The double click is necessary because of how the game registers the clicks. If you only
        click once, the game assumes you clicked and held the mouse.

    Args:
        n_crafts (int): number of times the same recipe is crafted
        time_each_craft_takes (int): the time each recipe takes to craft. I suggest you round up the number and add 3 seconds to the total time.
            Example 1 : if a craft takes 12.3 seconds to execute, then the value should be 16 ( 12.3 rounded up plus 3 ).
            Example 2 : if a craft takes 36.9 seconds to execute, then the value should be 40 ( 36.9 rounded up plus 3 ).
    """
    for x in range(n_crafts):
        print("Begining craft.")
        pyautogui.click(clicks=2, interval=2)
        time.sleep(3)
        print("Craft number " + str(x+1) + " out of " + str(n_crafts) + " is now starting.")
        pyautogui.click(clicks=2, interval=2)
        time.sleep(time_each_craft_takes)
        print("Craft completed!")
        time.sleep(2)
    print("All crafts are now completed!")
        
initial_sleep()
craft_recipe(n_crafts=36, time_each_craft_takes=43)