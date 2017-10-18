from cx_Freeze import setup, Executable

setup(name='Text2Studly',
      version='0.1',
      description="Its a text to sTuDlY converter",
      executables = [Executable("StudlyCaseConverter.py")])
