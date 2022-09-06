#!/usr/bin/env python3
import sys
# import json
from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
prompt = sys.argv[1]

# parsed_json = (json.load(prompt))
tokens = tokenizer(prompt)['input_ids']

print(len(tokens))

cost = len(tokens) * 0.02
print("Fine-tunning cost: $" + str(cost))