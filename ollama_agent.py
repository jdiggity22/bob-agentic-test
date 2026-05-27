"""
Simple LangChain Agent that connects to local Ollama
This script demonstrates how to create a basic conversational agent using LangChain and Ollama.
"""

import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load environment variables
load_dotenv()

class OllamaAgent:
    """A simple agent that uses Ollama via LangChain"""
    
    def __init__(self, model_name="llama3.2", temperature=0.7, base_url="http://localhost:11434"):
        """
        Initialize the Ollama agent
        
        Args:
            model_name: The Ollama model to use (e.g., llama3.2, mistral, codellama)
            temperature: Controls randomness in responses (0-1)
            base_url: The Ollama server URL (default: http://localhost:11434)
        """
        # Get configuration from environment (with defaults)
        model_name = os.getenv("OLLAMA_MODEL", model_name)
        base_url = os.getenv("OLLAMA_BASE_URL", base_url)
        
        # Initialize Ollama LLM
        self.llm = ChatOllama(
            model=model_name,
            temperature=temperature,
            base_url=base_url,
        )
        
        # Store conversation history
        self.conversation_history = []
        
        print(f"✓ Ollama Agent initialized with model: {model_name}")
        print(f"✓ Connecting to Ollama at: {base_url}")
    
    def chat(self, message):
        """
        Send a message to Ollama and get a response
        
        Args:
            message: The user's message
            
        Returns:
            Ollama's response
        """
        try:
            # Add user message to history
            self.conversation_history.append(HumanMessage(content=message))
            
            # Get response from Ollama
            response = self.llm.invoke(self.conversation_history)
            
            # Add AI response to history
            self.conversation_history.append(AIMessage(content=response.content))
            
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_conversation(self):
        """Clear the conversation history"""
        self.conversation_history = []
        print("✓ Conversation history cleared")


def main():
    """Main function to run the interactive agent"""
    print("=" * 60)
    print("Ollama Agent - Powered by LangChain")
    print("=" * 60)
    print("\nCommands:")
    print("  - Type your message to chat with Ollama")
    print("  - Type 'reset' to clear conversation history")
    print("  - Type 'quit' or 'exit' to end the session")
    print("=" * 60)
    
    try:
        # Initialize the agent
        agent = OllamaAgent()
        
        # Interactive loop
        while True:
            print("\n" + "-" * 60)
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit']:
                print("\nGoodbye! 👋")
                break
            
            if user_input.lower() == 'reset':
                agent.reset_conversation()
                continue
            
            # Get response from Ollama
            print("\nOllama: ", end="", flush=True)
            response = agent.chat(user_input)
            print(response)
    
    except KeyboardInterrupt:
        print("\n\nSession interrupted. Goodbye! 👋")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure you have:")
        print("1. Ollama installed and running (ollama serve)")
        print("2. A model pulled (e.g., ollama pull llama3.2)")
        print("3. Installed all requirements: pip3 install -r requirements.txt")


if __name__ == "__main__":
    main()

# Made with Bob