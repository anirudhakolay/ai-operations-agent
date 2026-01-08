from fastapi import FastAPI
from agent.controller import run_agent

app = FastAPI(title="AI Operations Agent")

@app.post("/agent")
def agent_endpoint(task: str):
    response = run_agent(task)
    return {
        "task": task,
        "response": response
    }
