# Airline AI Agent

An intelligent AI-powered customer service agent for FlightAI airline that helps customers check flight ticket prices and allows authorized staff to update prices through a conversational interface.

## Features

- 🤖 **AI-Powered Chat Interface**: Interactive chat interface built with Gradio using OpenAI's GPT-4o-mini model
- 💰 **Ticket Price Queries**: Customers can inquire about flight ticket prices to any destination
- 🔐 **Secure Price Updates**: Authentication-protected functionality for authorized staff to update ticket prices
- 🗄️ **SQLite Database**: Persistent storage for ticket prices using SQLite
- 🔧 **Function Calling**: Leverages OpenAI's function calling capabilities for dynamic tool usage
- 💬 **Natural Language Processing**: Understands natural language queries and responds appropriately

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Jupyter Notebook or JupyterLab (for running the notebook)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LLM/AirlineAIAgent
```

2. Install required dependencies:
```bash
pip install openai python-dotenv gradio
```

3. Set up your environment variables:
   - Create a `.env` file in the project root directory
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Database Setup

The application uses a SQLite database (`prices.db`) to store ticket prices. The database should have a `prices` table with the following schema:

```sql
CREATE TABLE prices (
    city TEXT PRIMARY KEY,
    price REAL NOT NULL
);
```

The database file (`prices.db`) is automatically created when you first run the application if it doesn't exist. You can initialize it with sample data:

```python
import sqlite3

conn = sqlite3.connect('prices.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prices (
        city TEXT PRIMARY KEY,
        price REAL NOT NULL
    )
''')
cursor.execute('INSERT OR IGNORE INTO prices (city, price) VALUES (?, ?)', ('london', 699))
cursor.execute('INSERT OR IGNORE INTO prices (city, price) VALUES (?, ?)', ('tokyo', 1400))
cursor.execute('INSERT OR IGNORE INTO prices (city, price) VALUES (?, ?)', ('hyderabad', 2000))
conn.commit()
conn.close()
```

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook airline_ai_agent.ipynb
```

2. Run all cells in order (or use "Run All" from the Cell menu)

3. The Gradio interface will launch automatically in your browser

4. Start chatting with the AI agent!

## Authentication

The application includes authentication for price updates. The following users are pre-configured

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Administrator |
| manager | manager456 | Manager |
| staff | staff789 | Staff |

**Note**: For production use, you should change these default credentials and consider implementing more secure authentication methods.

## Example Queries

### Customer Queries (No Authentication Required)
- "What's the ticket price to London?"
- "How much does a ticket to Tokyo cost?"
- "I want to know the ticket price to London and Tokyo"

### Staff Queries (Authentication Required)
- "Change the London ticket price to $700"
- "Set the Tokyo ticket price to $1500"
- "Update the ticket price to Paris to $800" (with username and password)

### Complex Queries
- "Can you check the ticket price to Hyderabad and only if it is more than Tokyo's ticket price, check London ticket price"

## Project Structure

```
AirlineAIAgent/
├── airline_ai_agent.ipynb    # Main Jupyter notebook
├── prices.db                  # SQLite database for ticket prices
├── .env                        # API key details
└── README.md                  # This file
```

## How It Works

1. **User Input**: The user sends a message through the Gradio chat interface
2. **AI Processing**: The message is sent to OpenAI's GPT-4o-mini model with function definitions
3. **Function Calling**: If the model determines a function call is needed (e.g., `get_ticket_price` or `set_ticket_price`), it requests the function execution
4. **Tool Execution**: The application executes the appropriate function:
   - `get_ticket_price`: Queries the database for ticket prices
   - `set_ticket_price`: Updates ticket prices (requires authentication)
5. **Response**: The function results are sent back to the model, which generates a natural language response
6. **Output**: The final response is displayed to the user

## Technologies Used

- **OpenAI API**: GPT-4o-mini model for natural language understanding and generation
- **Gradio**: Web-based chat interface
- **SQLite**: Lightweight database for storing ticket prices
- **Python-dotenv**: Environment variable for API key management
- **Jupyter Notebook**: Interactive development environment

## Configuration

### Model Selection
The default model is `gpt-4o-mini`. You can change it by modifying the `MODEL` variable in the notebook:

```python
MODEL = "gpt-4o-mini"  # Change to "gpt-4", "gpt-3.5-turbo", etc.
```

### System Message
The AI agent's behavior is controlled by the system message. You can customize it in the notebook:

```python
system_message = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""
```

## Security Considerations

⚠️ **Important**: This is a demonstration project. For production use:

1. Change default authentication credentials
2. Implement proper password hashing (e.g., bcrypt)
3. Use environment variables for sensitive data
4. Add rate limiting to prevent abuse
6. Consider using a more secure database solution
7. Add input validation and sanitization

## Troubleshooting

### OpenAI API Key Issues
- Ensure your `.env` file is in the correct location
- Verify the API key is valid and has sufficient credits
- Check that `python-dotenv` is installed

### Database Issues
- Ensure SQLite is available (usually included with Python)
- Check file permissions for `prices.db`
- Verify the database schema matches the expected structure

### Gradio Interface Not Launching
- Try changing the port in the `launch()` function
- Ensure all dependencies are installed correctly

