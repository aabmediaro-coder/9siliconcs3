# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Volleyball

Description: A net sport that consists of 2 teams, playing against one other to compete for the win. The only purpose of the game is to prevent the ball from touching your team's court. If it was hit to the opponent's side of the court, a point will be awarded to your team's side, and vice versa. The game oftentimes uses 3 sets and for each sets a team need to reach 25 points, but if a deuce occurs, wherein 2 teams reached 24 points, they will play until one team reaches a 2-point gap against the other team.
## New Related Class
Class: Sport

Description: A Sport is simply a game wherein the body is trained to excessively improve how your body feel, move, and repeatedly make difficult movements. This class represents indoor and oudoor games that has strict rules needed to be followed. It sometimes has objects that are used for the game. It can be also really competitive as this helps determine who or what team is the greteast at which specific sport.
## Association
Relationship: Volleyball is under sport.

Explanation: Sports consists of all health-related and skill-related fitness that are sometimes used in volleyball. Specifically, sports 
## Multiplicity

Multiplicity:

Explanation:
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
