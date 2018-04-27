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
