# How to import modules
import os
import random
from pathlib import Path

# Get the current directory of this script file
current_dir = Path(__file__).resolve().parent

# How to join file paths
nouns_file = os.path.join(current_dir, 'nouns.txt')
adjectives_file= os.path.join(current_dir, 'adjectives.txt')

# How to read a file line by line and append to a list
# and how to create a function
def read_file(file_name):
    result = []
    with open(file_name) as file:
        while (line := file.readline().rstrip()):
            result.append(line)
    return result
    
# How to use the function to create global variables
nouns = read_file(nouns_file)
adjectives = read_file(adjectives_file)

# How to use the random module to choose an element of a list
def generate_nickname():
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    nickname = adjective + '-' + noun
    return nickname

if __name__ == '__main__':
    # How to use a for loop to repeat a task
    for i in range(1000):
        print(generate_nickname())
    