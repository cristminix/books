# Unlocking Tool Calling for Any LLM: Using MicroAgents Framework

In modern AI development, coordinating multiple language-model agents efficiently presents a significant challenge. To address this, the MicroAgents framework delivers a lightweight, flexible orchestration layer that supports universal tool calling with minimal dependencies.

## The Limitations of Existing Frameworks

Many orchestration solutions introduce unwanted complexity — and still can’t enable tool calling for a broad range of models:

- **Limited tool calling**: Frameworks like CrewAI, LangGraph, AutoGen, and LangChain cannot invoke tools on many open-source or on-prem models (e.g., Llama, DeepSeek, Phi-3, Gemma).
- **Bloated dependencies**: Popular libraries often require hundreds of megabytes of vendor and integration packages.
- **Complex setup**: Extensive boilerplate code is needed before a single agent can run.
- **Model lock-in**: Tight coupling to specific LLM providers can limit experimentation.

Although these projects offer sophisticated features, they typically span tens or hundreds of thousands of lines of code and demand dozens of megabytes of additional libraries — but still leave major LLMs unable to call functions.

## MicroAgents: A Truly Lightweight Alternative

**MicroAgents** adopts a radically minimalist design:

- **~1K LOC**, **<1 MB** installed footprint
- Only **requests** and **urllib3** as dependencies
- Direct Python-function integration — no wrapper classes
- Compatible with **any** OpenAI-style API endpoint

## Key Features That Set microAgents Apart

### Universal Tool Calling Support

The standout feature of microAgents is its universal tool calling support:

- Works with **ANY** LLM API that follows the OpenAI-compatible format
- Enables function/tool calling **even with models that don’t natively support it**
- Uses an intuitive XML-based tool calling format that’s human-readable

### Ultra-Lightweight Design

When compared to other frameworks:

- **LangGraph** — 37K LOC; +51 MB;
- **CrewAI** — 18K LOC; +173 MB;
- **AutoGen** — 7K LOC; +26 MB;
- **MicroAgents** — ~1K LOC; <1 MB;

### Simple Integration

MicroAgents emphasizes simplicity and flexibility:

- Direct function integration without wrapper classes
- Works with any LLM that follows OpenAI’s API format
- Minimal dependencies, only core HTTP libraries required

## Breaking the Tool-Calling Barrier

Because function calling has historically been restricted to top-tier hosted models, developers faced three common trade-offs:

1. **Cost**: Rely on expensive API calls.
2. **Privacy**: Deploy on-premises at the expense of feature support.
3. **Specialization**: Use domain-specific open-source LLMs without native tool-calling.

MicroAgents removes these constraints: **any** OpenAI-compatible model can invoke tools through its XML protocol. It successfully enabled tool calling across multiple LLMs that don’t natively support it like:

- **GPT-4** — native ✓; microAgents ✓; CrewAI ✓; LangGraph ✓; AutoGen ✓
- **Claude 3** — native ✓; microAgents ✓; CrewAI ✓; LangGraph ✓; AutoGen ✓
- **Llama 3** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen✗
- **Mistral** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen ✗
- **Qwen** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen ✗
- **Phi-3** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen ✗
- **Gemma** — native ✗; microAgents ✓; CrewAI ✗; LangGraph ✗; AutoGen✗

## The XML Format Advantage

When a model doesn’t natively support function calling, microAgents guides it to use a structured XML format like:

```xml
<tool>
  <name>search_database</name>
  <parameters>
    <query>quantum computing</query>
  </parameters>
</tool>
```

This XML format is:

- **Intuitive for LLMs**: Even models without specific function calling training can understand and generate this format
- **Human-readable**: Making debugging and development much easier
- **Structured and parseable**: Allowing for reliable execution regardless of the underlying model

## Quick-Start Installation

Getting started with microAgents is incredibly simple:

```bash
# Install directly from PyPI
pip install microAgents
```

Or install from source for development:

```bash
git clone https://github.com/prabhjots664/MicroAgents.git
cd MicroAgents
pip install -e .
```

## Basic Example: Creating a Math Agent

Here’s a complete example showing how to create a math agent:

```python
from microAgents.llm import LLM
from microAgents.core import MicroAgent, Tool, BaseMessageStore

# Initialize LLM with your API
llm = LLM(
    base_url="https://api.example.com/v1",  # Replace with your API endpoint
    api_key="your-api-key",
    model="your-preferred-model",
    max_tokens=4000,
    temperature=0.8,
    top_p=0.9
)
# Define tools for basic math operations
def add_numbers(a: float, b: float) -> float:
    return a + b
def multiply_numbers(a: float, b: float) -> float:
    return a * b
# Create math agent
math_agent = MicroAgent(
    llm=llm,
    prompt="You are a math assistant. Handle basic arithmetic operations.",
    toolsList=[
        Tool(description="Add two numbers", func=add_numbers),
        Tool(description="Multiply two numbers", func=multiply_numbers)
    ]
)
# Create message store for conversation history
message_store = BaseMessageStore()
# Use the agent
response = math_agent.execute_agent(
    "First add 3 and 5, then multiply the result by 2",
    message_store
)
print(response)
```

## Building a Multi-Agent System with Orchestration

Where microAgents truly shines is in its ability to create and coordinate multiple specialized agents:

