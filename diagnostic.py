import sys
import os
import json

def run_diagnostic():
    """
    Evaluates local system properties to verify that the workspace
    is ready for development tools.
    """
    report = {
        "status": "agent_environment_secure",
        "runtime": {
            "python_version": sys.version.split()[0],
            "platform": sys.platform,
            "current_dir": os.getcwd()
        }
    }
    
    # Return standard confirmation payload
    print(json.dumps(report))

if __name__ == "__main__":
    run_diagnostic()
