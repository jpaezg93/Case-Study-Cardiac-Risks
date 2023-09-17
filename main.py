from datasets import load_dataset
import numpy as np
import pandas as pd

def main():
    dataset = load_dataset("mstz/heart_failure")
    data = dataset["train"]
    age = np.array(data['age'])
    print(age)
    print(f'All of the patients who took part in the study had an average age of {age.mean():.2f} years')

if __name__ == '__main__':
    main()