import json

input_file = "data/HealthCareMagic-100k.json"
output_file = "data/HealthCareMagic-100k.jsonl"

with open(input_file, "r") as f:
    data = json.load(f)

with open(output_file, "w") as f:
    for item in data:
        json.dump(item, f)
        f.write("\n")

print(f"✅ Converted {len(data)} records to JSONL format.")
