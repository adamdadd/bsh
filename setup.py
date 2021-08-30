from cx_Freeze import setup, Executable
  
setup(name = "bsh",
      version = "0.1" ,
      description = "" ,
      executables = [Executable("bulletsh/__main__.py", target_name="bsh")])
