import unittest
import pandas as pd
from src.agents.evaluator_agent import EvaluatorAgent

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        data = {'date': pd.to_datetime(['2025-01-01']*10), 'ctr': [0.05]*5 + [0.01]*5, 'spend': [100]*10, 'revenue': [200]*10, 'impressions': [1000]*10, 'clicks': [50]*10}
        self.df = pd.DataFrame(data)
        self.agent = EvaluatorAgent(self.df)

    def test_fatigue(self):
        is_valid, _ = self.agent.validate_hypothesis({"issue": "Creative Fatigue"})
        self.assertTrue(is_valid)

if __name__ == '__main__':
    unittest.main()