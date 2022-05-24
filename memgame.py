from os import times
from tkinter import *
from tkinter import ttk, messagebox
import random, time
import json

t = 3
score = 0


wordList = ['rookie', 'crab', 'time', 'bike', 'ice', 'tan', 'tall',
            'mouse', 'movie', 'bottle', 'golf', 'sun', 'run',
            'cat', 'neat', 'glove', 'toy', 'banana', 'soda', 'dessert', 'hat', 'dog',
            'cow', 'apple', 'top', 'sock', 'night', 'pet', 'fist', 'power', 'paper', 'sand',
            'key', 'chair', 'pear', 'shirt', 'pants', 'far', 'sight', 'fan', 'clap', 'send',
            'laptop', 'sugar', 'net', 'tie', 'wig', 'bit', 'bird', 'spin', 'hot', 'finger', 'coin',
            'computer', 'spot', 'graphics', 'tablet']

dupArray = []

class MainWindow():

    def __init__(self, mainWidget):
        #  center it with padding 200
        self.main_frame = ttk.Frame(mainWidget, width=1, height=1, padding=(150, 0, 0, 150))
        self.main_frame.grid(row=1, column=1, )

        self.control = 0

        self.main_user_interface()

    def main_user_interface(self):
        # title of the game
        root.title('Memory Game')

        self.main_label_1 = ttk.Label(self.main_frame, text='Welcome to the Memory game')
        self.main_label_1.grid(row=1, column=1, )

        self.main_label_2 = ttk.Button(self.main_frame, text='Play Game')
        self.main_label_2.grid(row=2, column=1)
        self.main_label_2.bind('<Button-1>', self.prepare_gui)

        self.main_label_3 = ttk.Button(self.main_frame, text='Scoreboard')
        self.main_label_3.grid(row=3, column=1)
        self.main_label_3.bind('<Button-1>', self.score_board)

        self.option_button = ttk.Button(self.main_frame, text='Options')
        self.option_button.grid(row=4, column=1)
        # center the button

        self.option_button.bind('<Button-1>', self.settings_ui)

        self.ui_widgets = [self.main_label_1,
                           self.main_label_2,
                           self.main_label_3,
                           self.option_button
                           ]

    def easy_difficulty(self):
        global t
        t = 10

    def medium_difficulty(self):
        global t
        t = 5

    def hard_difficulty(self):
        global t
        t = 3

    # def medium(self):
    #
    #
    # def hard(self):




    def settings_ui(self, event):
        self.remove_widgets(self.ui_widgets)

        root.title('Options')

        self.main_label_1 = ttk.Label(self.main_frame, text='Select difficulty level')
        self.main_label_1.grid(row=1, column=0)

        self.main_menu_button = ttk.Button(self.main_frame, text='Main menu')
        self.main_menu_button.grid(row=0, column=1)
        self.main_menu_button.bind('<Button-1>', self.title_screen)



        var = IntVar()
        R1 = Radiobutton(self.main_frame, text="Easy", variable=var, value=1,
                         command=self.easy_difficulty)
        R1.grid(row=2, column=0)

        R2 = Radiobutton(self.main_frame, text="Medium", variable=var, value=2,
                         command=self.medium_difficulty)
        R2.grid(row=3, column=0)

        R3 = Radiobutton(self.main_frame, text="Hard", variable=var, value=3,
                         command=self.hard_difficulty)

        R3.grid(row=4, column=0)




        self.control = 1

        self.ui_widgets = [self.main_label_1,
                           self.main_menu_button,
                            R1, R2, R3]

    def title_screen(self, event):
        if self.control == 1:
            self.remove_widgets(self.ui_widgets)
        else:
            pass
        self.main_user_interface()

    def remove_widgets(self, widgets):
        for widgets in widgets:
            widgets.destroy()

    def prepare_gui(self, event):
        self.remove_widgets(self.ui_widgets)

        root.title('Preparation')

        self.main_label_4 = ttk.Label(self.main_frame, text='The game will begin when you click start')
        self.main_label_4.grid(row=0, column=1)

        self.start_button = ttk.Button(self.main_frame, text='Start')
        self.start_button.grid(row=1, column=1)
        self.start_button.bind('<Button-1>', self.play_gui)

        self.control = 1

        self.ui_widgets = [self.main_label_4,
                           self.start_button]

    def game_end(self):
        self.remove_widgets(self.ui_widgets)

        root.title('Enter your username')
        self.main_label_7 = Entry(root, textvariable=times)
        self.main_label_7.grid(row=1, column=1)

        self.main_label_5 = ttk.Label(self.main_frame, text='Enter your  username to enter your scores')
        self.main_label_5.grid(row=0, column=1)

        self.main_label_6 = ttk.Button(text="Submit username", command=self.record_score)
        self.main_label_6.grid(row=2, column=1, )

        self.control = 1

        self.main_menu_button = ttk.Button(self.main_frame, text='Main menu')
        self.main_menu_button.grid(row=10, column=3)
        self.main_menu_button.bind('<Button-1>', self.title_screen)


        self.ui_widgets = [self.main_label_5, self.main_label_6, self.main_label_7, self.main_menu_button]


    def record_score(self):

        user_name = self.main_label_7.get()
        with open('scores.txt', 'w') as outfile:
            outfile.write("run" + " "+ user_name + " " + str(score))

        messagebox.showinfo("Submitted", " Your score has been recorded")




    def score_board(self, event):
        self.remove_widgets(self.ui_widgets)








        root.title('scoreboard')

        # self.main_label_4 = ttk.Label(self.main_frame, text='Top 5')
        # self.main_label_4.grid(row=0, column=1)
        #
        # self.main_label_5 = ttk.Label(self.main_frame, text='Name')
        # self.main_label_5.grid(row=1, column=0)
        #
        # self.main_label_6 = ttk.Label(self.main_frame, text='Score')
        # self.main_label_6.grid(row=1, column=4)

        self.main_menu_button = ttk.Button(self.main_frame, text='Main menu')
        self.main_menu_button.grid(row=0, column=5)
        self.main_menu_button.bind('<Button-1>', self.title_screen)





        self.control = 1

        # Opening JSON file
        # f = open('scores.json')

        # returns JSON object as
        # a dictionary
        # data = json.load(f)

        # Iterating through the json
        # list
        # print username
        # print(data[0]["user"])
        # print(data[0]["score"])

        # Closing file
        # f.close()
        z = 0
        with open('scores.json') as a:
            dict1 = json.load(a)
        for item in dict1:
            self.main_label_7 = ttk.Label(self.main_frame, text=item)
            z = z + 1
            print(self.main_label_7.grid(row=1 + z, column=0))


        # self.main_label_7 = ttk.Label(self.main_frame, text=item)
        # self.main_label_7.grid(row=2, column=0)
        #
        # self.main_label_8 = ttk.Label(self.main_frame, text=data[0]["score"])
        # self.main_label_8.grid(row=2, column=4)
        #
        # self.main_label_10 = ttk.Label(self.main_frame, text=data[1]["user"])
        # self.main_label_10.grid(row=3, column=0)
        # self.main_label_9 = ttk.Label(self.main_frame, text=data[1]["score"])
        # self.main_label_9.grid(row=3, column=4)
        #
        # self.main_label_16 = ttk.Label(self.main_frame, text=data[2]["user"])
        # self.main_label_16.grid(row=4, column=0)
        # self.main_label_11 = ttk.Label(self.main_frame, text=data[2]["score"])
        # self.main_label_11.grid(row=4, column=4)
        #
        # self.main_label_12 = ttk.Label(self.main_frame, text=data[3]["user"])
        # self.main_label_12.grid(row=5, column=0)
        # self.main_label_13 = ttk.Label(self.main_frame, text=data[3]["score"])
        # self.main_label_13.grid(row=5, column=4)
        #
        #
        # self.main_label_14 = ttk.Label(self.main_frame, text=data[4]["user"])
        # self.main_label_14.grid(row=5, column=0)
        # self.main_label_15 = ttk.Label(self.main_frame, text=data[4]["score"])
        # self.main_label_15.grid(row=5, column=4)


        self.ui_widgets = [self.main_label_7, self.main_menu_button]

        # self.ui_widgets = [self.main_label_4, self.main_label_5,
        #                    self.main_label_6, self.main_label_7,
        #                    self.main_label_8, self.main_label_9,
        #                    self.main_label_10, self.main_label_11,self.main_label_12, self.main_label_13,
        #                    self.main_label_14, self.main_label_15, self.main_label_16, self.main_menu_button]

    def duplicate(input):
        for duppWord in dupArray:
            if duppWord == input:
                print("Duplicate word, try again")

    def play_gui(self, event):
        # remove prepare_gui elements
        self.remove_widgets(self.ui_widgets)

        def countdown():
            global t
            if t > 0:
                l1.config(text=t)
                t = t - 1
                l1.after(1000, countdown)
            elif t == 0:
                print("Game end")
                self.main_label_4 = Label(text="Please enter the words you memorized")
                self.main_label_4.grid(row=0, column=1)
                # hide the list of words when countdown reaches 0
                self.words_label1.grid_remove()
                self.words_label2.grid_remove()
                self.main_label_5 = Entry(root, textvariable=times)
                self.main_label_5.grid(row=1, column=1)

                self.main_label_1 = ttk.Button(text="enter word", command=score)
                self.main_label_1.grid(row=2, column=1, )

                # self.main_label_2 = ttk.Button(text="Quit", command=root.destroy)
                # self.main_label_2.grid(row=10, column=1, )

                self.main_label_3 = ttk.Button(text="End Game", command=self.game_end)
                self.main_label_3.grid(row=11, column=1, )

                self.ui_widgets = [self.main_label_1, self.main_label_3, self.main_label_4,
                                   self.main_label_5]
                # get rid of count down label after clicking main menu
                l1.config(text="")
        def score():
            global score
            global strike
            # print("Now its time to check your answers, start with the first word then hit enter")
            entry1 = Entry(root, textvariable=times)
            get_input = entry1.get()

            # Checks for duplicate words
            for duppWord in dupArray:
                if duppWord == get_input:
                    print("Duplicate word, try again")
                    messagebox.showinfo("Duplicate word", " Duplicate word, try again!")
                    print("Your score is " + str(score) + " out of 10")
                    break

            else:

                for i in range(0, 10):

                    # get_input = entry1.get()
                    if get_input == wordList[i]:
                        dupArray.append(get_input)
                        print("Correct!!!")
                        score = score + 1
                        break
                else:

                    print("please try again")

                    messagebox.showinfo("Wrong word", "Try again!      ")







                    # else:
            #
            #     print("Please try again")
            #
            # print("Your score is " + str(score) + " out of 10")

        # wordList = ['rookie', 'crab', 'time', 'bike', 'ice', 'tan', 'tall',
        #             'mouse', 'movie', 'bottle', 'golf', 'sun', 'run',
        #             'cat', 'neat', 'glove', 'toy', 'banana', 'soda', 'dessert', 'hat', 'dog',
        #             'cow', 'apple', 'top', 'sock', 'night', 'pet', 'fist', 'power', 'paper', 'sand',
        #             'key', 'chair', 'pear', 'shirt', 'pants', 'far', 'sight', 'fan', 'clap', 'send',
        #             'laptop', 'sugar', 'net', 'tie', 'wig', 'bit', 'bird', 'spin', 'hot', 'finger', 'coin',
        #             'computer', 'spot', 'graphics', 'tablet']

        random.shuffle(wordList)

        self.words_label1 = ttk.Label(
            text=wordList[0] + '\n' + wordList[1] + '\n' + wordList[2] + '\n' + wordList[3] + '\n' + wordList[
                4])
        # grid for the first list
        self.words_label1.grid(column=0, row=1)
        self.words_label2 = ttk.Label(
            text=wordList[5] + '\n' + wordList[6] + '\n' + wordList[7] + '\n' + wordList[8] + '\n' + wordList[
                9])
        # grid for the second list
        self.words_label2.grid(column=2, row=1)

        #  count down label
        l1 = Label(root, font="times 15")
        l1.grid(row=1, column=1)
        times = StringVar()

        # start countdown automatically
        countdown()


def main():
    global root
    root = Tk()

    root.geometry("500x500")
    window = MainWindow(root)

    root.mainloop()


if __name__ == '__main__':
    main()
