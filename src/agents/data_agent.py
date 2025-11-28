import pandas as pd
from src.utils.data_loader import load_data

class DataAgent:
    def __init__(self):
        self.df = load_data()

    def get_performance_summary(self):
        df = self.df.copy()
        df['week'] = df['date'].dt.to_period('W').dt.start_time
        weekly = df.groupby('week').agg({'spend': 'sum', 'revenue': 'sum', 'impressions': 'sum', 'clicks': 'sum'}).reset_index()
        weekly['roas'] = weekly['revenue'] / weekly['spend']
        weekly['ctr'] = weekly['clicks'] / weekly['impressions']
        weekly['week'] = weekly['week'].dt.strftime('%Y-%m-%d')
        return weekly.to_dict(orient='records')

    def get_low_performing_creatives(self):
        mean_spend = self.df['spend'].mean()
        df = self.df[self.df['spend'] > mean_spend].copy()
        threshold = df['ctr'].quantile(0.10)
        return df[df['ctr'] <= threshold][['creative_message', 'ctr', 'roas', 'creative_type']].to_dict(orient='records')

    def get_top_performing_creatives(self):
        mean_spend = self.df['spend'].mean()
        df = self.df[self.df['spend'] > mean_spend].copy()
        threshold = df['roas'].quantile(0.90)
        return df[df['roas'] >= threshold][['creative_message', 'ctr', 'roas', 'creative_type']].to_dict(orient='records')