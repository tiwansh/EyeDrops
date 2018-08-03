Python based app created on Ubuntu which notifies user to take a break after each hour.
Application also reads from a list in the Wunderlist API an shows all the tasks added in the notification tab.

Application notifies busy coders to take a break and take care of their eyes. Again it beeps after 10 minutes of breakto attract the lousy coder back to the workstation.

To use,
1. Download/clone the repo
2. install depedencies
	a. notify2
	b. playsound

3. Execute the main file - code.py.
(E.g. "python3 code.py")


In case you want to add it to your startup,
1. Go to Ubuntu Dash
2. Search and open "Startup Application"
3. Click on "Add"
4. Specify the name 
5. In command field, enter "python3 'path_where_the_code_is_saved'" For eg. I have entered - python3 "/home/anshuman/PycharmProjects/desktop_notifier/code.py"
6.Enter any comment you would like

P.S. There might be an error while installing the notify2 package in your virtual environment which states something like "dbus is a dependency and not found." In that case you must install python-dbus using python3 install python3-dbus. 
In case it again throws error, please switch to your base interpreter. 
If you still want to run the project in the virtual environment, you will have to install the python-dbus using the binaries since it throws exception with pip. 
