##Name: Ally
##Section: Silicon
##Last Name: Mediario
##Date: August 20, 2026

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
