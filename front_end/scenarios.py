#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

__author__ = "Mary Catherine Good"

"""
GLOBAL VARIABLES
"""
score = {}

# PARENT CLASS - UI OUTLINE FOR THE SCENARIOS
class ScenarioFrame(tk.Frame):

    def __init__(self, parent, controller, scenario, scenario_title, scenario_text, OPTIONS, next):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E6F1FF")

        v = IntVar()            # DEALS WITH RADIO BUTTONS
        self.total = IntVar()   # DEALS WITH SCORE TOTAL

        # CREATE FRAMES
        title_frame = tk.Frame(self, background="#E6F1FF", width=550, pady=10)
        border_frame1 = tk.Frame(self, background="#5BA3FF", height=2, width=550)
        border_frame2 = tk.Frame(self, background="#006EFF", height=2, width=550)
        border_frame3 = tk.Frame(self, background="white", height=2, width=550)
        border_frame4 = tk.Frame(self, background="#006EFF", height=2, width=550)
        border_frame5 = tk.Frame(self, background="#5BA3FF", height=2, width=550)
        main_frame = tk.Frame(self, background="#E6F1FF", height=400, width=550)
        footer_frame = tk.Frame(self, background="#E6F1FF", height=200, width=550)

        # LAYOUT FRAMES
        title_frame.grid(row=0, column=0, sticky="nsew")
        border_frame1.grid(row=1, column=0, sticky="new")
        border_frame2.grid(row=2, column=0, sticky="new")
        border_frame3.grid(row=3, column=0, sticky="new")
        border_frame4.grid(row=4, column=0, sticky="new")
        border_frame5.grid(row=5, column=0, sticky="new")
        main_frame.grid(row=6, column=0)
        footer_frame.grid(row=7, column=0)

        # SCENARIO WIDGETS
        self.security_awareness_label = tk.Label(title_frame, text="Security Awareness Training", font=("Noteworthy", 30), anchor="center", background="#E6F1FF", pady=15)
        self.scenario1_label = tk.Label(main_frame, text=scenario_title, font=("Arial 20 bold"), wraplength=425, anchor="center", justify="left", background="#E6F1FF", pady=10)
        self.info_label = tk.Label(main_frame, text=scenario_text, wraplength=425, justify="left", background="#E6F1FF")
        self.place_holder_label = tk.Label(main_frame, background="#E6F1FF")
        self.next_button = tk.Button(footer_frame, text="Next", font=(15), command=lambda: controller.show_frame(next), state="disabled", highlightbackground="#5BA3FF", pady=5, width=15)

        # PLACE WIDGETS ON THE FRAME
        self.security_awareness_label.pack(side="top", fill="x")
        self.scenario1_label.pack()
        self.info_label.pack()
        for text, option in OPTIONS:
            self.b = tk.Radiobutton(main_frame, text=text, variable=v, value=option, command=lambda: self.getScore(scenario, v), wraplength=425, anchor="w", justify="left", background="#E6F1FF", pady=5, width=50)
            self.b.pack()
        self.place_holder_label.pack()
        self.next_button.pack(side="bottom")

    def getScore(self, scenario, v):
        score[scenario] = v.get()
        self.next_button["state"]="normal"

        print("TEST -- PRINT ALL")
        for x, y in score.items():
            print(x, y)


# SCENARIO 1 - PASSWORD CREATION
class Scenario1(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        scenario1_title = "Scenario 1: Password Creation"
        scenario1_text = "Alice just started a new job working at SONY Corporation. As part of her new job, she has to create a new password to sign in to access different applications. \nWhat rules should Alice follow when creating her new passwords?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Include: 12+ characters, upper and lower case letters, numbers, special characters. Not Include: personal information such as birthdays and names of pets and family. These rules will ensure that your new password is strong and tough for hackers to crack." , 2),
        ("Include: 12+ characters, upper and lower case letters, numbers, special characters. Not Include: personal information such as birthdays and names of pets and family, words that can be found in the dictionary. These rules will ensure that your new password is strong and tough for hackers to crack." , 3),
        ("Include: 12+ characters, upper and lower case letters, numbers, special characters. Not Include: words that can be found in the dictionary. These rules will ensure that your new password is strong and tough for hackers to crack.  But will also enable you to remember your password so you can sign in." , 1)]
        # NEXT PAGE
        next = "Scenario2"

        ScenarioFrame.__init__(self, parent,controller, 1, scenario1_title, scenario1_text, OPTIONS, next)


