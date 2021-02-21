import cx_Freeze
import sys
base = None
if sys.platform == "win32":
    base = "Win32GUI"
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Smart Calculator",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]/CALCULATOR.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="CALCULATOR.py", icon='icons3/on.ico', base=base)]

cx_Freeze.setup(
    version="2.0",
    description="Calculator@kenn",
    author="kennartfoudation",
    name="Smart Calculator",
    options={"build_exe": {"packages":["ttkthemes"],"include_files":['icons3','on.ico', 'AA.png', 'arrow.png', 'KM.ico']},
             "bdist_msi": bdist_msi_options,
             },
    executables = executables

    )
