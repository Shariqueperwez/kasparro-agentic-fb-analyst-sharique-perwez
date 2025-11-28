import pandas as pd
import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_data():
    config = load_config()
    path = config["data"]["path"]
    if path.endswith('.csv'):
        df = pd.read_csv(path)
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['spend'] = df['spend'].replace(0, 0.01)
    return df