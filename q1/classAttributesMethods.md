# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML](q1/classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| brand | string | private | To protect the brand information and control how it is changed |
| weight | boolean | private | To prevent the value from being changed directly outside the class |
| elasticity | boolean | public | Allows the object's elasticity information to be accessed directly |
| balls | int | public | Allows the number of balls to be accessed directly |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
