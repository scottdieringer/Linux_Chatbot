# Linux Performance Troubleshooting Chatbot

## 1. Design Choices

- **Tree-Based Structure**:  
  The chatbot uses a tree data structure (`Node`) to represent the decision flow. Each node contains either a **question** or an **answer**.  
  - Leaf nodes provide advice.  
  - Intermediate nodes guide the user through diagnostic steps.  
  This design makes the chatbot **extensible**, allowing new troubleshooting branches to be added easily.

- **Recursion for Traversal**:  
  The chatbot uses a recursive function `traverse()` to navigate through the tree.  
  This keeps the code clean and avoids deeply nested `if`/`elif` statements.

- **Guidance Before Questions**:  
  Users are instructed on what command to run (e.g., `top` or `htop`) before asking a yes/no question.  
  This makes the bot **educational**, teaching the user how to check system performance interactively.

- **Interactive Yes/No Prompts**:  
  Input is validated to accept only `"y"` or `"n"` responses. Incorrect input triggers a prompt to try again.  
  This ensures robust and predictable flow through the troubleshooting tree.

---

## 2. Technical Implementation

- **Node Class**:  
  ```python
  class Node:
      def __init__(self, question=None, answer=None):
          self.question = question
          self.answer = answer
          self.children = {}
