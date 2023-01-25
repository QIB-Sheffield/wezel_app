# Installation
# ------------
# Create virtual environment and activate it.
# py -3 -m venv .venv_myproj           
# .venv_myproj/Scripts/activate 

# If you are contributing to dbdicom or wezel development, 
# Or you just want the latest version (prerelease),
# then download the source code from the development branch
# and install these as editable packages:

# pip install -e C:\Users\steve\Dropbox\Software\QIB-Sheffield\dbdicom
# pip install -e C:\Users\steve\Dropbox\Software\QIB-Sheffield\wezel

# If you are not contributing then just pip install wezel:

# pip install wezel

# Then install any other requirements needed in your application.
# For instance if you are including Transform or Segment menus,
# You must install some packages separately:

# pip install dipy
# pip install SimpleITK
# pip install itk-elastix

# Or else just list them all in a requirements file and run that:
# pip install -r requirements.txt

# To launch your application
# --------------------------

# Make sure to select the python interpreter in your virtual environment.
# In VSCode, go to "View->Command Palette->Python:select interpreter" 
# and the select the python interpreter in your virtual environment:
# .venv_myproj/Scripts/python.exe

# Now run execute.py, including your own menus as needed.

# To build an executable:
# -----------------------
# If First make sure you have pyinstaller:

# pip install pyinstaller

# To create an executable for distribution (single file):
# pyinstaller --name wezel --clean --onefile --noconsole --additional-hooks-dir=. --splash wezel.jpg exec.py

# To debug an executable:
# pyinstaller --name wezel --clean --additional-hooks-dir=. exec.py


import wezel
from mymenus import dev


if __name__ == "__main__":

    wzl = wezel.app()
    wzl.set_menu(dev)
    wzl.show()