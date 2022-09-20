#!/usr/bin/env python3
from dotenv import load_dotenv
import os

load_dotenv('.env')

openai.api_key=os.environ['OPENAI_API_KEY']

print("Starting Fine Tunning")

openai.prepare_data()

export "fine-tuned" openai api fine_tunes.create -t "./formatted/treaty_prepared.jsonl" -m "davinci-002" || { echo 'fine_tunes.create failed' ; exit 1; }

openai api fine_tunes.follow -i "./fine-tuned" || { echo 'fine_tunes.follow failed' ; exit 1; }


print("Finished Fine Tunning")