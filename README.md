Skip to content
Jaaz7
/
dice-mania

Type / to search

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Breadcrumbsdice-mania
/
README.md
in
main

Edit

Preview
Indent mode

Spaces
Indent size

2
Line wrap mode

Soft wrap
Editing README.md file contents
Selection deleted
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
# Dice Mania
**A game where the player bets tokens to guess the total sum of a dice roll.**
<br><br>
Dice Mania is a simple idea which can be compared to classic dice games due to its randomization. It's all about luck and unpredictability, keeping it interesting and fun.
<br><br>
<img src="https://github.com/Jaaz7/dice-mania/assets/130407877/b9c67ae4-0f73-46df-9619-20aa656e38c0" width=90% height=90%>
<br>
**[Visit the live project here.](https://dice-mania-d8c8705be82a.herokuapp.com/)**

---
# Table of Contents
- ### [How To Play](https://github.com/Jaaz7/dice-mania#how-to-play-1)
- ### [Logic Flowchart](https://github.com/Jaaz7/dice-mania#logic-flowchart-1)
- ### [User Experience (UX)](https://github.com/Jaaz7/dice-mania#user-experience-ux-1)
- ### [Features](https://github.com/Jaaz7/dice-mania#features-1)
  - [Existing Features](https://github.com/Jaaz7/dice-mania#existing-features)
  - [Features Left To Implement](https://github.com/Jaaz7/dice-mania#features-left-to-implement)
- ### [Design](https://github.com/Jaaz7/dice-mania#design-1)
  - [Colors](https://github.com/Jaaz7/dice-mania#colors)
  - [Art Title](https://github.com/Jaaz7/dice-mania#art-title)
  - [Flowchart](https://github.com/Jaaz7/dice-mania#flowchart)
- ### [Technologies Used](https://github.com/Jaaz7/dice-mania#technologies-used-1)
- ### [Frameworks, Libraries & Programs Used](https://github.com/Jaaz7/dice-mania#frameworks-libraries--programs-used)
- ### [Testing](https://github.com/Jaaz7/dice-mania#testing-1)
  - [Manual Testing](https://github.com/Jaaz7/dice-mania#manual-testing)
  - [Input Validation Testing](https://github.com/Jaaz7/dice-mania#input-validation-testing)
- ### [Bugs](https://github.com/Jaaz7/dice-mania#bugs-1)
  - [Fixed Bugs](https://github.com/Jaaz7/dice-mania#fixed-bugs)
  - [Bugs Left To Fix](https://github.com/Jaaz7/dice-mania#bugs-left-to-fix)
- ### [Deployment](https://github.com/Jaaz7/dice-mania#deployment-1)
  - [Local Cloning](https://github.com/Jaaz7/dice-mania#local-cloning)
  - [Deploying To Heroku](https://github.com/Jaaz7/dice-mania#deploying-to-heroku)
  - [Forking The Github Repository](https://github.com/Jaaz7/dice-mania#forking-the-github-repository)
- ### [Credits](https://github.com/Jaaz7/dice-mania#credits-1)
  - [Code](https://github.com/Jaaz7/dice-mania#code)
  - [Content](https://github.com/Jaaz7/dice-mania#content)
- ### [Acknowledgements](https://github.com/Jaaz7/dice-mania#acknowledgements-1)

---
## How To Play
  - The starting screen gives the user an option to read the rules.
  - Once this option is chosen, the player is prompted to charge their balance with the game's currency: tokens.
  - Once the tokens are accepted, a message will indicate it was successfully submitted.
  - The player will then start the game. They will be prompted to pick their bet, their dice number and their play option.
  - The play options are "More", "Less", and "Same".
  - Once chosen, the dice will be rolled and it will be decided whether the player wins or loses. This completes a play.
  - Winning means 2x the bet value, but there's also a jackpot that can be won if the player chooses 4 dice with the option "Same".
  - The player can then choose to continue, to top up or to quit the game. Topping up means adding more tokens to the current balance.

---
## Logic Flowchart
  - <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/e8d0b9c7-0ae3-448d-b557-e9a29ca0417e" width=90% height=90%>

---
## User Experience (UX)
  - Dice Mania presents itself as an understandable and easy-to-interact game from the beginning.
  - With different color schemes and an option to reveal the rules, it not only highlights important aspects and numbers of the game but it also increases its replayability, resulting in a cleaner experience for returning users.
  - The premise is to guess the total sum of the next dice roll against a number known before, it's easy enough to be interacted and quickly understood by people of all ages.
  - The game has helpful tips that keep remembering players of things they can do.
  - Its questions highlight the important input that is required by the player with colors.
  - It has a 4x winning bet if the player wants to be riskier, it provides a good reward system that motivates players to go for big plays.
  - The player is motivated to invite friends to play Dice Mania.
  - Delay in key moments such as input questions will allow the player to read important information such as remaining balance before the next code runs, this results in a better game pace.

---
## Features
  - ### Existing Features
    - Starting screen
      <br><br>
      Displays the logo, a welcome message and some tips:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/1b54b57b-847b-42a6-8966-966f64668d50" width=70% height=70%>
    - Show rules
      <br><br>
      Rules are shown when choosing "y":
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/2b277fd9-4dbc-4e95-8f30-32f26b6fcd0f" width=70% height=70%>
    - Charge tokens prompt
      <br><br>
      Confirmation that tokens were accepted:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/ace9638f-95c8-479e-bbe6-c67383c81d26" width=50% height=50%>
    - Bet prompt
      <br><br>
      Before betting, the player is reminded of how many tokens they have and what's their current mania number
    - A counter of how many games currently played.
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Editing dice-mania/README.md at main · Jaaz7/dice-mania