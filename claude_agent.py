"""
Simple Langflow Agent that connects to Claude API
This script demonstrates how to create a basic conversational agent using Langflow and Claude.
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables
load_dotenv()

class ClaudeAgent:
    """A simple agent that uses Claude via Langflow/LangChain"""
    
    def __init__(self, model_name="claude-3-5-sonnet-20241022", temperature=0.7):
        """
        Initialize the Claude agent
        
        Args:
            model_name: The Claude model to use
            temperature: Controls randomness in responses (0-1)
        """
        # Get API key from environment
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        # Initialize Claude LLM
        self.llm = ChatAnthropic(
            model=model_name,
            temperature=temperature,
            anthropic_api_key=api_key,
            max_tokens=1024
        )
        
        # Set up conversation memory
        self.memory = ConversationBufferMemory(
            return_messages=True,
            memory_key="history"
        )
        
        # Create conversation chain
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=True
        )
        
        print(f"✓ Claude Agent initialized with model: {model_name}")
    
    def chat(self, message):
        """
        Send a message to Claude and get a response
        
        Args:
            message: The user's message
            
        Returns:
            Claude's response
        """
        try:
            response = self.conversation.predict(input=message)
            return response
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_conversation(self):
        """Clear the conversation history"""
        self.memory.clear()
        print("✓ Conversation history cleared")


def main():
    """Main function to run the interactive agent"""
    print("=" * 60)
    print("Claude Agent - Powered by Langflow")
    print("=" * 60)
    print("\nCommands:")
    print("  - Type your message to chat with Claude")
    print("  - Type 'reset' to clear conversation history")
    print("  - Type 'quit' or 'exit' to end the session")
    print("=" * 60)
    
    try:
        # Initialize the agent
        agent = ClaudeAgent()
        
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
            
            # Get response from Claude
            print("\nClaude: ", end="", flush=True)
            response = agent.chat(user_input)
            print(response)
    
    except KeyboardInterrupt:
        print("\n\nSession interrupted. Goodbye! 👋")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure you have:")
        print("1. Created a .env file with your ANTHROPIC_API_KEY")
        print("2. Installed all requirements: pip install -r requirements.txt")


if __name__ == "__main__":
    main()

# Made with Bob
