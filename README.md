# Space-Impact
Space Impact Video Game
Game Description: In Space Impact, the player controls the blue rectangle representing the defensive ship with the arrow keys. It can move horizontally and vertically. The player presses the spacebar to shoot bullets at the “invaders” which are the green rectangles. The goal of the game is to destroy as many invaders as possible in order to prevent them from destroying Earth. Meanwhile, the invaders shoot bullets of their own which can lower the player’s health. Health remaining is visually represented by the number of red hearts in the top right corner. As the game progresses, the number of shots it takes to kill an invader increases. You lose by either letting an invader reach the earth’s atmosphere (the left half of the screen) or by losing all 5 health units.
How to start playing: 
•	type ‘main()’ and click enter
•	You will be presented with three options
•	By clicking “play” you’ll be taken to the game.

The game utilizes 3 class functions: Heart (Polygon objects that keep track of health), Spaceship (the rectangles including the defensive ship and invaders), and Rocket (Small Circle objects which fire and cause damage to ships). When SpaceImpact() (which is a GraphWin) is called, the graph window is created and the user’s ship is created. The hearts representing the ship’s health are created and drawn. The number of hearts created depends on how much health is given to the ship when created. When the function play() is initiated, the prompt shows up and waits for the user to click on the screen before beginning. The program then begins tracking time steps which is defined by the number of times the whileloop is completed. At the beginning of each loop, the program makes sure that the number of hearts accurately represents the health of the ship. If health refills (which won’t happen in this version) the hearts turn back to red. The window then performs checkKey() so that the user can move the ship and fire bullets.
The program was being designed so that the more kills the player got, the more frequently the invaders would shoot bullets and the more bullets it would take to kill each invader. Due to time constraints, only the latter function was achieved. Additionally, after achieving a certain number of kills, the bullets of the user’s ship changes colors. The original red bullets are regular speed, the blue ones are faster, and the purple ones are fastest. Also, after 1000 timesteps, the invaders move slightly faster. You may notice that the invaders move at different speeds. This is because of the use of randomness when defining how many pixels they move in each timestep.
How bullet collisions are detected: Each timestep, the program goes through its list of bullets. Each bullet goes through the list of ships and checks if it hit a ship with the rocket object checkContact(). 
Bugs and room for improvement:
One major bug that I haven't fixed yet is that if the program generates invaders too quickly, it will stop tracking kills. By making print statements, I found out that bullets would detect contact and would even determine if a certain hit was fatal, but the main program would not enter an if statement which counts the kill. I figured out that this problem occurred if there were three or more invader ships in the screen at a time.
You will notice that after getting game over, the game reports the number of kills and the high scores. Unfortunately these scores aren’t authentic, however they are imported from a separate txt file from the folder I shared. The vision was to have the game automatically update this txt file with players’ scores.
I wanted to make health packets so that the user’s ship touched them they would regain full health. This would be done with the Heart’s revive() function that I wrote. I was planning to use the randrange function so that every certain number of timesteps there would be a 1/5 chance that the health package would be made. I didn’t get to this because of time constraints.
Right now, the game is fairly easy. One way that I would like to make it more challenging is by getting the invaders to shoot direction at the ship. Using a helper function to determine what dy value their bullets would need won't be too complicated to do.
