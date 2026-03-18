import os
from google import genai
from google.adk.agents import Agent
from google.adk.models import Gemini

# 1. Setup Environment Variables (Best practice for ADK in 2026)
# This ensures the ADK knows to use Vertex AI and your specific project
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"
os.environ["GOOGLE_CLOUD_PROJECT"] = os.environ.get("GOOGLE_CLOUD_PROJECT", "vjindal-project-ai-basic")
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"

# 2. Define the Model
# We use the Gemini wrapper from ADK which internally uses the genai client
model_config = Gemini(model_id="gemini-3.1-flash")

# 3. Define the Agent
# We pass the model_config here so the Agent knows which 'brain' to use
root_agent = Agent(
    name="hello_agent",
    model=model_config,
    instruction="You are a witty AI Engineer's assistant. You help build agents."
)

# This part is for the 'adk web' command to find your agent
if __name__ == "__main__":
    from google.adk.runtime import Runtime
    runtime = Runtime(agents=[root_agent])
