# Merge CSV Files
This is a simple program that allows you to merge CSV files from a source folder to a destination folder. It was developed in Python and uses the PySimpleGUI library to create a user-friendly graphical user interface (GUI).

*Operation
Select Source Folder: Click the "Select Source Folder" button to choose the folder containing the CSV files you want to merge.

Select Destination Folder: Click the "Select Destination Folder" button to choose the folder where the merged file will be saved.

Merge CSV: After selecting the source and destination folders, click the "Merge CSV" button to start the merge process. The CSV files in the source folder will be combined into a single file called "Merged_File.csv" in the destination folder.

Error Messages: If you try to merge without selecting both the source and destination folders, the program will display an error message asking you to select the missing folders.

*Configuration and Execution
1 - Make sure you have Python installed on your system. You will also need the PySimpleGUI library, which can be installed with the following command:

pip install PySimpleGUI

2 - Run the program with the following command:

python seu_script.py

3 - Use the graphical interface to select the source and destination folders and merge the CSV files.

*Personalization
You can customize the program by adjusting the logic within the select_source_folder(), select_destination_folder() and merge_csv() functions, according to your needs. Additionally, you can customize the appearance of the GUI by changing the theme and layout as desired.

This program is a simple demonstration of how to create a CSV file merge tool with Python and PySimpleGUI. Feel free to expand and customize to your specific requirements.
