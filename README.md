# APLBreaker
An Android Pattern Lock Breaker written in Python3.

## Description and References
This Python3 helps you recover/crack the pattern lock of your Android device.\
**Note:** _it works ONLY on rooted devices._

Here we can inspect the original code related to the Android function "patternToHash()":\
https://android.googlesource.com/platform/frameworks/base/+/3553c296c0e0951a150f1783b2d0ff0d4bfe06cd/core/java/com/android/internal/widget/LockPatternUtils.java#728

Analyzing this function we can deduce that:
- the pattern is encrypted using SHA-1
- the pattern consists of a sequence of digits
- the digits represent the indices of a 3x3 matrix (the pattern lock grid)

Here we can find the name of the file containing the encrypted pattern:\
https://android.googlesource.com/platform/frameworks/base/+/6b0623a/services/core/java/com/android/server/LockSettingsStorage.java#52

## Tested Devices
- Xiaomi Redmi Note 5 Pro (whyred)
- Asus ZenFone Laser2 (ZE550KL)

## Features
The following features are supported
- [x] Recover/Crack a Pattern

## To-do list
- [ ] Improve the Readme

## Requirements
- binascii
- hashlib
- PIL (Pillow)
- numpy

## Examples
If you want to try the tool, below are the commands to run it on both Linux and Windows.
I also included an example, using a file extracted from my device named "pat.key". At the bottom of the page you can see a PNG image with the recovered/cracked sequence.

> Linux Version
```
user@kali:~$ python3 aplbreaker.py pat.key
[ CRACKED! ] 0124678
```

> Windows Version
```
C:\> python.exe aplbreaker.py pat.key
[ CRACKED! ] 0124678
```


![Image of Cracked Pattern](https://github.com/AleDiBen/APLBreaker/blob/master/decoded.png)\
_An example of cracked pattern._
