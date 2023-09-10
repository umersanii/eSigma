from cx_Freeze import setup, Executable

# List of additional data files to include
additional_data = ["Y:/Coding/DiscBot/eSigma/data", "Y:/Coding/DiscBot/eSigma/requirements.txt"]

# Create an executable
executables = [
    Executable(
        script="Y:/Coding/DiscBot/eSigma/main.py",  # Path to your main script
        base="Win32GUI",  # Make it windowed
        icon="Y:/Icons/icons8-discord-50.ico",  # Path to your icon file
    )
]

# Setup cx_Freeze
setup(
    name="eSigma",
    version="1.0",
    description="Your description here",
    options={
        "build_exe": {
            "excludes": ["tkinter", "matplotlib"],
            "packages": ["nacl", "cffi", "pycparser"],
            "include_files": additional_data,
        }
    },
    executables=executables
)
