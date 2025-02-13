#!/usr/bin/env python
import sys
import warnings
import yaml
import os

# Ensure the 'src' directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from resume_crew.crew import ResumeCrew  # Import after fixing path

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def load_inputs():
    """ Load job URL and resume type from input.yaml """
    input_file = os.path.join(os.path.dirname(__file__), "config", "input.yaml")
    print(f"DEBUG: Loading input.yaml from {input_file}")  # Debugging log
    try:
        with open(input_file, "r") as file:
            data = yaml.safe_load(file) or {}  # Ensure it returns a dictionary
            print(f"DEBUG: Loaded data: {data}")  # Debugging log
            return data
    except Exception as e:
        print(f"Error loading input.yaml: {e}")
        sys.exit(1)


def run():
    """ Run the resume optimization crew with job URL and resume type """
    inputs = load_inputs()

    if not inputs.get("job_url") or not inputs.get("resume_type"):
        print("Error: Missing 'job_url' or 'resume_type' in input.yaml")
        sys.exit(1)

    print(f"Running with inputs: {inputs}")  # Debugging log
    ResumeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
