"""
The Mysterious Island
A text-based adventure game created with GitHub Copilot
"""

import time
import sys

def print_slow(text, delay=0.03):
    """Print text with a typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_separator():
    """Print a decorative separator"""
    print("\n" + "=" * 60 + "\n")

def get_choice(options):
    """Get valid user input from available options"""
    while True:
        choice = input("\nYour choice: ").strip().lower()
        if choice in options:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(options)}")

def intro():
    """Introduction to the game"""
    print_separator()
    print_slow("🏝️  THE MYSTERIOUS ISLAND  🏝️", 0.05)
    print_separator()
    time.sleep(0.5)
    print_slow("You wake up on a strange beach, waves crashing nearby...")
    time.sleep(0.5)
    print_slow("The last thing you remember is your ship caught in a storm.")
    time.sleep(0.5)
    print_slow("You must find a way to escape this mysterious island!")
    print_separator()
    time.sleep(1)

def beach_scene():
    """Starting scene at the beach"""
    print_slow("\n🏖️  You stand on a sandy beach.")
    print_slow("To your left, you see a dense JUNGLE with strange sounds.")
    print_slow("To your right, there are CAVES carved into the cliff face.")
    print_slow("Straight ahead, you notice WRECKAGE from your ship.")
    
    print("\nWhere do you want to go?")
    print("  [jungle] - Explore the jungle")
    print("  [caves] - Investigate the caves")
    print("  [wreckage] - Check the ship wreckage")
    
    choice = get_choice(['jungle', 'caves', 'wreckage'])
    
    if choice == 'jungle':
        jungle_scene()
    elif choice == 'caves':
        caves_scene()
    elif choice == 'wreckage':
        wreckage_scene()

def jungle_scene():
    """Jungle exploration path"""
    print_separator()
    print_slow("🌴 You venture into the thick jungle...")
    time.sleep(0.5)
    print_slow("Vines hang from towering trees, and colorful birds call out.")
    print_slow("You discover a STREAM with fresh water and a TEMPLE covered in vines.")
    
    print("\nWhat do you do?")
    print("  [stream] - Follow the stream")
    print("  [temple] - Explore the ancient temple")
    print("  [back] - Return to the beach")
    
    choice = get_choice(['stream', 'temple', 'back'])
    
    if choice == 'stream':
        stream_scene()
    elif choice == 'temple':
        temple_scene()
    elif choice == 'back':
        beach_scene()

def stream_scene():
    """Following the stream"""
    print_separator()
    print_slow("💧 You follow the babbling stream through the jungle...")
    time.sleep(0.5)
    print_slow("It leads you to a beautiful waterfall and a hidden cove.")
    print_slow("Behind the waterfall, you spot a BOAT that looks seaworthy!")
    time.sleep(0.5)
    print_slow("\n🎉 You repair the boat with materials from the jungle.")
    print_slow("As the sun sets, you sail away from the mysterious island...")
    print_separator()
    print_slow("✨ CONGRATULATIONS! You've escaped the island! ✨", 0.05)
    print_separator()
    return True

def temple_scene():
    """Ancient temple exploration"""
    print_separator()
    print_slow("🏛️  You approach the mysterious temple...")
    time.sleep(0.5)
    print_slow("Stone steps lead up to a grand entrance.")
    print_slow("Inside, you find ancient murals and a pedestal with a GOLDEN IDOL.")
    
    print("\nWhat do you do?")
    print("  [take] - Take the golden idol")
    print("  [leave] - Leave the idol and explore further")
    print("  [back] - Return to the jungle entrance")
    
    choice = get_choice(['take', 'leave', 'back'])
    
    if choice == 'take':
        print_separator()
        print_slow("⚠️  As you grab the idol, the ground begins to shake!")
        time.sleep(0.5)
        print_slow("The temple starts to collapse! Rocks fall from the ceiling!")
        time.sleep(0.5)
        print_slow("💀 You didn't make it out in time...")
        print_separator()
        print_slow("GAME OVER - The temple claimed another victim.", 0.05)
        print_separator()
        return False
    elif choice == 'leave':
        print_separator()
        print_slow("You wisely leave the idol and continue exploring...")
        print_slow("You find a back exit that leads to a hidden beach!")
        print_slow("There, a ship passes by and rescues you!")
        print_separator()
        print_slow("✨ CONGRATULATIONS! You've been rescued! ✨", 0.05)
        print_separator()
        return True
    elif choice == 'back':
        jungle_scene()

def caves_scene():
    """Cave exploration path"""
    print_separator()
    print_slow("🕳️  You enter the dark caves...")
    time.sleep(0.5)
    print_slow("The air is cool and damp. Water drips from the ceiling.")
    print_slow("You see TWO PATHS: one leads deeper, the other shows a faint light.")
    
    print("\nWhich path do you take?")
    print("  [deep] - Go deeper into the cave")
    print("  [light] - Follow the light")
    print("  [back] - Return to the beach")
    
    choice = get_choice(['deep', 'light', 'back'])
    
    if choice == 'deep':
        deep_cave_scene()
    elif choice == 'light':
        light_cave_scene()
    elif choice == 'back':
        beach_scene()

def deep_cave_scene():
    """Deep cave encounter"""
    print_separator()
    print_slow("You venture deeper into the darkness...")
    time.sleep(0.5)
    print_slow("Suddenly, you hear a LOW GROWL echoing through the cavern.")
    print_slow("Two glowing eyes appear in the darkness!")
    time.sleep(0.5)
    print_slow("💀 A giant cave bear charges at you!")
    time.sleep(0.5)
    print_slow("With no weapon and nowhere to run...")
    print_separator()
    print_slow("GAME OVER - The cave was not empty.", 0.05)
    print_separator()
    return False

def light_cave_scene():
    """Following the light in the cave"""
    print_separator()
    print_slow("✨ You carefully follow the light source...")
    time.sleep(0.5)
    print_slow("The passage opens up to reveal an underground lagoon!")
    print_slow("Bioluminescent algae lights up the water in brilliant blues and greens.")
    print_slow("You spot a SUBMARINE partially submerged at the dock!")
    time.sleep(0.5)
    print_slow("\nYou manage to start the old submarine and navigate out to sea.")
    print_separator()
    print_slow("✨ CONGRATULATIONS! You've escaped via submarine! ✨", 0.05)
    print_separator()
    return True

def wreckage_scene():
    """Ship wreckage investigation"""
    print_separator()
    print_slow("🚢 You approach the wreckage of your ship...")
    time.sleep(0.5)
    print_slow("Debris is scattered across the beach.")
    print_slow("You find a RADIO, some SUPPLIES, and a FLARE GUN.")
    
    print("\nWhat do you do?")
    print("  [radio] - Try to repair the radio")
    print("  [flare] - Fire the flare gun")
    print("  [supplies] - Gather supplies and explore")
    
    choice = get_choice(['radio', 'flare', 'supplies'])
    
    if choice == 'radio':
        print_separator()
        print_slow("📻 You spend hours trying to repair the radio...")
        time.sleep(0.5)
        print_slow("Finally, you get it working!")
        print_slow("You send out an SOS signal.")
        time.sleep(0.5)
        print_slow("Within a day, a rescue helicopter arrives!")
        print_separator()
        print_slow("✨ CONGRATULATIONS! You've been rescued! ✨", 0.05)
        print_separator()
        return True
    elif choice == 'flare':
        print_separator()
        print_slow("🔥 You fire the flare high into the sky...")
        time.sleep(0.5)
        print_slow("It burns bright red against the blue sky.")
        time.sleep(0.5)
        print_slow("But no one sees it. You only had one flare...")
        print_slow("You'll need to find another way off the island.")
        time.sleep(1)
        beach_scene()
    elif choice == 'supplies':
        print_separator()
        print_slow("🎒 You gather supplies: water, food, a knife, and rope.")
        print_slow("Feeling more prepared, you decide to explore further.")
        time.sleep(1)
        beach_scene()

def play_again():
    """Ask if player wants to play again"""
    print("\nWould you like to play again?")
    print("  [yes] - Start a new adventure")
    print("  [no] - Exit game")
    
    choice = get_choice(['yes', 'no'])
    return choice == 'yes'

def main():
    """Main game loop"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + "  🎮 Welcome to Choose Your Own Adventure! 🎮  ".center(58) + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    
    while True:
        intro()
        beach_scene()
        
        if not play_again():
            print_separator()
            print_slow("Thanks for playing! Safe travels, adventurer! 🌟", 0.05)
            print_separator()
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
