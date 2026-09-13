# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML](classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| brand | string | public | Identifies the ball's brand and can be accessed normally |
| weight | boolean | public | Indicates whether the ball is heavy or not |
| elasticity | boolean | private | Protects the ball's elasticity information from direct changes |
| balls | int | private | Prevents the number of balls from being changed to an invalid value |
## Updated UML Class Diagram
![Class Diagram](images/Screenshot_20260914-061708_1.png)
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
