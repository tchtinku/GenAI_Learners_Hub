import json

# Load the notebook
with open("/Users/macbookpro/Desktop/PowerProjects/GenAILearnersHub/beginner-projects/linkedInPostGenerator.ipynb", "r") as f:
    nb = json.load(f)

# Remove problematic widgets metadata
if "metadata" in nb:
    nb["metadata"].pop("widgets", None)  # Delete if exists

# Save the fixed notebook
with open("fixed_notebook.ipynb", "w") as f:
    json.dump(nb, f, indent=2)