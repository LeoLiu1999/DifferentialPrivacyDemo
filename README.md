# DifferentialPrivacyDemo

## Launch Instructions

### 1. Clone this repository

#### ssh:

`git clone git@github.com:tmoi29/tenaciousTurtles.git`

#### https:

`git clone https://github.com/tmoi29/tenaciousTurtles.git`

### 2. Install dependencies

`pip install -r /path/to/requirements.txt`

### 3. Generate a dataset

Within the repo, 

`python data_generator.py`

This will create `employees.csv`, which contains a mock dataset of 10,000 employees

### 4. Query the dataset

You can now use the functions in `data_processor.py` to query the dataset, with noise added in to protect the privacy of each individuals within the dataset. See `data_processor.py` for details and sample queries.