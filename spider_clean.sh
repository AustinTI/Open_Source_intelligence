#!/bin/bash

# Spiderfoot automation script

# Run Spiderfoot scan
spiderfoot --cli --no-geoip > spider

# Check if the spider output file exists
if [[ -f "spider" ]]; then
    # Preprocess the Spiderfoot output
    python preprocess_script.py "spider" > spider_processed

    # Check if the preprocessed file exists
    if [[ -f "spider_processed" ]]; then
        # Run the PyTorch machine learning script
        python machine_learning_script.py "spider_processed" > new_commands

        # Check if the machine learning script returned any new commands
        if [[ -s "new_commands" ]]; then
            # Append the new commands to the Spiderfoot output file
            cat new_commands >> spider

            # Run Spiderfoot scan with the updated commands
            spiderfoot --cli --no-geoip --sf-file spider --sft-file spider-results
        fi
    fi
fi
