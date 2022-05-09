# DifferentialPrivacyDemo

[See here for details](https://github.com/LeoLiu1999/DifferentialPrivacyDemo/blob/main/Differential%20Privacy.pdf)

## Launch Instructions

### 1. Clone this repository

#### ssh:

`git@github.com:LeoLiu1999/DifferentialPrivacyDemo.git`

#### https:

`https://github.com/LeoLiu1999/DifferentialPrivacyDemo.git`

### 2. Install dependencies

`pip install -r /path/to/requirements.txt`

### 3. Generate a dataset

Within the repo, 

`python data_generator.py`

This will create `employees.csv`, which contains a mock dataset of 10,000 employees

### 4. Query the dataset

You can now use the functions in `data_processor.py` to query the dataset, with noise added in to protect the privacy of each individuals within the dataset. See `data_processor.py` for details and sample queries.