# SCENARIO 2 - PASSWORD USAGE
class Scenario2(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        # SCENARIO
        scenario2_title = "Scenario 2: Password Usage"
        scenario2_text = "Now even though Alice has created a new password, multiple applications require passwords. She is thinking of using her new password, but is also considering using some passwords that she already has. This would make remembering passwords easier and she would not forget them as much. \nWhat should Alice do?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Alice should just use her new password that she created since it follows best practices. It is a strong password that likely will not be hacked." , 1),
        ("Alice should use a combination of her new secure password that she just created and some of her old passwords. This way she will be able to remember all of her passwords and will not have to write them down anywhere. This will make it a lot harder for hackers to guess her passwords." , 2),
        ("Alice should create a new password for each application and should not reuse any passwords. This may make it difficult to remember all of her passwords but it will be difficult for hackers to guess her passwords. To keep track of all passwords, she could use a secure password manager." , 3)]
        # NEXT PAGE
        next = "Scenario3"

        ScenarioFrame.__init__(self, parent,controller, 2, scenario2_title, scenario2_text, OPTIONS, next)


# SCENARIO 3 - PHYSICAL ACCESS
class Scenario3(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        # SCENARIO
        scenario3_title = "Scenario 3: PHYSICAL ACCESS"
        scenario3_text = "Throughout her work day, Alice gets up multiple times to go grab a new cup of coffee or to go chat with a coworker. The coffee station and her friend are both situated on the opposite side of the floor. Whenever she leaves, she sometimes locks her computer but not always.  She also sometimes remembers to bring her badge but since she does not need it to get back to her desk, it is not at the forefront of her mind. Alice also likes to take a 15 minute walk in the afternoon to clear her mind.  Sometimes when she re-enters the building she holds the door open for other people. \nHow would you rate Alice’s actions throughout the day?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Alice’s actions are a liability to the company." , 3),
        ("Alice’s actions are not a liability to the company. Maybe next time though, she should lock her computer every time she leaves her desk so nothing gets stolen off of it." , 1),
        ("Alice’s actions are not that big of a liability to the company. Maybe next time she should not hold the door open for other people because there is the chance that they are not actual employees of the company. Instead she should have them each badge in like she did." , 2)]
        # NEXT PAGE
        next = "Scenario4"

        ScenarioFrame.__init__(self, parent,controller, 3, scenario3_title, scenario3_text, OPTIONS, next)


# SCENARIO 4 - SEPARATION OF PRIVILEGE
class Scenario4(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        # SCENARIO
        scenario4_title = "Scenario 4: Separation of Privilege"
        scenario4_text = "Alice and her coworker Bob are talking about work at lunch one day.  Bob is talking about a task that he is currently working on.  It is a task that takes a lot of work.  It turns out the Alice has access to a system that would make Bob’s job easier and she has access to confidential information that Bob could potentially use.  Alice mentions this all to Bob.  Bob then asks Alice if she could grant him access to the system and pass along the information that she has. \nHow should Alice respond?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Of course Bob. It is more important to collaborate with coworkers and share information. This way we save time and energy while completing and enhancing a task." , 1),
        ("Unfortunately, I can not grant you access Bob.  It would violate the separation of privilege." , 3),
        ("I can get you the confidential information; however, I am unable to grant you access to the systems. That is not allowed under best practices." , 2)]
        # NEXT PAGE
        next = "Scenario5"

        ScenarioFrame.__init__(self, parent,controller, 4, scenario4_title, scenario4_text, OPTIONS, next)


# SCENARIO 5 - DATA ENCRYPTION
class Scenario5(ScenarioFrame, tk.Frame):
    # INITIALIZES SCENARIO 5
    def __init__(self, parent, controller):
        # SCENARIO
        scenario5_title = "Scenario 5: Data Encryption"
        scenario5_text = "Alice is sending a series of emails containing information - both sensitive materials and non-sensitive materials to another employee on her team. \nHow should she send the information so that it is sent safely?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Alice should always encrypt sensitive information that is sent via email." , 3),
        ("Alice does not need to encrypt sensitive information since she is just sending the information to another person on her team." , 2),
        ("Alice does not need to encrypt sensitive information since she is not sending it to an outside source." , 1)]
        # NEXT PAGE
        next = "Scenario6"

        ScenarioFrame.__init__(self, parent,controller, 5, scenario5_title, scenario5_text, OPTIONS, next)


