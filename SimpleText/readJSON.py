import os
import json

# Define the path to the directory containing the JSON files
directory_path = 'jsons/'

# Get a list of JSON file names in the directory and sort them in alphabetical order
json_files = sorted([filename for filename in os.listdir(directory_path) if filename.endswith('.json')])

# Loop through each file in the directory
with open("baseline.txt", "w") as b:
    for filename in json_files:
        if filename.endswith('.json'): # Make sure the file is a JSON file
            filepath = os.path.join(directory_path, filename)
            topic_id = os.path.splitext(filename)[0]
            topic_id = topic_id.replace('_', '.')
            with open(filepath) as f:
                data = json.load(f)

            # Navigate to the "hits" -> "hits" level of the JSON data
            hits = data['hits']['hits']
            rank = 1
            for hit in hits:
                doc_id = hit['_id']
                score = hit['_score']
                b.write(f"{topic_id} 1 {doc_id} {rank} {score} elastic\n")
                rank += 1            