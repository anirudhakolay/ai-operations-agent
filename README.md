# AI Operations Agent (Agentic AI)

## Overview
This project is a task-driven Agentic AI system built using FastAPI.  
The agent accepts natural language commands, determines intent, executes the appropriate tool, and returns structured JSON responses.

## Features
- Natural language task processing
- Agent-based decision routing
- Math operations as tools
- API-first architecture
- Easily extensible for LLMs and external APIs

## Example Tasks
- calculate 2 + 2
- add 5 and 4
- multiply 6 and 7
- get weather (API-based)

## Tech Stack
- Python
- FastAPI
- Uvicorn
- REST API

## How to Run
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
