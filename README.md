# DMRC Route Finder

This project is a Delhi Metro Route Finder using the Breadth-First Search (BFS) algorithm. It allows you to find the shortest path between two metro stations in Delhi and visualize the metro network. The web app is built with Flask for the backend and D3.js for graph visualization.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Git Commands to Clone This Repository](#git-commands-to-clone-this-repository)


## Project Overview
This application provides:

- **Station Search**: Select starting and destination stations.
- **Shortest Path Calculation**: Uses BFS to find the shortest route.
- **Visualization**: Displays the metro network and highlights the route.
## How It Works
Backend Setup with Flask
Flask routes handle different pages like Home, About, and Contact. The /find_path endpoint receives the selected stations and returns the shortest route calculated by the BFS function.

Graph Setup
The metro network is represented as a graph in Python, where stations are nodes, and connections are edges.

BFS Algorithm
The BFS algorithm finds the shortest path in the graph, which is then returned to the frontend for display.

Frontend Visualization
Uses HTML/CSS to design the interface.
JavaScript (D3.js) to visualize the network. The route is highlighted as users choose starting and destination stations.
## Setup Instructions
 ````

│
├── app.py               # Main Flask application
├── station_map.json     # JSON file containing station data
├── templates/           # HTML templates for rendering
│   ├── index.html
│   └── layout.html
│
├── static/              # Static files (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
└── requirements.txt     # List of dependencies

````
### Clone the Repository
Use the following command to clone the repository to your local machine:

```bash
git clone https://github.com/Amanrawat17/DMRC-BFS-.git
cd DMRC-BFS-
DMRC-BFS-/  



