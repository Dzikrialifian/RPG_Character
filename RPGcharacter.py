full_dot = '●'
empty_dot = '○'

# define a function to create a character with name and stats
def create_character(name, strength, intelligence, charisma):

    # validate the input parameters
    if not isinstance(name, str):
        return "The character name should be a string."

    # check if the name is empty
    if not name:
        return "The character should have a name."

    if len(name) > 10:
        return "The character name is too long."

    # check if the name contains spaces
    if " " in name:
        return "The character name should not contain spaces."

    # validate the stats with for loop
    stats = {strength, intelligence, charisma}

    # check if all stats are integers and within the valid range
    if any(type(stat) is not int for stat in stats):
        return "All stats should be integers"

    # check if all stats are within the valid range
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"

    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"

    # check if the total points allocated to stats is equal to 7
    if sum(stats) != 7:
        return "The character should start with 7 points"

    # return the character's name and stats in the specified format
    return (f"{name},\nSTR {full_dot*strength}{empty_dot*(10-strength)},\nINT {full_dot*intelligence}{empty_dot*(10-intelligence)},\nCHA {full_dot*charisma}{empty_dot*(10-charisma)}")

# test the function with a sample character
result = create_character('Bigbo', 4, 1, 2)
print(result)