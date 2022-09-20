# Data handling

## Setup
When cloning the repo:

1. Install `virtualenvwrapper` via `pip3`
Make sure to configure the directory: https://virtualenvwrapper.readthedocs.io/en/latest/install.html

2. `mkvirtualenv saivant -r requirements.txt`
3. Create an `.env` file and complete variables (check `.env.template` for reference)

To quit the project execute: 
```deactivate```

To enter the virtualenvs run: 
```workon saivant```

## Get token count:
python3 scripts/tokenizer.py "texttt is the new land"

## Preparing dataset:
1. `export OPENAI_API_KEY="<OPENAI_API_KEY>"`
2. `openai tools fine_tunes.prepare_data -f <LOCAL_FILE>`

## Fine tuning
openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>

Updating `requirements.txt`
```pip3 freeze > requirements.txt```

## Fine tuned models
Org: `org-0m3AhKLluCoRbtspwWfsMvaA`

Testing: `ft-jxwMh3oZORPKeZblV3lYl68m`


## Batching tutor's conversations

1. Check covnersation has less than 2048 tokens. If more, divide and duplicate intro
2. Use regex to clean up symbols
3. Prepare data before merging into training dataset

