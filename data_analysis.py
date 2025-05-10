import pandas as pd
from datetime import datetime

def process_contributors(data: list) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df = df[['login', 'contributions']]
    return df.sort_values('contributions', ascending=False)

def process_commits(data: list) -> pd.DataFrame:
    # Extrae autor y fecha
    records = []
    for c in data:
        author = c.get('commit', {}).get('author', {}).get('name')
        date = c.get('commit', {}).get('author', {}).get('date')
        date = datetime.fromisoformat(date.replace('Z', '+00:00'))
        records.append({"author": author, "date": date})
    df = pd.DataFrame(records)
    df['day'] = df['date'].dt.date
    summary = df.groupby('day').size().reset_index(name='commits')
    return summary
