import pandas as pd

def analyze(filepath):
    df = pd.read_csv(filepath)
    df['Total'] = df.iloc[:, 2:].sum(axis=1)
    df['Percentage'] = df['Total'] / (len(df.columns) - 2)
    summary = {
        'mean': df.iloc[:, 2:-2].mean().to_dict(),
        'top_students': df.sort_values('Total', ascending=False).head(5).to_dict('records'),
        'overall_average': df['Percentage'].mean()
    }
    return summary