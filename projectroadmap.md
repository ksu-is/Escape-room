# Project Roadmap

# Sprint 1

## Codebase Abandoned 

Pythonescaperoom was the first codebase I looked at, but it was much too complicated for what I wanted. It relied on dynamic module 

loading, multiple class files, and even a Flask web server. Furthermore, it required advanced Python concepts and a particular folder 

structure that are way outside the purview of my job.

I spent time reading through the files and attempting to run the project, but it became clear that:

- It took longer to set up than anticipated.
  
- It made advantage of sophisticated technologies like dynamic level loading, Flask routes, and importlib.
  
- It wasn't meant to be a straightforward text adventure, but rather puzzle-based code challenges.

I decided the code was not a suitable fit for my project after looking it over and trying to execute it, so I switched to a different codebase.

## Codebase Search pt 2.

I analyzed the ThoughtWorks Spy Safe Spaces Game on my second try. This project was simpler to understand and far more modern in style.  
It contained:

- A class named SafetyFinder
  
- A wide range of Python unit tests
  
- Clear function-based reasoning
  
- A straightforward structure free of unnecessary structures
  
This codebase was simpler to evaluate and operated successfully. However, the focus remained on algorithmic puzzles and grid-based

logic rather than narrative or chamber exploration.


## What I learned from the codebase, what it does, etc

I learned a few helpful principles from the ThoughtWorks codebase:

- How to organize functions neatly
  
- How to deal with edge cases, lists, and coordinates
  
- How expected behavior is referred to through unit tests
  
- How to separate an issue into smaller steps
  
The project helped me understand even if it is about locating secure hiding places on a grid rather than getting out of a dorm:

- Simple function design
  
- Flow of input, processing, and output
  
- How to arrange a class's code
  
Although I won't be using the code directly, I will draw ideas for my own project from its organization and clarity.


## Sprint 2
I'll start working on my own game, Escape the Dorm, for Sprint 2. It's a text-based adventure where the player has to locate their 

shoes, backpack, and keys before time runs out.

### Core features I will build first
 
- Move between roomsLook for things
- Keep track of inventory
- A countdown clock
  
I will have a basic, functional version of the game thanks to these features.

### Features I may consider later

- Random item locations
- Additional rooms 
- More endings
- A replay feature
  
### Tools and approach

I'll only use basic Python (functions, loops, and conditionals) to create the game.

As I proceed, I'll update GitHub with my progress.

# Check list

- [x] Created main.py (I set up the main game file and added the starting structure)
- [x] Added intro text (Wrote the welcome message that explains the goal of the game)
- [x] Added room movement (Created a function that lets the player move between the Dorm Room, Hallway, and Outside)
- [x] Added search function (Built a search feature so the player can find keys, backpack, and shoes in different rooms)
- [x] Added inventory (Made a list to store found items and display them when the player checks inventory)
- [x] Added timer (Added a timer that decreases each turn and ends the game if time runs out)

## Sprint 3 — Final Reflection (in process)

When the project is finished, I will write about:

- What I really created 
- What was changed from my initial plan (I ended up moving the countdown timer for the game to say if you won before the time ran out or not)
- Any difficulties I encountered 
- What I learned  
- What I could do better with more time
