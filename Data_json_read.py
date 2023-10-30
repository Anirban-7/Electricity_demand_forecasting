import json

# Read JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Store unique respondent names
unique_respondents = set()

# Extract unique respondents
for entry in data:
    respondent_name = entry.get("respondent-name")
    if respondent_name:
        unique_respondents.add(respondent_name)

# Print unique respondent names
for respondent in unique_respondents:
    print(respondent)


