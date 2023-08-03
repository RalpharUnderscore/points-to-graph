# Simple Graph Generator

Quick Access (Desmos Links):
- Linear Graph: https://www.desmos.com/calculator/kwi1uxjyev
- Exponential Graph: https://www.desmos.com/calculator/n04xtodhq4
   

Simple Graph Generator allows you to create a linear or exponential graph from either two points, or the constants of each formula.  
The formula for calculating linear graphs is y = mx+c, where m is the gradient and c is the y-intercept.  
The formula for calculating exponential graphs is y = ab^x, where a is the inital (or y-intercept) and b is the exponential's base.  
If you would like to experiment more with how the graph is calculated, I recommend visiting the Desmos Links above. You can also access by clicking the two green buttons on the top of the software.

## FAQ (Frequently Asked Questions that I made up and were not frequently asked at all):
Q: Why did you even make this?  
A: Serious Answer. This is my 3rd tkinter project I've worked on. I was thinking of developing my first "serious" video game. 
I wanted it to be mechanically simple to program since it was my first one so I thought about clicker games. As I thought more 
about it I came to realize that setting the cost for each level of an upgrade would be very time-consuming. The solution I'm opting 
for is to manually set values for the first and last level of the upgrade and have everything in between to be filled in by an exponential graph. I decided to create a python script that would return the y value for every x value in between the two points 
the user inputs. A month later after not using tkinter for a while I decided to work on this project just to see if I could do it. 
This program is a lot bigger than my last one. 
  
TLDR: Mainly made it just because it was fun.  
  
Q: How long did this take?
A: I'm not too consistent updates. I just update whenever I feel like it but the Initial Github commit is July 8th. v1.0 will go live on Jul 25th.  
  
Q: The code is horrendous.
A: First of all, that's not a question. Second of all, you are absolutely right. Writing code is not difficult once you learn the  
ropes. Code readiability and optimization is a whole other beast I'm trying to work on.  

Q: Why is the maximum amount of points 10?  
A: It's a clean number to end at. Also, additional ones wouldn't fit inside the window. 
If you would like to circumvent this, replace Line 415 in GraphGen.pyw from toplevel.resizable(False, False) -> toplevel.resizable(True, True)  
Then, comment out Line 40-42 in _plot.py by putting # in front.  
You should be able to resize the Graph Controls window and there won't be a limit anymore.
  
Q: Where is are the list of randomly generated titles and point names stored?  
A: In _namelist.py  
  
Q: Why does the Plot button open two graphs when I close the graph window by myself?  
A: Why did you close the graph window then??  
  
Q: Don't you think spliting the calculation into _lin.py and _exp.py is unnecessary?  
A: Yeah probably lol  
  
Q: Self-Promotion?  
A: I'm glad you asked. 
https://github.com/RalpharUnderscore?tab=repositories  
https://hiddenkendo.itch.io/pizza-escape  
https://soundcloud.com/ralpharisntcool  


