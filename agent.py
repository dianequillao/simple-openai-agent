import openai
from arize.otel import register
from dotenv import load_dotenv
from openinference.instrumentation.openai import OpenAIInstrumentor

load_dotenv()  # must run before openai.OpenAI()


#Set up the client to read 
client = openai.OpenAI()


response = client.responses.create(
    model='gpt-5.6-luna',
    input="What's my horoscope today? I'm a Leo",
    tools=[{"type": "web_search"}]
)

print(response.output_text)


tracer_provider = register(
    space_id=os.environ["ARIZE_SPACE_ID"],
    api_key=os.environ["ARIZE_API_KEY"],
    project_name="simple-project",
)
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)
