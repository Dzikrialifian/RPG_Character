# RPG_Character

# RPGcharacter

This implementation uses basic Python logic to create and validate an RPG character with a name and three character stats: *Strength*, *Intelligence*, and *Charisma*.

Some basic Python concepts applied in this project include:

- *Function & Parameters*: Using a function to create a character with a name and specific stats.
- *Input Validation*: Checking whether the input values follow the required rules before creating the character.
- *Type Checking*: Using `isinstance()` and `type()` to ensure the input values have the correct data types.
- *String Operations*: Using `len()` and string membership checks to validate the character name.
- *Set*: Grouping the character stats together to simplify the validation process.
- *For Loop*: Iterating through the character stats during validation.
- *`any()` & Generator Expression*: Checking whether any of the given stats fail to meet the required conditions.
- *`sum()`*: Checking whether the total points allocated to all stats are equal to 7.
- *F-string*: Formatting the character information into the required output format.

This project creates an RPG character based on a given name and three stats. The program validates the character's name and stats before generating the final character sheet.

The program follows these steps:

- **Validate the character name**:
  - The name must be a string.
  - The name cannot be empty.
  - The name must not be longer than 10 characters.
  - The name must not contain spaces.

- **Validate the character stats**:
  - All stats must be integers.
  - Each stat must be between 1 and 4.
  - The total value of all three stats must be exactly 7.

- **Generate the character sheet** using the given name and stats.
- **Format the character output** using dots to represent the remaining stat values.
- **Return the completed character information.**
