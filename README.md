alx_python_game
==================================
INTRODUCTION AND TEAM MEMBER ROLE.

The project i had in mind, requires to read and know a new pygame module, which was not introduced in the program. So   not to put others in a risky situation i chose to do it alone.

so i am the only team member and my nane is thomas kitaba.
==================================

 INSPIRATION.

17 or 18 years a go, there was this technology transformation in our country Ethiopia. Where land line phones were being replaced by wireles phones.

during that time nokai had this snake game. where every one was playing.
==================================
HOW TO PLAY THE GAME
=> GAME CONTROLLER
This depends on the device on which you are playing the game. there are two options for this.

ON WINDOWS:
- UP arrow on key keyboard: to move UP
- DOWN arrow key on keyboard: to move DOWN
	- RIGHT arrow key on keyboard: to move RIGHT
	- LEFT arrow key on keyboard: to move LEFT.
To play the game if you are on android phone.

ON ANDRIOD phone or ON TOUCH

SCREEN LAPTOP or tablet.
- UP arrow image on screen : to move UP
- DOWN arrow image on screen : to move DOWN
	- RIGHT arrow image on screen: to move RIGHT
	- LEFT arrow image on screen: to move LEFT.

==================================
3. TECHNOLOGY AND ARCHITECTURE
Pictures for SLIDE:
- ANDROID PHONE, TABLET and PC

REQUIRMENT TO RUN THE GAME
- Android version 7 and above
- windows 8 and above
no additional softwares required

=> MOVEMENTS WITH IN THE GAME
	The movments involved with in the

game, starting from the begning of the game up to the end of the game.


=========== PROCESS ==========
=> SCORE:
every time the snake eats it grows for       every valid food it eats a single point is        added to the score.
and  the score wont decrease by  any       means.

=> GAME END:
since i have chosen "endless mode"
for my mvp. the game is playable endlessely. but to make it more competitive,
the next version will be made to record collisions (every time the  snake hits a
meteor or if it tries to eat  its own body ) so that get the most
reknowned GAME OVER screen.


=> LEVELS: There are infinite levels
- level change happens after
that change speed on each level.



=== ALGORITHM AND CODE SNIPITS ====


Major part of the game that makes sure the gamer is playing the game smoothly.
IS related with collission, these game parts include.

	RESETING GAME:- Which happens for  two reasons when ..
- The snake collids with meteor
- The snake collids with itself


reseting  snake to its starting location)

	CHANGING LEVEL &/or SCORE CHANGE: which happens when the snake head collids with any part of it’s body

before we start explaining, the algorithms within the game, we should first understand what and how we are going to implement part of the game requiring algorithm.


a small program is written to check if the randomlly generated food coordinate doesn't appear  40m from the allready specified meteor location,     the random numbers are going to be generated 1000 times end distance with the meteors is

checked for those 1000 cases.

=== GETING DEEPER INTO THE GAME ===

NOTE: To make this game the skills, and knowledge required are.
	1. About Images:
specially editing size of an image is mandatory for 2 main reasons.
1.1 LOOK of the game: unproportional images will drag your excellent code down to grave.
1.2 SIZE OF apk, or package:  if size of an image is not commpressed enough in such a way that the image is in a state where it is not too small to decrease the quality of the games graphics or it should not be so big that it requires much cpu power and/or memory which can make the game run slower or even crash.

CODES:
the snake it self is an 2D array or 2D list.
		- pygame module:
			about pygame module:
		- knowlege of python data structure specifically knowledge of python list  is required.

	3. Maths and CODES involved in  making the game involved.

		- IMPLEMENTATION:
		- detail knowledge of basic 								coordinate geometry.
To detect collision with meteor and to detect if a spawned food has been swallowed or not. distance beyween the sprites in question should be calculated.
DISTANSE CALCULLATION:
Distance calculation is performed using

the concept of pythagores theorm.
hypotenous sqr = adjucent sqr + opposit sqr
where hypotenous = distance between objects


To change: LEVEL a single food is eaten
 if swallow_food_2< block:
    SCORE_2 += 1

# change SCORE_2 += 1 to SCORE_2 += 10

=> To test if randomly generated food is spawned approperiatly,  algorithm  written to check if the randomlly generated food coordinate doesn't appear  40m from the allready specified meteor location,     the randome numbers are going to be generated 1000 time, end distance with the meteors is checked for those 1000

cases.

for i in range(1000):
# generate 2 random numbers
# for x coordinate: 0 upto screen_width
# for y coordinate: 0 upto  screen_height

	x_test = int(random.randint(0,screen_width - 40))
y_test = int(random.randint(0,screen_height - 40))

METEOR numbers WITH in each level amount to
Level 1: 1
Level 2: 2
Level 3: 2
Level 4:3
Level 5: 3
Level 6: 3
Level 7: 4

Level 8: 4
Level 9: 4
Level 10: 5

This keeps happening for
Level = Score % f_t_c_l
Where f_t_c_l = food to change level
Explanation: everytime the score gets a value that is a multiple of f_t_c_l which in our case is 10, the level changes

to make the game a little bit interesting and challenging. The number of meteors with in each level has been made  to increase in number every time the level changes

==================================
 PROCESS COLLABORATION.
	- The project i had in mind, required to read and know a new pygame module,

which was not introduced in the program. So   not to put others in a risky situation i chose to do it alone.

=========================
6. CHALLENGES OVERCOME
	Pygame module: required to read how to use pygame module effectively

	Editing audio and images for the game required lots of time.

	Achieving the minimum contrast ratio recommended by  for foreground and background content (4.5:1) was a little bit hard because the images were composed of different

	Using pygames Unittest was unthinkable because adding return value to our function made the whole

game freeze  when it reaches the line of code that returns a value return location. So i was forced to do the manual testing beta testing myself.

=========================
 MY OTHER WORKES

If you want to see my graphics design work, visit https://sites.google.com/views/thomaskitaba/my_graphics_works

I have a mini art creation app i made using pygame. https://sites.google.com/views/thomaskitaba/apps

 I have also made a web_app to help me log diaries daily. visit  https://sites.google.com/views/thomaskitaba/apps.


Just as a reminder the portifolio project had presention with the following content.

1. Introduction of team members, and each person’s role (1pt)
2. Story of how your project was inspired (1pt)
3. Technology & Architecture (5pt)
4. Core algorithms and code snippet (5pt)
5. Discussion of process, collaboration and timeline (2pt)
6. Challenge(s) overcome (5pt)
7. Learnings about technical interests as a result of this project (1 pt)

icl
