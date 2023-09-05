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

---
## Features
  - ### Existing Features
    - Starting screen
      <br><br>
      Displays the logo, a welcome message and some tips:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/1b54b57b-847b-42a6-8966-966f64668d50" width=70% height=70%>
    - Show_rules
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
      <br>
      After the bet is accepted, a messaeg will confirm this and display the remaining tokens:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/34770609-1341-4dc8-85ec-e4df77aa28d8" width=50% height=50%>
    - Choose dice number prompt
      <br><br>
      A tip reminding about the jackpot is shown
      <br>
      Confirmation that the dice number was accepted:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/e9d582c9-acd8-4b4b-acc0-701ea69ac0f8" width=60% height=60%>
    - Choose play option prompt and conclusion of the play
      <br><br>
      After choosing, the dice are immediately rolled
      <br>
      The dice ASCII art is shown is a randomized matter. A message appears revealing the total sum, which is the new mania number
      <br>
      A message is shown revealing if the player wins or loses, as well as a message depicting the play option choice
      <br><br>
      A direct comparison of mania numbers is shown for clear understanding why the player wins or loses
      <br>
      A message revealing the player's new token balance is shown
      <br>
      A separator is printed to detach each play from the other, for visibility purposes
      <br><br>
      If the player wins, a message in cyan color clearly demonstrates a positive outcome and the tokens won are shown:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/392682d9-dff8-45e6-af0c-1ffc0410a485" width=60% height=60%>
      <br><br>
      If the player loses, a message in red color clearly demonstrates a negative outcome:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/dc5593c9-0e2b-4df9-8bab-196e874b2ef6" width=60% height=60%>
      <br><br>
      If the player wins the jackpot, a message in yellow color explains it and the tokens won are shown:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/ba95c0ea-2392-497e-b433-bbbd57b97185" width=60% height=60%>
    - Betting all the balance
      <br><br>
      If the player bets all their balance, a different message will appear
      <br>
      clearly demonstrating their balance in a red "0". Confirming they've just made an all-in.
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/9d9ad8c6-f498-4585-a574-b79b2cf82f72" width=50% height=50%>
    - Quitting
      <br><br>
      If the player quits, a message thanks the player for playing and shows the total tokens they've redeemed.
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/b89edfb3-70d5-4253-9d42-76448869aca7" width=50% height=50%>
  - ### Features Left To Implement
    - Option to cancel the top up, going back to the pervious menu.
    - Option to play with more than 4 dice.
    - There could have been different kinds of prizes.

