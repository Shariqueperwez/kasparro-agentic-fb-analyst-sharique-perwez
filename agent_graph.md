# Agent Architecture
1. **Planner**: Receives user query.
2. **Data Agent**: Loads CSV, aggregates metrics.
3. **Insight Agent**: Uses GPT-4 to propose hypotheses.
4. **Evaluator Agent**: Python math validation of hypotheses.
5. **Creative Agent**: Generates new copy if fatigue is detected.