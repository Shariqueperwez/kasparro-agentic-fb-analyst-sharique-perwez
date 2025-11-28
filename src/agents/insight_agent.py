from openai import OpenAI
import json
import os
from src.utils.logger import log_llm_interaction
from dotenv import load_dotenv
load_dotenv()

class InsightAgent:
    def __init__(self):
        self.client = OpenAI()

    def _load_prompt(self, filename):
        with open(os.path.join("prompts", filename), "r") as f: return f.read()

    def generate_insights(self, summary_data, query):
        prompt_template = self._load_prompt("insight_prompt.md")
        final_prompt = prompt_template.replace("{data_summary}", json.dumps(summary_data, indent=2)).replace("{query}", query)
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo", messages=[{"role": "user", "content": final_prompt}], response_format={"type": "json_object"}
            )
            content = json.loads(response.choices[0].message.content)
            log_llm_interaction("InsightAgent", final_prompt, content)
            return content
        except Exception: return {"hypotheses": []}