---
## Design
  - ### Colors
    - Yellow.
    - Cyan.
    - Red.
  - ### Art Title
    - [ASCII art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
  - ### Flowchart
    - [app.diagrams.net](https://app.diagrams.net/)

---
## Technologies Used
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---
## Frameworks, Libraries & Programs Used
  - [VS Code](https://code.visualstudio.com/)
    - To write code.
  - [Termcolor](https://pypi.org/project/termcolor/)
    - To use colors in the project.
  - [Git](https://git-scm.com/)
    - For version control.
  - [Github](https://github.com/)
    - to Deploy the website and storing files online.
  - [Text to ASCII art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
    - to create art for the project.
  - [App.diagrams.net](https://app.diagrams.net/)
    - To create a logic flowchart diagram.
  - [Heroku](https://www.heroku.com/)
    - To deploy the project.
  - [CI Python Linter](https://pep8ci.herokuapp.com/)
    - To check the code for issues.

---
## Testing
  - ### Manual Testing
    - CI Python Linter was used to test run.py
      <details><summary>Click to expand</summary>
      <img src="x" width=90% height=90%>
      </details>
    - The game was manually tested extensively from start to end while coding it, the website was deployed to heroku at a relative early stage with automation on because further testing was necessary to know how the app looks online.
    - Testing of logo ASCII image display, rules display, tokens input validation, bet input validation, dice number input validation, play option input validation, menu choice input validation (continue, top up, quit) and top up            validation were done and improved upon.
  - ### Input Validation Testing
    - Display rules
      <br><br>
      Must be "y" or "n":
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/f0a6a8d1-cc82-4dc1-9fe7-e2715cf44b85" width=50% height=50%>
    - Charge tokens
      <br><br>
      Must be a number between 1 and 500:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/ac51cdfd-f38e-445a-85f8-14d4a6370f17" width=75% height=75%>
    - Place bet
      <br><br>
      Must be a number between 1 and current balance:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/ce8e8ab7-e88b-4008-b8d9-8ffd3fe8d94c" width=75% height=75%>
    - Choose dice number
      <br><br>
      Must be a number between 2 and 4:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/d64aa420-8194-4738-a11f-a5e991f506fa" width=70% height=70%>
    - Play option
      <br><br>
      Must be "m" or "l" or "s":
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/c4d275fc-66b4-4083-a357-6f49744ab494" width=40% height=40%>
    - Final menu
      <br><br>
      Must be "c" or "t" or "q":
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/b36ee79b-f630-4f16-ac3a-e294e6c627d3" width=40% height=40%>
    - Top up
      <br><br>
      Must be a number between 1 and 500:
      <br>
      <img src="https://github.com/Jaaz7/dice-mania/assets/130407877/fb6b1cbc-ce0a-4bf4-a055-cad881f26624" width=75% height=75%>

---
## Bugs
  - ### Fixed Bugs
    - Fixed a bug where the dice were not being updated, Turns out the variable to carry on the updated dice number from the second game on was wrong.
    - Fixed a bug where the topped up tokens were not being carried on to the next loop, this was an easy fix as I was using the var wih the old token balance instead of the updated one that was topped up.
    - Fixed a bug where the old dice roll sum was not being accounted for (the mania number). This was a matter of inverting both variables I was using to do the math with the old plus new mania numbers.
    - Fixed a bug where if you bet your total balance and win, the game stops. This was an easy fix because the variable being used to pass on the tokens was the old one (with a value of 0), not the variable with the new balance, which accounts the bet that was just won.
  - ### Bugs Left To Fix
    - No detected unfixed bugs.
---        
## Deployment
  - ### Local Cloning
    ‎1. Log in to GitHub and locate [GitHub Repository dice-mania](https://github.com/Jaaz7/dice-mania).
    <br>
    ‎2. Click on the green code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
    <br>
    ‎3. Open Git Bash.
    <br>
    ‎4. Change the current working directory to the location where you want the cloned directory to be created.
    <br>
    ‎5. Type `git clone` and then paste The URL copied in step 3.
    <br>
    ‎6. Press Enter and your local clone will be created.
  - ### Deploying to Heroku
    To deploy to Heroku, Code Institute Python Essentials Template was used so the python app can be viewed in a terminal in a browser.
    <br><br>
    ‎1. Log in to Heroku or create a new account.
    <br>
    ‎2. On the main page click "New" and select "Create new app".
    <br>
    ‎3. Choose your unique app name and select your region.
    <br>
    ‎4. Click "Create app".
    <br>
    ‎5. On the next page find "settings" and locate "Config Vars".
    <br>
    ‎6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add".
    <br>
    ‎7. Scroll down, locate "Buildpack" and click "Add", select "Python".
    <br>
    ‎8. Repeat step 7. only this time add "Node.js", make sure "Python" is first on the list.
    <br>
    ‎9. Scroll to the top and select "Deploy" tab.
    <br>
    ‎10. Select GitHub as deployment method and search for your repository and link them together.
    <br>
    ‎11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy".
    <br>
    ‎12. Deployed website [Dice Mania](https://dice-mania-d8c8705be82a.herokuapp.com/).
  - ### Forking The Github Repository
    By forking the repository, a copy of the original one is made inside the GitHub account. This is important if one wants to view and make changes to a project without affecting the original. The steps are the following:
    <br><br>
    ‎1. Log in to GitHub and locate [GitHub Repository dice-mania](https://github.com/Jaaz7/dice-mania).
    <br>
    ‎2. At the top of the Repository, under the main navigation, locate "Fork" button.
    <br>
    ‎3. Now there should be a copy of the original repository in the GitHub account.

---
## Credits
  - ### Code
    - Gained understanding of python through the Code Institute lessons.
    - Gained knowledge about looping through ASCII dictionaries with @CodingProfessor on [YouTube](https://www.youtube.com/@CodingProfessor).
    - Python 3.10.12 documentation.
    - [Termcolor Library](https://pypi.org/project/termcolor/) color documentation.
    - [InventWithPython](https://inventwithpython.com/bigbookpython/project17.html). Dice ASCII art concept, implentation and logic.
  - ### Content
    - Game idea given by mentor Mitko Bachvarov.
    - All code and content were written by Jaaziel do Vale.

---
## Acknowledgements
  - Mentor Mitko Bachvarov for providing constructive feedback.
  - Slack community and tutors for help and observations.