#!/usr/bin/env python3
import sys
# import json
from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
prompt = sys.argv[1]

# parsed_json = (json.load(prompt))
tokens = tokenizer(prompt)['input_ids']

print(len(tokens))

trainingcost = 0.1200 /1000
defaultEpochs = 4
cost = len(tokens) * trainingcost * defaultEpochs 
print("Total tokens: $" + str(cost))
print("Fine-tunning cost: $" + str(cost))