# SCENARIO 6 - PHISHING
class Scenario6(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        # SCENARIO
        scenario6_title = "Scenario 6: Phishing"
        scenario6_text = "After sending the email, Alice is going through her inbox. She finds an email from an outside source that she does not recognize but it appears legit. The email contains interesting information with a link to learn more. \nWhat should Alice do with the email?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Since it looks legit and includes interesting information, she should click the link to learn more. Learning something new never hurts anyone!" , 1),
        ("Since Alice does not recognize the email, there is a possibility that is could be a phishing email but it also may not be one.  To be safe though, Alice decides not to open the link even though she is curious." , 2),
        ("Alice should report the email to her cybersecurity group and delete the email. It could be a phishing email and Alice should take no chances." , 3)]
        # NEXT PAGE
        next = "Scenario7"

        ScenarioFrame.__init__(self, parent,controller, 6, scenario6_title, scenario6_text, OPTIONS, next)


# SCENARIO 7 - BRINGING DATA HOME
class Scenario7(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        # SCENARIO
        scenario7_title = "Scenario 7: Bringing Data Home"
        scenario7_text = "At the end of the day, Alice realizes that she was unable to complete all of her work that is due by tomorrow morning.  To ensure that she is able to complete everything by tomorrow, Alice decides to bring some of her work home with her.  She copies the data she needs onto a flash drives and packs up.  When she arrives home, she realizes that she left her laptop at work.  So she decides to use her own personal computer to finish the work that she needs to do. \nWhat are all the security violations that Alice is making?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Alice should never copy data onto flash drives." , 1),
        ("Alice should not use her own personal computer for work." , 2),
        ("Alice should never copy data onto flash drives and Alice should not use her own personal computer for work." , 3)]
        # NEXT PAGE
        next = "Scenario8"

        ScenarioFrame.__init__(self, parent,controller, 7, scenario7_title, scenario7_text, OPTIONS, next)


# SCENARIO 8 - VPN vs PUBLIC NETWORK
class Scenario8(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        # SCENARIO
        scenario8_title = "Scenario 8: VPN vs. Public Network"
        scenario8_text = "It is Friday and so Alice has decided to work from home today.  It is 9AM in the morning and Alice is craving a coffee. To satisfy this craving Alice decides to go to her local coffee shop to grab a coffee and do some work. After Alice grabs her cup of coffee, she sits down in a comfy chair and logs onto the coffee shop’s WiFi network and begins to do work. \nIs this a potential security hazard?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Yes, the coffee shop’s network is a public network.  The network is not secure. Instead Alice should log into her company’s VPN (Virtual Private Network). Alice’s VPN is a secured network and she will cause no harm to her company." , 3),
        ("No, the coffee shop’s network is secure even though it is a public network.  In the end it doesn’t matter if she uses the coffee shop’s WiFi or if she logs into her company’s VPN." , 2),
        ("No, all WiFi networks are secure" , 1)]
        # NEXT PAGE
        next = "Scenario9"

        ScenarioFrame.__init__(self, parent,controller, 8, scenario8_title, scenario8_text, OPTIONS, next)


# SCENARIO 9 - DATA MANAGEMENT / ENCRYPTION
class Scenario9(ScenarioFrame, tk.Frame):
    def __init__(self, parent, controller):
        # SCENARIO
        scenario9_title = "Scenario 9: Data Management / Encryption"
        scenario9_text = "The next week Alice returns to work on Monday.  After her morning standup meeting Alice goes and meets up with Bob to take a coffee break.  While talking with Bob, they get into a discussion about data and encryption. \nAlice believes that you should always encrypt sensitive and confidential information.  Her motto is - you can never be too careful. \nBob believes that you do not need to encrypt every single piece of sensitive and/or confidential information. The company already has countermeasures put in place if any hackers were to try and break into the systems and steal data. \nWho is right, Alice or Bob?"
        # SCENARIO RADIO BUTTONS OPTIONS
        OPTIONS = [("Alice and Bob" , 2),
        ("Alice" , 3),
        ("Bob" , 1)]
        # NEXT PAGE
        next = "Score"

        ScenarioFrame.__init__(self, parent,controller, 9, scenario9_title, scenario9_text, OPTIONS, next)
