#%%

import nbformat
from pathlib import Path

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_path_str", help="file_path_str")
args = parser.parse_args()

input_str = args.file_path_str


# input_str = input(r'.py file path:')
# input_str = input_str.strip(r'"')

sep = r'#%%'

input_path = Path(input_str)
file_name = input_path.stem
output_path = input_path.parent / (file_name + '.ipynb')

#%%

with input_path.open() as f:
    chunks = f.read().split(sep)

#%%

if chunks[0].__len__() == 0:
    chunks.pop(0)

nb = nbformat.v4.new_notebook()

metadata_dict = {
    "kernelspec": {
        "name": "python3",
        "display_name": "Python 3"
        },
    "accelerator": "GPU"
    }

nb["metadata"] = metadata_dict

nb["cells"] = [nbformat.v4.new_code_cell(sep+chunk) for chunk in chunks]

with output_path.open("w") as f:
    nbformat.write(nb, f)