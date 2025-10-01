## Setup

- Tree-Based Structure:  
  Each node represents a question or answer. Leaf nodes provide advice; intermediate nodes guide the diagnostic flow.

- Recursive Traversal:  
  Keeps code clean and readable.

- Guidance Before Questions:  
  Users are instructed to run a certain Linux command before answering. This makes the bot both educational and actionable.

- Interactive Yes/No Prompts:  
  Validates input to accept only Y/N (case-insensitive). Ensures predictable flow through the troubleshooting tree.  If the user inputs
  anything other than a Y/y or N/n then the question is asked again.

## Approach

- Node-Based Design:  
  Each node contains either a question with possible answers or a final piece of advice.

- Recursive Traversal:  
  The chatbot starts at the root node and keeps asking questions until it reaches an answer node. If the user enters something invalid, it asks again.

## Chatbot in action

![Decision Tree](chatbot_in_action.png)
