import pandas as pd

def few_shot_format(row):
    """
    Create formatted string for a single few-shot example.
    """
    output_format = f"""---
    Abstract: {row['Abstract']},
    Title: {row['Title']} \n"""

    return output_format

# Create few shot examples
def create_few_shot_examples(df, n=2):
    """
    Randomly sample n examples from the dataset.
    """

    sampled_dfs = []
    for sample in range(n):
        sampled = df.sample(n=n, replace=True, random_state=42)
        sampled_dfs.append(sampled)

    # Concatenate the sampled DataFrames
    sampled_df = pd.concat(sampled_dfs).reset_index(drop=True)
    return sampled_df