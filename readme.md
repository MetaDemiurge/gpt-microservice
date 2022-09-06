When cloning the repo:

virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt


To find virtualenvs run: `workon fine-tune-test`

Get token count:
python3 tokenizer.py "texttt is the new land"

Preparing dataset:
python3 

Fine tuning
python3 fine-tune.py prepared-dataset.jsonl





