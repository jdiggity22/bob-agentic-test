# Claude Agent with Langflow

A simple conversational agent that connects to Claude AI using Langflow/LangChain.

## Features

- 🤖 Interactive chat with Claude AI
- 💬 Conversation memory to maintain context
- 🔄 Easy conversation reset
- 🎯 Simple and clean implementation
- 🔐 Secure API key management with environment variables

## Prerequisites

- Python 3.8 or higher
- Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com/))

## Installation

1. **Clone or navigate to this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_actual_api_key_here
   ```

## Usage

### Running the Interactive Agent

Simply run the main script:

```bash
python claude_agent.py
```

### Commands

Once the agent is running, you can use these commands:

- **Chat**: Just type your message and press Enter
- **Reset conversation**: Type `reset` to clear the conversation history
- **Exit**: Type `quit` or `exit` to end the session

### Example Session

```
============================================================
Claude Agent - Powered by Langflow
============================================================

Commands:
  - Type your message to chat with Claude
  - Type 'reset' to clear conversation history
  - Type 'quit' or 'exit' to end the session
============================================================
✓ Claude Agent initialized with model: claude-3-5-sonnet-20241022

------------------------------------------------------------

You: Hello! Can you help me understand what you can do?

Claude: Hello! I'm Claude, an AI assistant. I can help you with a wide variety of tasks...

------------------------------------------------------------

You: reset
✓ Conversation history cleared

------------------------------------------------------------

You: quit
Goodbye! 👋
```

## Using the Agent in Your Own Code

You can also import and use the `ClaudeAgent` class in your own Python scripts:

```python
from claude_agent import ClaudeAgent

# Initialize the agent
agent = ClaudeAgent(
    model_name="claude-3-5-sonnet-20241022",
    temperature=0.7
)

# Chat with Claude
response = agent.chat("What is the capital of France?")
print(response)

# Reset conversation if needed
agent.reset_conversation()
```

## Configuration

You can customize the agent by modifying these parameters when initializing:

- **model_name**: Choose different Claude models
  - `claude-3-5-sonnet-20241022` (default, balanced)
  - `claude-3-opus-20240229` (most capable)
  - `claude-3-haiku-20240307` (fastest)

- **temperature**: Control response randomness (0.0 to 1.0)
  - Lower values (0.0-0.3): More focused and deterministic
  - Medium values (0.4-0.7): Balanced (default: 0.7)
  - Higher values (0.8-1.0): More creative and varied

## Project Structure

```
.
├── claude_agent.py      # Main agent implementation
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment file
├── .env               # Your actual API key (not in git)
└── README.md          # This file
```

## Troubleshooting

### Import Errors

If you see import errors, make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### API Key Issues

If you get authentication errors:
1. Verify your API key is correct in the `.env` file
2. Make sure the `.env` file is in the same directory as `claude_agent.py`
3. Check that your API key is active at [console.anthropic.com](https://console.anthropic.com/)

### Rate Limits

If you hit rate limits, consider:
- Adding delays between requests
- Using a lower-tier model (e.g., Haiku instead of Sonnet)
- Upgrading your Anthropic API plan

## Dependencies

- **langflow**: Framework for building LLM applications
- **anthropic**: Official Anthropic Python SDK
- **langchain**: LLM application framework
- **langchain-anthropic**: LangChain integration for Anthropic models
- **python-dotenv**: Environment variable management

## License

See LICENSE file for details.

## Contributing

Feel free to submit issues or pull requests to improve this agent!

## Resources

- [Anthropic Documentation](https://docs.anthropic.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [Langflow Documentation](https://docs.langflow.org/)

---

**Note**: This is a simple example implementation. For production use, consider adding:
- Error handling and retry logic
- Logging
- Token usage tracking
- Streaming responses
- More sophisticated memory management