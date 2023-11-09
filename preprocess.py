import os
import re
import argparse
import json

parser = argparse.ArgumentParser(description='Preprocess transcript files.')
parser.add_argument('--input_folder', type=str, help='path to the input folder')
args = parser.parse_args()

# Set the path to the directory containing the transcript files
directory_path = args.input_folder

# Create an empty list to store the contents of each transcript file
transcript_contents = []

# Loop through each subdirectory in the directory
for subdir in os.listdir(directory_path): 
    subdir_path_one = os.path.join(directory_path, subdir) 
    if os.path.isdir(subdir_path_one):
        for subdir in os.listdir(subdir_path_one): 
            subdir_path = os.path.join(subdir_path_one, subdir) 
            if os.path.isdir(subdir_path): 
                # Loop through each file in the subdirectory
                for filename in os.listdir(subdir_path):
                    if filename.endswith(".txt"): 
                        # Open each file and read its contents
                        with open(os.path.join(subdir_path, filename), "r", encoding='latin-1') as f: 
                            # Remove the words before the first colon in each sentence
                            contents = f.read() 
                            contents = re.sub(r'^[^:]+:\s*', '', contents, flags=re.MULTILINE) 
                            # Append the contents to the list
                            transcript_contents.append(contents) 

# Merge the contents of the list into a single string
merged_contents = "\n".join(transcript_contents) 

# Create an empty dictionary to store the questions and answers
qa_dict = {"questions": [], "answers": []}

# Split the merged contents into lines
lines = merged_contents.split("\n")

# Loop through the lines and assign "question" and "answer" category to each alternate line
for i in range(0, len(lines)-1, 2):
    question = lines[i]
    answer = lines[i+1]
    qa_dict["questions"].append(question)
    qa_dict["answers"].append(answer)
    
# Set the path to the output file
output_file_path = "q_dict.json"

# Write the dictionary to the output file in JSON format
with open(output_file_path, "w") as f:
    json.dump(qa_dict, f)