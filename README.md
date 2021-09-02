# Bulletsh
![img](img/bulletsh.svg)

Bsh is a shell wrapper that sends push notifications using pushbullet. On success or failure of any bash command run get a notification on your phone. No babysitting scripts, set them off and come back when they've failed or completed.

## Prerequisites
- python 3.7+
- free pushbullet account

Create api token for your pushbullet account from [Account Settings](https://www.pushbullet.com/#settings/account)

Add this token to the first line of a text file in the path:
```
$HOME/.bulletsh/token.txt
```

## Running using python
### Installing package
```bash
pip install .
```

### Running as python module
Can be run as module using following command in any shell:
```bash
python3 -m bulletsh
```

### Running
Run command in any shell
```bash
bsh
```

## Compiling to binary
```bash
python3 setup_cx.py build
```

This should create a binary in the build folder

symlink binary to PATH

```
ln -s <full_path_to_binary> <PATH>
```

### Running shell command
Run from any shell
```bash
bsh
```

## Contribution
Feel free to submit pull requests or issues :)

## LICENSE
[MIT License](./LICENSE)

