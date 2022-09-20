#!/usr/bin/env python3
import openai

print("Starting Preparing Data")

openai tools fine_tunes.prepare_data -f raw/utopia.json

print("Finished Preparing Data")