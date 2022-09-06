

# Make sure we have a fresh .responses directory for the circuit
mkdir -p .responses

echo "Starting "

openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>

echo "Finished"