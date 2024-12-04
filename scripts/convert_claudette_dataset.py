import csv
import json

# Define the input TSV file and the output JSON file
input_tsv_file = '../data/CLAUDETTE/claudette_train_merged.tsv'
output_json_file = '../data/CLAUDETTE/test_all.json'

# Initialize the list to hold the converted data
converted_data = []

# Read the TSV file
with open(input_tsv_file, 'r', encoding='utf-8') as tsvfile:
    tsv_reader = csv.DictReader(tsvfile, delimiter='\t')

    for row in tsv_reader:
        # Construct the "problem" field with the specified format
        problem = (
            "You are an expert in identifying potentially unfair clauses in terms of service documents. "
            "Answer 'Yes' or 'No' only. Is the following sentence a potentially unfair clause? '{text}'"
        ).format(text=row['text'])

        # Convert the "label" field to "solution"
        solution = "Yes" if row['label'] == '1' else "No"

        # Append the converted row to the list
        converted_data.append({
            "id": int(row['id']),
            "problem": problem,
            "solution": solution
        })

# Write the converted data to the JSON file
with open(output_json_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(converted_data, jsonfile, ensure_ascii=False, indent=4)

print(f"Converted data has been written to {output_json_file}")
