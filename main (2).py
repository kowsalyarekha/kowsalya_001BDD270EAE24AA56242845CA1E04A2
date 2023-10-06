# Define the Batsman class
class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is batting")

# Define the Bowler class
class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is bowling")

# Create objects of both classes
batsman = Batsman("John")
bowler = Bowler("Alice")

# Call the play method for each object
batsman.play()  # Output: John is batting
bowler.play()   # Output: Alice is bowling
