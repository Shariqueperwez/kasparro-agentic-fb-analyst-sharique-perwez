# kasparro-agentic-fb-analyst-sharique-perwez

# Kasparro Agentic Facebook Performance Analyst

A multi-agent AI system designed to autonomously diagnose Facebook Ads performance, identify root causes for ROAS fluctuations, and generate data-driven creative recommendations.



[Image of Multi-Agent System Architecture Diagram]


## 📋 Table of Contents
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Data Instructions](#-data-instructions)
- [Validation Mechanism](#-validation-mechanism)
- [Project Structure](#-project-structure)
- [Example Outputs](#-example-outputs)

---

## 🤖 Architecture
The system follows a **Planner-Evaluator** agentic workflow:

1.  **Planner (Orchestrator):** Decomposes the user query and coordinates agent execution.
2.  **Data Agent:** Loads raw CSV data, cleans it, and aggregates weekly performance metrics.
3.  **Insight Agent:** Uses LLMs (GPT-4/3.5) to analyze trends and propose hypotheses (e.g., "Creative Fatigue").
4.  **Evaluator Agent:** The **Validation Layer**. It uses deterministic Python math (pandas) to verify if the LLM's hypothesis is supported by raw data.
5.  **Creative Agent:** Generates new ad copy based on winning creatives if performance issues are validated.

---

## 🚀 Quick Start

### 1. Setup Environment
Clone the repository and install dependencies.
```bash
git clone [https://github.com/yourusername/kasparro-agentic-fb-analyst-sharique.git](https://github.com/yourusername/kasparro-agentic-fb-analyst-sharique.git)
cd kasparro-agentic-fb-analyst-sharique
pip install -r requirements.txt
2. Configure API Key
Create a .env file in the root directory and add your OpenAI API Key:

Plaintext

OPENAI_API_KEY=sk-your-key-here
3. Generate Data
Create the synthetic dataset required for analysis:

Bash

python setup_data.py
4. Run Analysis
Execute the main orchestration script:

Bash

python run.py "Analyze why ROAS dropped"
📊 Data Instructions
The system relies on a synthetic dataset located at data/synthetic_fb_ads_undergarments.csv.

Source: Generated via setup_data.py.

Schema: Includes campaign_name, date, spend, impressions, clicks, ctr, roas, creative_message.

Simulation: The data simulates a stable period followed by a drastic drop in CTR (Creative Fatigue) to test the agents.

✅ Validation Mechanism
A key feature of this system is the Evaluator Agent. It prevents "hallucinations" by enforcing mathematical checks:

Hypothesis: "Creative Fatigue caused ROAS drop."

Validation Logic:

Split data into "Previous Period" vs "Recent Period".

Calculate % change in CTR.

If CTR_Change < -10% AND Impressions are stable → VALIDATED.

Otherwise → REJECTED.

📂 Project Structure
Plaintext

kasparro-agentic-fb-analyst-sharique/
├── config/             # Configuration (thresholds, model settings)
├── data/               # CSV datasets
├── logs/               # JSON traces of agent execution
├── prompts/            # Prompt templates (.md)
├── reports/            # Generated outputs (Final Report)
├── src/
│   ├── agents/         # Individual agent logic
│   └── utils/          # Helper functions (logger, loader)
├── tests/              # Unit tests for evaluator
├── run.py              # Main entry point
└── requirements.txt    # Dependencies
📄 Example Outputs
1. Final Report (reports/report.md)
Markdown

# Facebook Ads Analysis Report
## Diagnosis
✅ **Creative Fatigue**: Confirmed.
- **Evidence:** CTR dropped by 70.0% while spend remained constant.

## Creative Recommendations
**Option:** Last Chance for BOGO Deal
> "Our best-selling summer styles are almost gone. Buy 1 Get 1 Free ends tonight!"
*Rationale: Uses urgency to counter fatigue.*
2. Structured Logs (logs/trace_execution.json)
JSON

{
  "agent": "InsightAgent",
  "input": "Analyze why ROAS dropped",
  "status": "success"
}
