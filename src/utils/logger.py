import json
import os
from datetime import datetime

def log_llm_interaction(agent_name, input_data, output_data):
    """Saves LLM traces to logs/ directory for evidence."""
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"logs/{timestamp}_{agent_name}.json"
    
    log_entry = {
        "timestamp": timestamp,
        "agent": agent_name,
        "input": input_data,
        "output": output_data
    }
    
    with open(filename, "w") as f:
        json.dump(log_entry, f, indent=2)