from datasets import load_dataset
import numpy as np
import pandas as pd

def main():
    dataset = load_dataset("mstz/heart_failure", split="train")
    df = pd.DataFrame(dataset)
    #print(df.columns)
    deceased = df[df['is_dead']==1]
    survived = df[df['is_dead']==0]
    print(f'Participants who passed away throughout the study on average were {deceased["age"].mean():.2f} years old')
    print(f"Participants who were alive during the study's duration had an average age of {survived['age'].mean():.2f}")
if __name__ == '__main__':
    main()