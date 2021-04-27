from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
currCard = {}
makeDict = {}
try:
    data = pd.read_csv('data/words_new.csv')

except FileNotFoundError:
    Fdata = pd.read_csv('data/french_words.csv')
    makeDict = Fdata.to_dict(orient='records')

else:
    makeDict = data.to_dict(orient='records')

def nextCard():
    global currCard, timer
    window.after_cancel(timer)
    currCard = random.choice(makeDict)
    canvas.itemconfig(cardTitle, text='French', fill='Black')
    canvas.itemconfig(cardMean, text=currCard['French'])
    canvas.itemconfig(cardBackground, image=cardFrontImg)
    timer = window.after(4000, func=cardFlip)


def cardFlip():
    canvas.itemconfig(cardTitle, text='English', fill='White')
    canvas.itemconfig(cardMean, text=currCard['English'], fill='White')
    canvas.itemconfig(cardBackground, image=cardBackImg)

def alrKnow():
    makeDict.remove(currCard)
    data = pd.DataFrame(makeDict)
    data.to_csv('data/words_new.csv', index=False)
    nextCard()

window = Tk()
window.title('Flash App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(4000, func=cardFlip)

canvas = Canvas(width=800, height=500)
cardFrontImg = PhotoImage(file='images/card_front.png')
cardBackImg = PhotoImage(file='images/card_back.png')
cardBackground = canvas.create_image(400, 260, image=cardFrontImg)

cardTitle = canvas.create_text(400, 150, text='title', font=('Arial', 40, 'bold'))
cardMean = canvas.create_text(400, 263, text='word', font=('Arial', 28, 'italic'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

crossImg = PhotoImage(file='images/wrong.png')
unknownBtn = Button(image=crossImg, highlightthickness=0, command=nextCard)
unknownBtn.grid(row=1, column=0)

tickImg = PhotoImage(file='images/right.png')
knownBtn = Button(image=tickImg, highlightthickness=0, command=alrKnow)
knownBtn.grid(row=1, column=1)

nextCard()

window.mainloop()