#!/bin/bash

echo "Starting Ollama Service..."

# Start Ollama in the background.
echo "Starting Ollama server..."
/bin/ollama serve &

# Record the Process ID.
pid=$!

# Allow the server to initialize properly.
echo "Waiting for Ollama to initialize..."
sleep 5

# Pull the llama3.2 model.
echo "🔴 Retrieving LLAMA3.2 model..."
/bin/ollama pull llama3.2
echo "🟢 Model retrieval complete!"

# Wait for the Ollama process to finish.
wait $pid

