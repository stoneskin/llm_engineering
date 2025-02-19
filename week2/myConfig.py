# Standard library imports
import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv(override=True)

class Config:
    """Configuration class to hold constants and environment variables."""
    
    OPEN_ROUTER_KEY_ENV = 'Open_Router_Key'
    API_BASE_URL = "https://openrouter.ai/api/v1"
    
    # Retrieve API key from environment variables
    api_key: str = os.getenv(OPEN_ROUTER_KEY_ENV)
    if api_key and api_key.startswith('sk-or-v1') and len(api_key) > 10:
        print("API key looks good so far")
    else:
        print("There might be a problem with your API key? Please visit the troubleshooting notebook!")

class OpenAIClient:
    """Class to initialize and hold the OpenAI client."""
    
    def __init__(self, api_key: str):
        self.client = OpenAI(
            api_key=api_key,
            base_url=Config.API_BASE_URL
        )

class Models:
    """Class to hold model constants."""
    
    GEMINI2_FLASH_THINK = 'google/gemini-2.0-flash-thinking-exp:free'
    GEMINI2_PRO = 'google/gemini-2.0-pro-exp-02-05:free'
    GEMINI2_FLASH_LITE = 'google/gemini-2.0-flash-lite-preview-02-05:free'
    META_LLAMA33 = 'meta-llama/llama-3.3-70b-instruct:free'
    DEEPSEEK_V3 = 'deepseek/deepseek-chat:free'
    DEEPSEEK_R1 = 'deepseek/deepseek-r1-distill-llama-70b:free'
    QWEN_VLPLUS = 'qwen/qwen-vl-plus:free'
    OPENAI_O3MINI = 'openai/o3-mini'
    OPENAI_4O = 'openai/gpt-4o-2024-11-20'
    CLAUDE_HAIKU = 'anthropic/claude-3.5-haiku-20241022'

# Initialize OpenAI client
openai_client = OpenAIClient(api_key=Config.api_key).client