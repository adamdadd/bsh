from cx_Freeze import setup, Executable

setup(name="bsh",
      author="Adam Dad",
      author_email='adam-dad@hotmail.co.uk',
      version="0.1",
      description="",
      license='LICENSE',
      packages=['bulletsh'],
      executables=[Executable("bulletsh/__main__.py", target_name="bsh")],
      install_requires=[
          "pushbullet.py~=0.12.0",
          "requests~=2.26.0",
      ],
      )
