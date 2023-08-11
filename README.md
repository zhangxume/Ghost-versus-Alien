# Ghost versus Alien

#### Description:
> 👻 Ghost versus 👽 Alien game.  
This is a simple python game played in the terminal window.  
In this game, you will play as a ghost character and your rival is an alien. Each character has corresponding attributes. Each character also has an attack function and a defense function, if the character is attacked, it will reduce HP which use ❤️ as the symbol, and if actively defending, it can avoid receiving damage. Finally, the winner will receive a shiny award cup 🏆
- How to play
> just run `project.py`
- Attributes
> `name` the name of the character  
> `level` the level of the character  
> `maxhp` a character's max health point initialized at the beginning of the game  
> `hp` a character's current health point  
> `lasthp` lasthp means a character's health point in the previous round of battle  
- Methods
> `attack` to attack your rival  
> `defense` defend against attacks from rival  
The script uses `random` and `sys` libraries to generate the alien's level randomly as its hurt value, sys is used to catch exception during the game and avoid interrupt the program unfriendly.
Notice, there may be slight differences in the display of Emoji on different systems.
The script can be interrupted at any time by pressing `Ctrl + D`, which will print a goodbye message and exit gracefully.
- Possible ways to optimize this program in the future  
> Optimize the structured writing logic of this program to reduce redundancy and contact coupling situations  
> Add more special method for each character with interesting functions  
> generate more character for user to choose  
> Add a beautiful user graphical interface  
> ......
