import random

print("Гра почалась")

# first_list = ["вода", "чай", "печиво", "футбол", "ультрас"]
first_list = ["чай"]
question = random.choice(first_list)  # метод обирає рандомне слово

word = question  # змінна яка зберігає слово

attempt = int(input("Скільки ви хочете отримати спроб для розвязання:>"))

stars = []
count = 1

for i in range(len(word)):
    stars.append("*")  # приймає answer і робить з нього ******* в змінній stars
print(''.join(stars))


while ''.join(stars) != question:

    answer = str(input("Введіть букву або слово:> ")).lower()

    if answer == word:
        print("Ви вгадали слово.")
        break

    elif len(answer) == 1:
        if answer not in word:
            print("Такої літери немає(")
            if count == attempt:
                print("G-A-M-E O-V-E-R")
                print(f"Слово {word}")
                break
            print(''.join(stars))

            count += 1

        for i in range(len(word)):
            if answer == word[i]:
                stars[i] = answer
                if count == attempt and ''.join(stars) != word:
                    print("G-A-M-E O-V-E-R")
                    print(f"Слово {word}")
                    break
                print(''.join(stars))

    elif answer != word:
        print("Не вірно.")
        print(''.join(stars))
        count += 1
