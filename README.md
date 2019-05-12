# nbexport, Python code to export .ipynb file from .py

This is a Python code to export .ipynb file from .py using `#%%` as the separator of cells so your Python code can be run in Jupyter or Google Colab (with GPU) keeping the code chunks separated as cells.

This Python code is especially useful for Pythonistas who use PyCharm Professional's Scientific Mode to develop a Deep Learning code and Google Colab to run with GPU.

## Instruction to use as an external tool in PyCharm

Navigate to `File` >> `Settings` >> `Tools` >> `External Tools` >> `+` icon, and configure as shown in the following screenshot.

<img src="images_for_readme/PyCharm_External_Tools.PNG">
<p align="center">
	Set up in PyCharm External Tools
</p>

To use, right-click the .py file >> External Tools >> "Export .ipynb" as shown in the following screenshot.

<img src="images_for_readme/Use _PyCharm_External_Tool.png"> 
<p align="center">
	Use as a PyCharm External Tool
</p>

Reference: https://www.jetbrains.com/help/pycharm/settings-tools-external-tools.html
