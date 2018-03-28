# Status Report
## Team
**Title:** DnD Town Generator</br>
**Team Name:** DnD Town Generator</br>
### Team Members:</br>
Dakota Sanders</br>
Bert Bashford</br>
Matt Matto</br>
Ben Johnson</br>

## Introduction
Our application was designed from the beginning to be a town generator for the tabletop game Dungeons and Dragons. The primary usage of our application is to aid a dungeon master (DM) in creating an in-game town, full of characters and unique story events.

Obviously the main requirement for an application such as this one is the ability to display characters matched with backstories. Without this functionality our application cannot accomplish its main goal. Some secondary goals involve map generation and customizable character/event creation.

Our primary requirement over the course of this project has not been changed since its beginning. Without displaying character information, our application is of no use to the DM. Out of our secondary goals, only the customizable character/event creation feature has been implemented thus far.

The user interface of our app has gone through a series of changes, but we believe we have settled on a design that works best for the format of our application. Most of the work on this project has been done over small increments rather than major sprints, so although we followed the path of the sprints, many of our sprint goals have been accomplished ahead of time or pushed back to fit the more-realistic scope of the project.

## Customer Value
Our project has gone through some slight changes throughout its lifetime. The primary change has been the addition of a "Wizard," or a program that allows for DMs to easily add data files to the application's local storage. This change was implemented by Ben Johnson towards the end of February. The reason for this addition was primarily to assist in adding test files. By creating a wizard, our team could easily check whether the proper information would be displayed depending on what file format was submitted. 

The second major change our project went through was the abandonment of our "Main Menu" format. The reason for this change primarily sprouted from the addition of the Town Wizard. Once this feature was implemented, it made sense for our project to adopt a format that supported easy switching among tabs. Our group, especially Dakota Sanders and Matt Matto, who had developed the GUI for the main menu, decided to adopt the temporary format Ben Johnson had created when making the Wizard. This format involves adding buttons to the top of all windows within the application, allowing our users to easily switch from one content tab to another. Although this format was originally added to be a temporary format for the Wizard, our team as a whole found the new format to be nicer and easier to use, thus we abandoned our previous format and adopted the new one in early March.

## Technology
#### Architecture
The architecture of our project consists of two levels: a staging area for building towns out of individual component and a holding area for loading and manipulating towns after being built.  Individual components are JSON files that must follow a few specific rules, which are mainly naming schemes to unify the different components at build-time.  The staging area takes these multiple JSON files and builds them into a monolithic file, called a town, which can be easily shared between users.  The building process is relatively simple, provided the naming schemes are followed.  The holding area loads a town file into a class in order to easily share information between the current and future modules.  This class also handles town building.

#### Goals
Our goals were to create a function GUI and backend that handles the loading and building of town files.

### What works?
We are able to successfully load and complile a town file.  Additonally, we are able to print our town's information to the console and even some information into our GUI.

#### Testing
During development, we have extensively hand-tested each component across multiple computers and operating systems.  However, we have not implemented any official testing frameworks for this project.

### Future goals
We plan to implement randomized individuals per town to add individuality to each town.  Additionally, we intend to expand on the GUI in terms of usability, information, and features.  The team that previously worked on the GUI have shifted their focus to the generation of maps as a visual aid for each town.  The team working on the backend will continue developing an API for the GUI and map generation as well as expand upon the interface and a standard library of component files.

## Team
Our team contains four people, and up until the demo accompanying this status report, we have operated as two seperate subteams: one for the GUI, and one for the backend.

Our GUI team consisted of Dakota Sanders and Matt Matto. The primary goal of this team was to set up the menu and create a codebase that would allow us to easily add windows and functionality to the application. As mentioned before, the original layout for the GUI was abandoned in early March, thus repurposing this team. In the near future this team will be working on generating maps that can interact with the information our backend creates.

The other subteam was responsible for creating a backend to generate and provide town information for the GUI to present. This team consists of Ben Johnson and Bert Bashford. This team's roles evolved with the addition of the Town Wizard, and eventually the sandbox environment created by this team was adopted over the GUI created by the GUI team. Thus far this team has implemented the Wizard and functionality to display town members. This team going forward plans to clean up the data storage into a more-usable template, as well as create an interface for the GUI code to easily pull information from the local storage. This interface will also provide relevant information to our map generation code.

## Project Management
The project can currently display the information, which is technically our primary goal. The GUI development was set back significantly by our adoption of the new layout, but adding functionality to display the information in a visually pleasing way will only take a short amount of time to add. As far as our primary goal goes, we are on track.

Regarding the map generation, we are in a good spot to begin development without negatively impacting the other goals of our project. Because of this fact, we are slightly ahead of schedule.

## Reflection
The primary "hiccup" throughout this project has been the decision to adopt a new GUI style midway through development. While this went well as far as the transition goes, it effectively nullified a significant amount of work that was already completed. As such, we probably could have tested design ideas more at the beginning to avoid this hiccup.

What this change actually did help us understand was the structure of how we arranged our content windows. One of the benefits of switching our GUI layout was the adoption of an easier structure to change content on the screen. This new way means we don't have to spend as much time keeping track of what panels are passed to what functions.

The development of the Wizard application aspect has gone tremendously well. Our decision to use PyQt5 ended up being very beneficial because of how simple it was to utilize Python structures in our program. This meant that quickly adding functionality like the Wizard became significantly easier to do. The logic behind the code that runs the wizard is very simple to understand and add to.

In the next iteration, we will plan design choices better to avoid rewriting code. We will also focus on planning out aspects of functionality ahead of time so that all of our members are aware of the implementations we decide.
