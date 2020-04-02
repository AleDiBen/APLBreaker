# APLBreaker
An Android Pattern Lock Breaker written in Python3.

## Description and References
This Python3 helps you recover/crack the pattern lock of your Android device.\
**Note:** _it works ONLY on rooted devices._

Here we can inspect the original code related to the Android function "patternToHash()":\
https://cs.android.com/android/platform/superproject/+/master:frameworks/base/core/java/com/android/internal/widget/LockPatternUtils.java;l=1270

Analyzing this function we can deduce that:
- the pattern is encrypted using SHA-1
- the pattern consists of a sequence of digits
- the digits represent the indices of a 3x3 matrix (the pattern lock grid)

Here we can find the name of the file containing the encrypted pattern:\
https://cs.android.com/android/platform/superproject/+/master:frameworks/base/services/core/java/com/android/server/locksettings/LockSettingsStorage.java;l=81

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
I also included an example file extracted from my device named "pat.key" and a PNG image with the recovered/cracked sequence.

> Linux Version
```
user@kali:~$ python3 pbreaker.py gesture.key
[ CRACKED! ] 0124678
```

> Windows Version
```
C:\> python.exe pbreaker.py gesture.key
[ CRACKED! ] 0124678
```
