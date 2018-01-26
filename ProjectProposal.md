# A Dungeons and Dragons Town Generator
### By The Not Neckbeards

## Team Members:
	Dakota Sanders
	Ben Johnson
	Bert Bashford
	Matt Matto

## Introduction
One of the most popular table top role playing games is called Dungeons and Dragons (henceforth referred to as DnD).
In Dungeons and Dragons, the players create their own fictional persona and role-play as those characters.
They go on adventures set out for them, in which they interact with an imaginary world and a slew of invented characters.
DnD is one example of a Tabletop Role Playing Game, and there are more games that utilize a very similar format. For the purpose of this proposal, the main use of our tool will be DnD, however this tool can be utilized for these other similar games, like Pathfinder.

The main purpose of our tool is a fictional town generator for DnD.
DnD is all about creating a story. Part of what makes a fictional story great is immersion, and immersion requires a great amount of detail.
Our tool will generate details for members in a fictional town. This includes details about the characters such as height, age, and when they moved into the town.
The most unique part of our tool is the ability to generate randomized backstories for the created characters.
In real life, major life events affect more than one person, so it makes sense for events to affect multiple people in DnD as well.
Our generator strives to achieve this effect by linking together backstories for the characters based on events specified by the user.
For example, if the user specifies a flood event in our generator, then several characters in the city may have backstories related to the events that took place during the time of the flood.

### A generalized summary of how our tool will work looks like the following:
	1. The user will run our tool natively on their computer (or possibly on the web).
	2. They will specify details about the city, like size and events.
	3. Our tool will generate a list of characters and their information.
	4. Potentially, our tool will also generate a grid-like map of the town.
	5. Our tool will conveniently display the information for the user to utilize.

There are such generators in place already, but these generators only generate basic statistics important to the game.
There is no backstory and very minimal detail regarding the town citizens.
Our generator will be different primarily because every character will have an individual backstory.

## Customer Value
The primary customer for our tool will be the Dungeon Master (DM). The DM is in charge of creating the storyline for the game, including all of the characters, activities, and map to be used.
This is an extraordinary amount of work for one person to do on their own, so many times DMs look for tools like ours or pre-made story details to add to their games. Even so, the amount of time spent still remains a huge obstacle for many DMs to overcome.

Because of the difficulty in creating a detailed plot, many times smaller details are ignored by the DM.
By using our tool, a DM does not have to worry about such minute levels of detail as would be found in a town. Our tool handles this for the DM.

As mentioned earlier, some tools and references exist already in print and online. Our tool will most likely use some storyline charts already available to DMs online.
By utilizing online resources, we can make sure our tool has a large library of events and backstories to use in making a large, detailed town.
The main purpose for using our tool is because everything is compiled into one place, and our tool makes it so that the information gathered is sorted.
Using the online resources without our app would require an enormous amount of time, most of which would be spent categorizing backstories and details.
This step can be reduced to minutes if it is automated, which is why we see a need for a tool such as this.

Our tool can be considered a success if DMs, both new to the game and experienced, can use our tool without confusion and successfully integrate the information it provides into his/her game.
Our goal is to display this information in a clear, concise way, while still allowing the user to customize details he/she wants to see. Making an options menu that allows variable town sizes and events is a high priority on our project.

## Proposed Solution
The way we plan to implement our project has some concrete goals we must achieve in order to make a working product, along with some goals we would like to achieve but are optional in forming a working app.

The main goal of the tool is to provide characters and backstories to the user. The GUI must be clear and simple to use.
Without a clear GUI, users cannot efficiently implement our project in any meaningful way, so developing this must be a high priority.

Our GUI should have a setting option, where the user can access toggles for specific details like town size, event selection, and geographical specifications. We should also have a menu to show the characters in a way that separates characters from each other and lists their details, separating into groups to show event connections.

A secondary goal of the tool is to generate a two dimensional grid map.
Our GUI should be able to display this map on the same page as the character listing, and preferably when a user hovers over a character in our list, the map will highlight the house of that character. This would make finding people and places significantly easier.

This map should be able to randomly generate geographical objects, like rivers, ponds, mountains or hills, roads, farms, etc.
This feature is not necessary for our implementation, but if it can be achieved it would generate an even greater level of detail for a DM.

For the first implementation of our tool, we plan to make a standalone computer app. However, we have a goal set to potentially transfer this tool to a web app if we can meet that goal in time.
Uploading this tool to the internet allows a broader audience and gives us room to get feedback from actual users.

## Technology
The languages we plan to utilize in developing this tool are primarily Python 3 and C++.
Potentially these languages could change if we find that they do not fit the goals we need to accomplish.

Our system has a frontend GUI that will be written using Python, and a backend that will be written using C++.
Our frontend will be set up to display information and dynamically connect our character list to our map, as well as specifying any details the user desires.
The backend will read from premade backstory charts and randomly generate certain features of characters, as well as generate a map for those characters to live in.
It will send this information to our user interface in a sorted, easy-to-parse format that will make displaying the information easy and fast.

### We have a few components to our system:
	1. A GUI to display information
	2. A backstory chart parser
	3. A sorting and linking algorithm
	4. A randomized characteristic trait generator
	5. An optional map generator

As a bare minimum, the least functional tool we would be comfortable with releasing would be one that parses backstory tables and presents them, with connected backstories.
Anything less than this benchmark would be useless, as there are already tools out there that generate characters, and the main point of our tool is to connect those backstories.

This system allows us to create many updates, adding new features every time. Some of the planned features include an entropy slider to create a more random map, integrating the tool as a web app, adding the ability to force certain events, customizing event data, and multi-event connections for characters.

We plan to do extensive testing on our tool to ensure there are no ways for a user to break our system.
As such, when we plan our agenda for the coming weeks, a bulk of our time will be spent doing unit testing on our tool.
