#!/bin/bash

# Spiderfoot automation script

# Run Spiderfoot scan
spiderfoot --cli --no-geoip > spider

# Check if the spider output file exists
if [[ -f "spider" ]]; then
    # Parse the Spiderfoot output to generate new commands based on returns
    new_commands=$(python machine_learning_script.py "spider")

    # Check if the machine learning script returned any new commands
    if [[ -n "$new_commands" ]]; then
        # Append the new commands to the Spiderfoot output file
        echo "$new_commands" >> spider

        # Run Spiderfoot scan with the updated commands
        spiderfoot --cli --no-geoip --sf-file spider --sft-file spider-results
    fi
fi
