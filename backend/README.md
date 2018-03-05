# Welcome to the rear
The backend is where all the fun happens.  Here, towns get compiled together from separate elements and are sorted.

Additionally, an API is in the works to communicate with the front end of this Halloween horse costume.

## Folder Hierarchy
### ./data:
individual events and separate town information

### ./towns
Compiled towns - made up of events in ./data

## multiview.py
**Explanation terminology:** VIC - View-Inherited Class (such as TownWizard)

### MultiView
MultiView interacts with window features (such as status/menu bars) and Views

#### Functions
**addView(VIC):** adds a View class that can be switched to

**setCurrentView(VIC[, updatemenu]):** sets the current view to a View class it contains

**getCurrentView():** returns current VIC's widget

**getViewer():** returns viewer widget so you can place it wherever you want

**setmenu(VIC.getMenu()):** sets the menu (Views can call to force a menu update)

### View
View is an inherited class that holds information about a widget and its menu structure. It is used as part of a MultiView

#### Functions
**loadMenu('path/to/json'):** loads a json file representation of menu bar

**getMenu():** not user called

**getWidget():** returns the main widget of the class

**setViewLayout(layout):** sets the layout of the class's main widget
