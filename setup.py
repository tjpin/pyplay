from cx_Freeze import setup, Executable
# pip install cx_freeze

files = ["play.ico", "src/", "widgets/", "assets/"]  # other files to include
target = [Executable(
    script='app.py',
    base="Win32GUI",
    icon="play.ico"
    ),
    Executable("app.py"),
    #Executable("file_dialog.py")
]


setup(
    name="Pyplay",
    version="1.0",
    author="Chairman studios",
    description="advanced music player",
    options={"build_exe": {"include_files": files}},
    executables=target
)
