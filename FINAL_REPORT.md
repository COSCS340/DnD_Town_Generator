# A Dungeons and Dragons Town Generator
### By The Not Neckbeards

## Team Members:
	Dakota Sanders
	Ben Johnson
	Bert Bashford
	Matt Matto

## Introduction
One of the most popular tabletop roleplaying board games is known as Dungeons and Dragons.
For the purpose of this report, the game will be referred to as DnD.
The game revolves around player-created characters that explore a campaign created
by another player known as a Dungeon Master (DM). One of the most challenging
parts of being a dungeon master is the task of creating the campaign that the
players will play in. Part of this creation involves generating non-player-characters
(NPCs), who are characters that are not created by normal players, but are still
expected to be able to interact with player-made characters. This creates a
difficult situation for the DM, because it's hard to have backstories of every
character in a campaign.

This problem prompted us to create an application that would generate some
details about the NPCs so that the DM does not have to spend nearly as much time
creating details like names, ages, backstories, and other relevant details.
Our approach to this application is one that should allow users to upload files
that fit a certain format, so that all one has to do to add more details
is change the content of the uploaded files. This approach allowed us to
work on generating random characters while still allowing users to customize the
details available to them.

At the start of our project, we decided we wanted to set a secondary goal of map
generation. This goal would take the generated NPCs and place them on a grid
that would show the map of the town.
This goal ended up not being completed due to time restraints. To generate a
town, the level of detail required and the time needed to complete the project
was going to be much more than we could afford for the class.

Our primary goal was completed, as the project will properly generate random
characters correctly. Our secondary goal of map generation was not completed.
Our interface ended up being clean and simple to use, so overall the project
was a success.

## Customer Value
Our project has undergone some significant changes throughout the course of the
semester. The primary change has been to the user interface, as we decided to
modify the way our navigation code worked. We also significantly reduced features
of the character generation in order to increase the overall stability of our
final product.

The adoption of the new GUI took place sometime in late March. The reason for
this change was due to the developments that Ben Johnson did in his goal to
create a wizard. The wizard aspect of our app creates a seed for a town, which
contains the potential character information needed to load and generate a
town. During the course of this development, we as a team were having some
trouble keeping the already-developed toolbars accessible during changes to the
main windows. For example, navigating from the home page to the wizard page would
require significant code changes to simply display the same menu already available
on the previous page. In order to fix this problem, Ben implemented a new format
for all of the windows to follow. This format involved creating a parent view class
that would allow any child windows (i.e. the main menu, wizard, display and help screens)
to inherit the necessary menu structure and navigation screens. This solution
was significantly better suited to our needs than the work that had already been
done on the menu screen to date. As such, we decided as a group that adopting this
new format was going to save us time in the long run, and contribute to a cleaner,
easier to understand codebase as a whole.

Originally, our application sought to generate data specifically for the town
itself. This included events that were town-specific that would appear in
several of the NPCs backstories. We also wanted to have NPC to NPC interactions
available so that certain NPCs would have the unique capability to be
related to another NPCs through events or other factors. Both of these features
proved to be too ambitious due to the time needed to do important tasks like
bug-fixes. We realized around April that the code modifications needed to include
this functionality were going to be far too much to add before the end of the
semester. It turns out that adding code that will link certain NPCs together
creates a myriad of problems, primarily in that certain interactions should not
be allowed if other actions are present. As such, it would have taken far too
much time to implement, and we did not feel as though it was necessary for our
minimum viable product.

## Technology

![ScreenShot](screenshots/MainMenu.png)
###### Above Screenshot is the opening menu of our application.

Our minimum viable product for this semester was an app that would generate
and display the characters within the town. By the time our group presented the
project, we had completed the MVP and were ready to begin adding extra functionality.
One of the things we finished actually before the MVP was even done was the
ability to generate, save, and load seeds and towns. We also implemented functionality
to undo any additions made within the town wizard. Both of these additions
were not necessary for the minimum viable product, but we managed to create those
at the same time we implemented some of the other important features within
our app.

Our application is broken down into 4 main sections: the Main Menu, the Wizard,
the Display Page, and the Help Menu.

The Main Menu and Help menu are just display pages. The main menu displays an image
and provides navigation menus. The help menu displays an HMTL page that tells users
how to use the application.

The wizard is the most complex part of our app. It functions as follows: The user
loads in JSON files containing details on character events and character names.
From there, the user clicks "Generate seed", and is prompted for a save location
for the seed file. This seed file is automatically loaded into the town Generator
on the right side of the screen, and the user is then prompted to input a name
for the town, population, and years of history. Once "Generate Town" is clicked,
the user selects a save location for the town file. The population and years of
history designate how many characters are to be displayed, and how many events
they should have assigned to them. For each year of history, each character has
a 1 in 4 chance of being assigned an event.

![ScreenShot](screenshots/Wizard.png)
###### Above Screenshot is the wizard screen
