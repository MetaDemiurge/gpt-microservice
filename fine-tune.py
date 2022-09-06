#!/usr/bin/env python3

OPENAI_API_KEY = "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"

print("Starting Fine Tunning")

export "fine-tuned" openai api fine_tunes.create -t "./fine-tune.sh" -m "davinci-002" || { echo 'fine_tunes.create failed' ; exit 1; }

openai api fine_tunes.follow -i "./fine-tuned-ooaoa" || { echo 'fine_tunes.follow failed' ; exit 1; }


print("Finished Fine Tunning")