```python
"""Simple end-to-end demo with math agents and orchestrator."""

from microAgents.llm import LLM
from microAgents.core import MicroAgent, Tool, BaseMessageStore

# Initialize LLM
math_llm = LLM(
    base_url="https://api.hyperbolic.xyz/v1",
    api_key="YOUR_API_KEY",
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    max_tokens=4000,
    temperature=0.8,
    top_p=0.9
)

# Define tools
def add_numbers(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

def factorial(n: int) -> int:
    """Calculates factorial of a number."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Create agents
simple_math_agent = MicroAgent(
    llm=math_llm,
    prompt="""You are a simple math assistant. Handle basic arithmetic operations.""",
    toolsList=[
        Tool(description="Adds two numbers", func=add_numbers),
        Tool(description="Multiplies two numbers", func=multiply_numbers)
    ]
)

advanced_math_agent = MicroAgent(
    llm=math_llm,
    prompt="""You are an advanced math assistant. Handle complex math operations.""",
    toolsList=[
        Tool(description="Calculates factorial", func=factorial)
    ]
)

class Orchestrator(MicroAgent):
    def __init__(self):
        super().__init__(
            llm=math_llm,
            prompt="""You are a math query analyzer. For each query:
1. If it contains basic arithmetic (addition, subtraction, multiplication, division), output exactly: SIMPLE_MATHS NEEDED
2. If it contains advanced math (factorials, exponents, logarithms, derivatives, integrals), output exactly: ADVANCED_MATHS NEEDED
3. If unsure, output exactly: UNKNOWN_MATH_TYPE

Examples:
- "What is 5 plus 3?" → SIMPLE_MATHS NEEDED
- "Calculate 10 factorial" → ADVANCED_MATHS NEEDED
- "Solve x^2 + 2x + 1 = 0" → UNKNOWN_MATH_TYPE

Always output exactly one of these three options, nothing else.""",
            toolsList=[]
        )
        self.simple_math_agent = simple_math_agent
        self.advanced_math_agent = advanced_math_agent

    def execute_agent(self, query: str, message_store: BaseMessageStore) -> str:
        """Handle full query flow through orchestrator."""
        print(f"\nDebug: Orchestrator analyzing query: {query}")
        
        # Get initial analysis from orchestrator
        analysis = super().execute_agent(query, message_store)
        print(f"Debug: Orchestrator analysis result: {analysis}")
        
        if "SIMPLE_MATHS NEEDED" in analysis:
            print("Debug: Routing to Simple Math Agent")
            result = self.simple_math_agent.execute_agent(query, message_store)
            print(f"Debug: Simple Math Agent result: {result}")
            return self._format_result("Simple Math Agent", result)
        elif "ADVANCED_MATHS NEEDED" in analysis:
            print("Debug: Routing to Advanced Math Agent")
            result = self.advanced_math_agent.execute_agent(query, message_store)
            print(f"Debug: Advanced Math Agent result: {result}")
            return self._format_result("Advanced Math Agent", result)
        else:
            return "Orchestrator: Unable to determine the appropriate agent for this query."

    def _format_result(self, agent_name: str, result: str) -> str:
        """Format the final result from an agent."""
        return f"Orchestrator: Result from {agent_name}:\n{result}"

def main():
    message_store = BaseMessageStore()
    orchestrator = Orchestrator()
    
    # Example queries that demonstrate XML-style tool calls
    queries = [
        "What is 15 plus 27?",
        "Calculate 5 factorial",
        "Multiply 8 by 9",
        "First add 3 and 5, then multiply the result by 2"
    ]
    
    for query in queries:
        print(f"\nUser: {query}")
        response = orchestrator.execute_agent(query, message_store)
        print(f"{response}")

if __name__ == "__main__":
    main()
```

## Practical Example: Database Assistant with Llama 3

Here’s an example showing how microAgents enables tool calling with Llama 3, which doesn’t natively support function calling:

```python
from microAgents.llm import LLM
from microAgents.core import MicroAgent, Tool, BaseMessageStore

# Initialize with Llama 3 (which doesn't natively support function calling)
llm = LLM(
    base_url="https://api.together.xyz/v1",
    api_key="your-api-key",
    model="meta-llama/Llama-3-8b-instruct",
    max_tokens=2000
)
# Define database tools
def query_database(table: str, filter_condition: str = None) -> list:
    # Simulated database query
    if table == "customers":
        return ["Customer1", "Customer2", "Customer3"]
    return ["No data found"]
def insert_record(table: str, data: dict) -> str:
    # Simulated insert operation
    return f"Record inserted into {table}"
# Create database agent
db_agent = MicroAgent(
    llm=llm,  # Llama 3 doesn't have native function calling!
    prompt="You are a database assistant. Help users interact with databases.",
    toolsList=[
        Tool(description="Query database table with optional filter", func=query_database),
        Tool(description="Insert record into database table", func=insert_record)
    ]
)
# Execute query - with full tool calling support!
result = db_agent.execute_agent("Show me all customers in the database", BaseMessageStore())
print(result)
```

## Real-World Use Cases

- **Prototyping**: Rapid multi-agent proofs of concept
- **Production**: Lightweight deployment in microservices
- **Edge/IoT**: Operate within resource constraints
- **Custom LLMs**: Any OpenAI-compatible API endpoint

## The Road Ahead

As an open-source project, MicroAgents welcomes contributions to:

- Expand its tool ecosystem
- Provide more templates and examples
- Enhance orchestration (streaming, async)
- Easy No Code Low Code UI for building multi-agent systems.