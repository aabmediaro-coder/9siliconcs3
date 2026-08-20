# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Ally
**Section:** Silicon
**Last Name:** Mediario
**Date:** August 20, 2026
---

## Step 1: Identify the Big Problem
### Main Problem
The school canteen's ordering and payment process is slow and inefficient, causing long queues and making it difficult to manage food inventory.
---
## Step 2: Identify the Sub-Problems
1. The canteen queue becomes too long during lunch break.
2. Students often take a long time deciding what food to order.
3. The cashier has difficulty calculating the total and change manually.
4. The canteen does not know which food items are running low or sold out.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| The canteen queue becomes too long during lunch break | Decomposition | Divide the queue process into smaller tasks such as making new queues, then adding students, serving the next student, and removing served students |
| Students often take a long time deciding what food to order | Pattern Recognition | Identify frequently ordered food items and common ordering patterns to help students decide faster |
| The cashier has difficulty calculating the total and change manually | Abstraction | Focus only on important information such as food items, quantities, prices, and the amount paid for the food |
| The canteen does not know which food items are running low or sold out | Algorithm Design | Create steps that automatically update food quantities after each purchase and notify the cashier when stock is low |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
The cashier has difficulty calculating the total and change manually
### Pseudocode
START

Display available food choices
Ask user to select a food item
Get price of food item

Ask user to enter food quantity
Get food quantity

Calculate total = price x quantity

Ask user to enter amount paid
Get amount paid

Calculate change = amount paid - total

Display total
Display change

END
---