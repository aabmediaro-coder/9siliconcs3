**Name:** Ally
**Section:** Silicon
**Last Name:** Mediario
**Date:** August 20, 2026

## Requirements

1. Ask the user to enter a year of birth.
2. The baseline year is 1900.
3. Validate that the year should not be earlier than 1900.
4. Display an invalid year message if the year is earlier than 1900.
5. Determine the Chinese Zodiac sign that recurs after each 12 years. 
6. Consider only the year of birth.

## Chinese Zodiac Signs

1. Rat (鼠 / Shǔ)
2. Ox (牛 / Niú)
3. Tiger (虎 / Hǔ)
4. Rabbit (兔 / Tù)
5. Dragon (龙 / Lóng)
6. Snake (蛇 / Shé)
7. Horse (马 / Mǎ)
8. Goat (羊 / Yáng)
9. Monkey (猴 / Hóu)
10. Rooster (鸡 / Jī)
11. Dog (狗 / Gǒu)
12. Pig (猪 / Zhū)

## Actual Code

# Ask the user to enter their birth year 
birth_year = int(input("Enter your birth year: "))

# Validate that the year is not earlier than 1900
if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    # Chinese zodiac signs starting from 1900
    zodiac_signs = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

    zodiac_index = (birth_year - 1900) % 12
    zodiac_sign = zodiac_signs[zodiac_index]

    print("Your Chinese Zodiac Sign is:", zodiac_sign)

## Screenshot
[Chinese Zodiac Signs Output](images/Screenshot%202026-08-20%20205039.png)