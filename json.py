import json
import sys

def load_payload():
    """
    Safely reads and decodes standard input data streams for JSON parsing.
    """
    try:
        content = sys.stdin.read()
        if not content.strip():
            return {"status": "empty"}
        return json.loads(content)
    except json.JSONDecodeError:
        return {"status": "invalid_json"}

if __name__ == "__main__":
    # Test utility loop
    data = load_payload()
    print(json.dumps({"processed": True, "input_received": data}))
