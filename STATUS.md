# Status Report
## Team
**Title:** DnD Town Generator</br>
**Team Name:** DnD Town Generator</br>
**Team Members:**</br>
<pre>Dakota Sanders</br>
Bert Bashford</br>
Matt Matto</br>
Ben Johnson</br> </pre>

## Introduction
Our application was designed from the beginning to be a town generator for the tabletop game Dungeons and Dragons. The primary usage of our application is to aid a dungeon master (DM) in creating an in-game town, full of characters and unique story events.

Obviously the main requirement for an application such as this one is the ability to display characters matched with backstories. Without this functionality our application cannot accomplish its main goal. Some secondary goals involve map generation and customizable character/event creation.

Our primary requirement over the course of this project has not been changed since its beginning. Without displaying character information, our application is of no use to the DM. Out of our secondary goals, only the customizable character/event creation feature has been implemented thus far.

The user interface of our app has gone through a series of changes, but we believe we have settled on a design that works best for the format of our application. Most of the work on this project has been done over small increments rather than major sprints, so although we followed the path of the sprints, many of our sprint goals have been accomplished ahead of time or pushed back to fit the more-realistic scope of the project.

## Customer Value
Our project has gone through some slight changes throughout its lifetime. The primary change has been the addition of a "Wizard," or a program that allows for DMs to easily add data files to the application's local storage. This change was implemented by Ben Johnson towards the end of February. The reason for this addition was primarily to assist in adding test files. By creating a wizard, our team could easily check whether the proper information would be displayed depending on what file format was submitted. 

The second major change our project went through was the abandonment of our "Main Menu" format. The reason for this change primarily sprouted from the addition of the Town Wizard. Once this feature was implemented, it made sense for our project to adopt a format that supported easy switching among tabs. Our group, especially Dakota Sanders and Matt Matto, who had developed the GUI for the main menu, decided to adopt the temporary format Ben Johnson had created when making the Wizard. This format involves adding buttons to the top of all windows within the application, allowing our users to easily switch from one content tab to another. Although this format was originally added to be a temporary format for the Wizard, our team as a whole found the new format to be nicer and easier to use, thus we abandoned our previous format and adopted the new one in early March.

## Technology

## Team
Our team contains four people, and up until the demo accompanying this status report, we have operated as two seperate subteams: one for the GUI, and one for the backend.

Our GUI team consisted of Dakota Sanders and Matt Matto. The primary goal of this team was to set up the menu and create a codebase that would allow us to easily add windows and functionality to the application. As mentioned before, the original layout for the GUI was abandoned in early March, thus repurposing this team. In the near future this team will be working on generating maps that can interact with the information our backend creates.

The other subteam was responsible for creating a backend to generate and provide town information for the GUI to present. This team consists of Ben Johnson and Bert Bashford. This team's roles evolved with the addition of the Town Wizard, and eventually the sandbox environment created by this team was adopted over the GUI created by the GUI team. Thus far this team has implemented the Wizard and functionality to display town members. This team going forward plans to clean up the data storage into a more-usable template, as well as create an interface for the GUI code to easily pull information from the local storage. This interface will also provide relevant information to our map generation code.

## Project Management

## Reflection
