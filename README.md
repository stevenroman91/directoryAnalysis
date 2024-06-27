# directoryAnalysis
## File and File Count Retriever
This Python function get_files_and_file_counts retrieves all the files in a given directory and its subdirectories, with the option to filter by specific file extensions. It returns a DataFrame containing the full path of each file found, the number of unique directories, and a DataFrame with the count of files per extension, sorted in descending order.

## Usage
To use this function, simply call it with the directory you want to analyze and (optionally) the file extensions you want to include:
```
import os
from collections import defaultdict
import pandas as pd

file_paths, num_folders, file_counts_df = get_files_and_file_counts('/path/to/directory', ['.pdf', '.docx'])
```
This will:

Retrieve all the files in the /path/to/directory directory and its subdirectories that have the .pdf or .docx extensions.
Return a DataFrame file_paths containing the full path of each file found.
Return an integer num_folders representing the number of unique directories.
Return a DataFrame file_counts_df with the count of files per extension, sorted in descending order.

## Parameters
directory (str): The directory in which to search for files.
extensions (list, optional): A list of file extensions to filter the files by (e.g., ['.pdf', '.docx']). If not provided, all files will be retrieved.

## Returns
pd.DataFrame: A DataFrame containing the full path of each file found.
int: The number of unique directories.
pd.DataFrame: A DataFrame with the count of files per extension, sorted in descending order.

## Example
Here's an example of how to use the function:
```
file_paths, num_folders, file_counts_df = get_files_and_file_counts('/path/to/directory', ['.py', '.ipynb'])
print(file_paths)
print(f"Number of unique directories: {num_folders}")
print(file_counts_df)
```

This will print the file paths, the number of unique directories, and the file counts per extension for Python and Jupyter Notebook files in the /path/to/directory directory and its subdirectories.
