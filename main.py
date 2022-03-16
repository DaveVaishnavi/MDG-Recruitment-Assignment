import requests
from tkinter import *
from PIL import Image, ImageTk


def is_vowel(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return True


def next_image():
    img_url1 = "https://foodish-api.herokuapp.com/api/"
    data1 = requests.get(url=img_url1, stream=True).json()
    dish1 = requests.get(url=data1["image"])
    with open("image.png", "wb") as file1:
        file1.write(dish1.content)

    def check():
        end_of_game = False
        lives = 5
        while not end_of_game:
            if guessed_letter in attempt:
                text.config(text=f"REMARKS : You already entered letter {guessed_letter}")
                guess.delete(0, len(guessed_letter)-1)
            for position in range(len(answer)):
                letter = answer[position]
                if letter == guessed_letter:
                    attempt[position] = letter
            if guessed_letter not in answer:
                text.config(text=f"REMARKS : The letter {guessed_letter} is not present in the food-dish name !")
                lives -= 1
                guess.delete(0, len(guessed_letter) - 1)
            if lives == 0:
                end_of_game = True
                text.config(text="REMARKS : Oh ! You could not guess it correctly !")
                guess.delete(0, len(guessed_letter) - 1)
            if '_' not in attempt:
                text.config(text="REMARKS : Yes , you are correct ! That is the correct answer !")

    img = ImageTk.PhotoImage(Image.open("image.png"))
    canvas8 = Canvas(width=1200, height=700)
    canvas8.create_image(600, 350, image=img)
    canvas8.place(x=100, y=50)
    answer = data["image"].split("/")[-2]
    attempt = []
    text = Label(text="REMARKS : Guess a letter", font=("Ariel", 20, "bold"))
    text.place(x=500, y=10)

    def passed():
        answer_display.config(text=answer)
    for char in answer:
        if is_vowel(char):
            attempt.append(char)
        else:
            attempt.append("_")
    check_button = Button(text="CHECK", command=check, font=("Ariel", 15, "bold"))
    pass_button = Button(text="I DO NOT KNOW", command=passed, font=("Ariel", 15, "bold"))
    check_button.place(x=1375, y=300)
    pass_button.place(x=1330, y=400)
    answer_display = Label(text=' '.join(attempt), font=("Ariel", 15, "bold"))
    label = Label(text="The name of the dish", font=("Ariel", 15, "bold"))
    label.place(x=1310, y=50)
    answer_display.place(x=1350, y=100)
    label2 = Label(text="Your guess :", font=("Ariel", 15, "bold"))
    label2.place(x=1350, y=150)
    guess = Entry(width=10, font=("Ariel", 15, "bold"), highlightthickness=2)
    guess.place(x=1350, y=200)
    guessed_letter = guess.get()
    next_image_button = Button(text="NEXT IMAGE", command=next_image, font=("Ariel", 15, "bold"))
    next_image_button.place(x=1350, y=500)


def new_page():

    def check():
        end_of_game = False
        lives = 5
        while not end_of_game:
            if guessed_letter in attempt:
                text.config(text=f"REMARKS : You already entered letter {guessed_letter}")
                guess.delete(0, len(guessed_letter)-1)
            for position in range(len(answer)):
                letter = answer[position]
                if letter == guessed_letter:
                    attempt[position] = letter
            if guessed_letter not in answer:
                text.config(text=f"REMARKS : The letter {guessed_letter} is not present in the food-dish name !")
                lives -= 1
                guess.delete(0, len(guessed_letter) - 1)
            if lives == 0:
                end_of_game = True
                text.config(text="REMARKS : Oh ! You could not guess it correctly !")
                guess.delete(0, len(guessed_letter) - 1)
            if '_' not in attempt:
                text.config(text="REMARKS : Yes , you are correct ! That is the correct answer !")
            answer_display.config(text=' '.join(attempt))
    canvas.destroy()
    canvas1.destroy()
    canvas2.destroy()
    canvas3.destroy()
    canvas4.destroy()
    canvas5.destroy()
    canvas6.destroy()
    canvas7.destroy()
    start_button.destroy()
    img = ImageTk.PhotoImage(Image.open("image.png"))
    canvas8 = Canvas(width=1200, height=700)
    canvas8.create_image(600, 350, image=img)
    canvas8.place(x=100, y=50)
    answer = data["image"].split("/")[-2]
    attempt = []
    text = Label(text="REMARKS : Guess a letter", font=("Ariel", 20, "bold"))
    text.place(x=500, y=10)

    def passed():
        answer_display.config(text=answer)
    for char in answer:
        if is_vowel(char):
            attempt.append(char)
        else:
            attempt.append("_")
    check_button = Button(text="CHECK", command=check, font=("Ariel", 15, "bold"))
    pass_button = Button(text="I DO NOT KNOW", command=passed, font=("Ariel", 15, "bold"))
    check_button.place(x=1375, y=300)
    pass_button.place(x=1330, y=400)
    answer_display = Label(text=' '.join(attempt), font=("Ariel", 15, "bold"))
    label = Label(text="The name of the dish", font=("Ariel", 15, "bold"))
    label.place(x=1310, y=50)
    answer_display.place(x=1350, y=100)
    label2 = Label(text="Your guess :", font=("Ariel", 15, "bold"))
    label2.place(x=1350, y=150)
    guess = Entry(width=10, font=("Ariel", 15, "bold"), highlightthickness=2)
    guess.insert(0, 'd')
    guess.place(x=1350, y=200)
    guessed_letter = guess.get()
    next_image_button = Button(text="NEXT IMAGE", command=next_image, font=("Ariel", 15, "bold"))
    next_image_button.place(x=1350, y=500)


img_url = "https://foodish-api.herokuapp.com/api/"
data = requests.get(url=img_url, stream=True).json()
dish = requests.get(url=data["image"])
with open("image.png", "wb") as file:
    file.write(dish.content)
window = Tk()
window.title("Guess it if you can !")
window.config(bg="white", height=2000, width=2000)
canvas = Canvas(width=600, height=264, bg="white")
foodie = PhotoImage(file="unnamed.png")
canvas.create_image(300, 132, image=foodie)
canvas.place(x=500, y=50)
start_button = Button(text="LET'S PLAY", command=new_page, font=("Ariel", 60, "bold"), width=12)
start_button.place(x=500, y=600)
canvas7 = Canvas(width=300, height=150, bg="white")
image7 = PhotoImage(file="hotdog.png")
canvas7.create_image(150, 75, image=image7)
canvas7.place(x=625, y=400)
canvas1 = Canvas(width=300, height=200, bg="white")
image1 = PhotoImage(file="burger.png")
canvas1.create_image(150, 100, image=image1)
canvas1.place(x=100, y=50)
canvas2 = Canvas(width=300, height=200, bg="white")
image2 = PhotoImage(file="cake.png")
canvas2.create_image(150, 100, image=image2)
canvas2.place(x=100, y=300)
canvas3 = Canvas(width=300, height=200, bg="white")
image3 = PhotoImage(file="donut.png")
canvas3.create_image(150, 100, image=image3)
canvas3.place(x=100, y=550)
canvas4 = Canvas(width=300, height=200, bg="white")
image4 = PhotoImage(file="fries.png")
canvas4.create_image(150, 100, image=image4)
canvas4.place(x=1200, y=50)
canvas5 = Canvas(width=300, height=200, bg="white")
image5 = PhotoImage(file="undhiyu.png")
canvas5.create_image(150, 100, image=image5)
canvas5.place(x=1200, y=300)
canvas6 = Canvas(width=300, height=200, bg="white")
image6 = PhotoImage(file="pizza.png")
canvas6.create_image(150, 100, image=image6)
canvas6.place(x=1200, y=550)
window.mainloop()
