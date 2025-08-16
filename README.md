Python Software Search Tool
This Python script, filesearch.py, provides a simple graphical user interface (GUI) application for searching .exe files (executable software) on your Windows system. It allows you to specify a search directory and a software name, then lists all found executables. You can also open the located software directly from the application.

The application leverages Python's tkinter for the GUI, os for file system operations, and threading to perform the search asynchronously, preventing the GUI from freezing during long searches.

Key Features:
GUI Interface: An intuitive graphical interface built with tkinter.

Directory Selection: Allows you to choose a custom root directory for your search, instead of just the default C:\.

Asynchronous Search: The file search runs in a separate thread, ensuring the application remains responsive while searching large directories.

Real-time Progress Updates: Displays the current directory being scanned, giving you feedback on the search progress.

List Search Results: Shows all found .exe files that match your entered name in a scrollable list.

Open Software: You can directly launch any selected software from the search results list.

How to Use:
Save the Script: Save the provided Python code as filesearch.py on your computer.

Run the Application: Open a command prompt or terminal, navigate to the directory where you saved the script, and run it using Python:

Bash

python filesearch.py
Application Interface:

Input Field: At the top, there's a text field where you should enter the name of the software you want to find (e.g., "chrome", "firefox", "word").

"选择搜索目录" (Select Search Directory) Button: Click this button to open a dialog box where you can choose the root directory for your search. By default, it starts at C:\.

"搜索" (Search) Button: After entering the software name and optionally selecting a directory, click this button to start the search.

"搜索进度：" (Search Progress:) Label: This label will update to show you which directory the script is currently scanning.

Result Listbox: Below the progress label, a listbox will populate with the full paths of all .exe files found that match your search query.

"打开" (Open) Button: Select an item from the result listbox and then click this button to launch the corresponding software.

Searching:

Enter the name of the software (or part of its name) into the input field.

(Optional) Click "选择搜索目录" to change the starting search folder.

Click "搜索" to begin. The "搜索" button will be disabled during the search and re-enabled once it's complete. You'll also get a "搜索完成" (Search Completed) message.

Opening Software:

Once the search is done, click on any item in the result listbox to select it.

Click the "打开" button. The application will attempt to open the selected executable.

Note: The script handles PermissionError silently, meaning it will skip directories you don't have access to without crashing.
