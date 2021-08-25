from bulletsh import shellwrapper


class Bulletsh:
    def __init__(self, token):
        shellwrapper.ShellWrapper(token).cmdloop()
