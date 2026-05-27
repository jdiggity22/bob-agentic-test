# Ollama Agent with LangChain

A simple conversational agent that connects to local Ollama using LangChain.

## Features

- 🤖 Interactive chat with local Ollama models
- 💬 Conversation memory to maintain context
- 🔄 Easy conversation reset
- 🎯 Simple and clean implementation
- 🔐 Optional configuration with environment variables
- 🚀 No API keys required - runs completely locally!

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally ([ollama.com](https://ollama.com))

## Installation

### 1. Install Ollama

First, install Ollama on your system:

**macOS/Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from [ollama.com/download](https://ollama.com/download)

### 2. Pull a Model

Pull a model to use (e.g., llama3.2):
```bash
ollama pull llama3.2
```

Other popular models:
- `ollama pull mistral` - Mistral 7B
- `ollama pull codellama` - Code Llama for programming
- `ollama pull phi3` - Microsoft Phi-3
- `ollama pull gemma2` - Google Gemma 2

### 3. Start Ollama Server

Start the Ollama server (if not already running):
```bash
ollama serve
```

### 4. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

### 5. (Optional) Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` to customize (optional - defaults will be used):
```
OLLAMA_MODEL=llama3.2
OLLAMA_BASE_URL=http://localhost:11434
```

## Usage

### Running the Interactive Agent

Simply run the main script:

```bash
python3 ollama_agent.py
```

### Commands

Once the agent is running, you can use these commands:

- **Chat**: Just type your message and press Enter
- **Reset conversation**: Type `reset` to clear the conversation history
- **Exit**: Type `quit` or `exit` to end the session

### Example Session

```
============================================================
Ollama Agent - Powered by LangChain
============================================================

Commands:
  - Type your message to chat with Ollama
  - Type 'reset' to clear conversation history
  - Type 'quit' or 'exit' to end the session
============================================================
✓ Ollama Agent initialized with model: llama3.2
✓ Connecting to Ollama at: http://localhost:11434

------------------------------------------------------------

You: Hello! Can you help me understand what you can do?

Ollama: Hello! I'm an AI assistant running locally on your machine...

------------------------------------------------------------

You: reset
✓ Conversation history cleared

------------------------------------------------------------

You: quit
Goodbye! 👋
```

## Using the Agent in Your Own Code

You can also import and use the `OllamaAgent` class in your own Python scripts:

```python
from ollama_agent import OllamaAgent

# Initialize the agent
agent = OllamaAgent(
    model_name="llama3.2",
    temperature=0.7,
    base_url="http://localhost:11434"
)

# Chat with Ollama
response = agent.chat("What is the capital of France?")
print(response)

# Reset conversation if needed
agent.reset_conversation()
```

## Configuration

You can customize the agent by modifying these parameters when initializing:

- **model_name**: Choose different Ollama models
  - `llama3.2` (default, balanced)
  - `mistral` (fast and capable)
  - `codellama` (optimized for code)
  - `phi3` (efficient, smaller model)
  - `gemma2` (Google's model)

- **temperature**: Control response randomness (0.0 to 1.0)
  - Lower values (0.0-0.3): More focused and deterministic
  - Medium values (0.4-0.7): Balanced (default: 0.7)
  - Higher values (0.8-1.0): More creative and varied

- **base_url**: Ollama server URL (default: `http://localhost:11434`)

## Project Structure

```
.
├── ollama_agent.py      # Main agent implementation
├── claude_agent.py      # Original Claude implementation (kept for reference)
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment file
├── .env               # Your configuration (optional)
└── README.md          # This file
```

## Troubleshooting

### Ollama Not Running

If you get connection errors:
```bash
# Start Ollama server
ollama serve
```

### Model Not Found

If you get "model not found" errors:
```bash
# Pull the model first
ollama pull llama3.2
```

### Import Errors

If you see import errors, make sure you've installed all dependencies:
```bash
pip3 install -r requirements.txt
```

### Slow Responses

If responses are slow:
- Use a smaller model (e.g., `phi3` instead of `llama3.2`)
- Ensure Ollama is using GPU acceleration if available
- Check system resources (RAM, CPU usage)

## Available Models

List all available models on your system:
```bash
ollama list
```

Search for more models:
```bash
ollama search <model-name>
```

## Dependencies

- **langchain**: LLM application framework
- **langchain-ollama**: LangChain integration for Ollama
- **langchain-core**: Core LangChain functionality
- **python-dotenv**: Environment variable management

## Advantages of Using Ollama

✅ **Privacy**: All data stays on your machine  
✅ **No API Costs**: Completely free to use  
✅ **Offline Capable**: Works without internet  
✅ **Fast**: No network latency  
✅ **Customizable**: Use any Ollama-compatible model  

## License

See LICENSE file for details.

## Contributing

Feel free to submit issues or pull requests to improve this agent!

## Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Ollama Models Library](https://ollama.com/library)
- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Ollama Integration](https://python.langchain.com/docs/integrations/chat/ollama)

---

**Note**: This is a simple example implementation. For production use, consider adding:
- Error handling and retry logic
- Logging
- Streaming responses
- More sophisticated memory management
- Model performance monitoring