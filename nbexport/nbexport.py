#%%

import nbformat
from pathlib import Path

#%%

sep = r'#%%'
input_path = Path().cwd() / 'examples' / 'sample_scientific_script.py'
file_name = input_path.stem
output_path = input_path.parent / (file_name + '.ipynb')

#%%
with input_path.open() as f:
    chunks = f.read().split(sep)

#%%

if chunks[0].__len__() == 0:
    chunks.pop(0)

nb = nbformat.v4.new_notebook()
nb["cells"] = [nbformat.v4.new_code_cell(sep+chunk) for chunk in chunks]

with output_path.open("w") as f:
    nbformat.write(nb, f)