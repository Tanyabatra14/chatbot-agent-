---

## 📚 System Components

### 1. *State Prompt*
Represents the conversational context at any given moment. Only *one state is active at a time*, ensuring instructional integrity and smooth user experience.

- *Goal:* Maintain context awareness and guide the user through clear, structured conversation turns.
- *Implementation:* Templates written using .jinja in state_machine/.

---

### 2. *State Transition Prompt*
Handles logic for *moving between states. Evaluates user input and system context to decide what the **next state* should be.

- *Goal:* Enable seamless progression and manage task completion logic.

---

### 3. *Knowledge Base*
Houses the core informational content the chatbot uses to respond intelligently.

- *Location:* knowledge_base/
- *Format:* JavaScript + JSON-like structure for easy querying
- *Goal:* Deliver domain-specific facts and support FAQ resolution

---

### 4. *Post-Call Configuration* (Optional / Bonus)
Performs analytics after each completed conversation to help measure system performance and customer satisfaction.

- *Location:* logging/postcall.py
- *Goal:* Provide business insights, track errors, identify pending tasks

---

### 5. *Chatbot Interface* (Optional / Bonus)
Reverse-engineered platform interface for the chatbot. Uses browser developer tools (Network tab) to mimic API interactions.

- *Goal:* Build and test the conversational agent in a real-world frontend or bot hosting platform

---

## 🚀 Getting Started

### Requirements
- Python 3.8+
- Flask or FastAPI (depending on app.py)
- Jinja2 for templating
- Node.js (if interacting with knowledge_base.js)
- Logging & analytics tools (e.g., pandas, logging, etc.)
