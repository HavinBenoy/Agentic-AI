AI Python Function Generator — Quasi Agent

An AI-powered quasi-agent that generates Python functions based on user requirements and returns a well-documented implementation along with corresponding unittest test cases.

The project demonstrates the core workflow of an AI agent without implementing an autonomous execution loop. The sequence of actions is explicitly defined and executed step by step.

Overview

The quasi-agent accepts a user's programming requirement and uses a language model to:

Generate an appropriate prompt.
Send the prompt to the language model.
Parse the model's response to extract the required result.
Use the parsed result for subsequent processing.
Convert the final result into a user-readable string.

The generated output contains:

A Python function implementing the requested functionality.
Documentation explaining the function.
unittest test cases for validating the implementation.
Agent Workflow
User Request
     │
     ▼
Prompt Generation
     │
     ▼
Language Model
     │
     ▼
Model Response
     │
     ▼
Response Parsing
     │
     ▼
Extract Required Result
     │
     ▼
Further Processing
     │
     ▼
String Conversion
     │
     ▼
Final Response

Unlike a fully autonomous agent, the workflow is predefined rather than dynamically planned.

Why "Quasi-Agent"?

This project implements several fundamental concepts found in AI agents:

Prompt construction
Interaction with an LLM
Context management
Response parsing
Using intermediate results for subsequent operations
Structured output generation

However, the system does not continuously reason, re-plan, or decide its next action autonomously.

The execution flow is explicitly defined in advance:

Step 1 → Step 2 → Step 3 → Step 4 → Step 5

rather than:

Observe → Reason → Act → Observe → Re-plan → Act → ...

Therefore, the project is referred to as a quasi-agent rather than a fully autonomous AI agent.

ChatML Message Format

The project uses the ChatML-style role structure to organize instructions and conversational context passed to the language model.

System Role

The system role defines the general behavior, rules, and constraints that the model should follow.

Example:

system:
You are a Python programming assistant.
Generate clean, well-documented Python functions
and corresponding unittest test cases.
User Role

The user role specifies the current task that needs to be performed.

Example:

user:
Create a Python function to determine whether a number is prime.
Assistant Role

The assistant role represents the model's previous response.

It can be injected into subsequent prompts to preserve conversational context and allow later model calls to take previous generated information into account.

Example:

assistant:
Here is the generated prime-checking function...

This role-based structure helps separate:

General instructions
Current user requirements
Previous model-generated context