# Bulletsh
![img](img/bulletsh.svg)

Bsh is a shell wrapper that sends push notifications using pushbullet.

## Prerequisites
- python 3.7+
- free pushbullet account

Create api token for your pushbullet account from [Account Settings](https://www.pushbullet.com/#settings/account)

Add this token to the first line of a text file in the path:
```
$HOME/.bulletsh/token.txt
```

## Installing Depenencies
```bash
pip install -r requirements.txt
```

## Compiling to binary (Recommended)
```bash
python3 setup.py build
```

This should create a binary in the build folder

symlink binary to PATH

```
ln -s <full_path_to_binary> <PATH>
```

### Running binary
Run from any shell
```bash
bsh
```

## Running using python
```bash
python3 -m bulletsh
```

## Contribution
Feel free to submit pull requests or issues :)

## LICENSE
[MIT License](./LICENSE)

