alx_python_game
Introduction and Team Member Role

This project is a solo endeavor, with Thomas Kitaba as the sole team member.
Inspiration

The inspiration for this project dates back 17 to 18 years ago during a technology transformation in Ethiopia. The shift from landline to wireless phones coincided with the popularity of Nokia's Snake game.
How to Play the Game
Game Controller

On Windows:

    UP arrow key: Move UP
    DOWN arrow key: Move DOWN
    RIGHT arrow key: Move RIGHT
    LEFT arrow key: Move LEFT

On Android or Touch Screen Devices:

    UP arrow image on screen: Move UP
    DOWN arrow image on screen: Move DOWN
    RIGHT arrow image on screen: Move RIGHT
    LEFT arrow image on screen: Move LEFT

Technology and Architecture
Pictures for Slide:

    Android Phone, Tablet, and PC

Requirements to Run the Game:

    Android version 7 and above
    Windows 8 and above
    No additional software required

Movements Within the Game

The game involves movements from the beginning to the end.
Process
Score

    Every time the snake eats, it grows.
    For every valid food eaten, a single point is added to the score.
    The score does not decrease by any means.

Game End

Since "endless mode" is chosen for the MVP, the game is playable endlessly. The next version aims to record collisions, such as when the snake hits a meteor or attempts to eat its own body, to display a renowned GAME OVER screen.
Levels

There are infinite levels, and level changes occur after certain milestones, affecting the speed on each level.
Algorithm and Code Snippets

Major aspects of the game ensuring smooth gameplay involve collision handling. This includes:

    Resetting Game: Triggered by collisions with a meteor or the snake itself, resetting the snake to its starting location.

    Changing Level &/or Score Change: Occurs when the snake's head collides with any part of its body.

To implement these game parts, a program checks randomly generated food coordinates to ensure they don't appear too close to specified meteor locations.
Getting Deeper into the Game
Skills and Knowledge Required

    About Images:
        Image size editing is crucial for the game's look and package size.

    Codes:
        The snake is a 2D array or list, and knowledge of the pygame module and Python data structures is essential.

    Maths and Codes:
        Implementation requires a detailed understanding of basic coordinate geometry.

Distance Calculation

Collision detection relies on the Pythagorean theorem for distance calculation.
Changing Levels

A single food is eaten for a level change. To test if randomly generated food is spawned appropriately, an algorithm is written to check the distance between the food and specified meteor locations.
Process Collaboration

The project was undertaken individually to avoid putting others at risk due to the need to learn a new pygame module.
Challenges Overcome

    Pygame Module: Required effective learning.
    Editing Audio and Images: Time-consuming task.
    Contrast Ratio: Achieving the recommended ratio was challenging due to diverse image compositions.
    Unittest with Pygames: Unusable due to freezing issues, necessitating manual beta testing.

My Other Works

Explore my graphic design work (https://sites.google.com/views/thomaskitaba/my_graphics_works)
and a mini art creation app made using pygame (https://sites.google.com/views/thomaskitaba/).
Additionally, check out a screen shot of web app for daily diary logging (https://sites.google.com/views/thomaskitaba).
Portfolio Presentation

The portfolio presentation included:

    Introduction of team members and roles (1pt)
    Story of project inspiration (1pt)
    Technology and architecture (5pt)
    Core algorithms and code snippets (5pt)
    Discussion of process, collaboration, and timeline (2pt)
    Overcoming challenges (5pt)
    Learnings about technical interests (1pt)

If you want to see my graphics design work, visit https://sites.google.com/views/thomaskitaba/my_graphics_works

I have a mini art creation app i made using pygame.

 I have also made a web_app to help me log diaries daily. visit  https://sites.google.com/views/thomaskitaba/apps.


Just as a reminder the portifolio project had presention with the following content.

    1. Introduction of team members, and each person’s role (1pt)
    2. Story of how your project was inspired (1pt)
    3. Technology & Architecture (5pt)
    4. Core algorithms and code snippet (5pt)
    5. Discussion of process, collaboration and timeline (2pt)
    6. Challenge(s) overcome (5pt)
    7. Learnings about technical interests as a result of this project (1 pt)
