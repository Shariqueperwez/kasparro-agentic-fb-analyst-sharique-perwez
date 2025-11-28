import pandas as pd

class EvaluatorAgent:
    def __init__(self, df):
        self.df = df

    def validate_hypothesis(self, hypothesis):
        issue = hypothesis['issue'].lower()
        if "fatigue" in issue or "ctr" in issue:
            return self._check_creative_fatigue()
        return False, "No quantitative test available."

    def _check_creative_fatigue(self):
        recent = self.df.sort_values('date')
        mid = len(recent) // 2
        first, second = recent.iloc[:mid], recent.iloc[mid:]
        ctr_change = (second['ctr'].mean() - first['ctr'].mean()) / first['ctr'].mean()
        if ctr_change < -0.05: return True, f"Validated: CTR dropped {ctr_change:.1%}."
        return False, f"Rejected: CTR change {ctr_change:.1%} not significant."