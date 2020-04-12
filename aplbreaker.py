import sys
import time
import math
import binascii
import numpy as np
import itertools as it
from hashlib import sha1
from PIL import Image, ImageDraw, ImageFont


def usage():
    print("           _____  _      ____                 _              ")
    print("     /\   |  __ \| |    |  _ \               | |             ")
    print("    /  \  | |__) | |    | |_) |_ __ ___  __ _| | _____ _ __  ")
    print("   / /\ \ |  ___/| |    |  _ <| '__/ _ \/ _` | |/ / _ \ '__| ")
    print("  / ____ \| |    | |____| |_) | | |  __/ (_| |   <  __/ |    ")
    print(" /_/    \_\_|    |______|____/|_|  \___|\__,_|_|\_\___|_|    ")
    print("                                                             ")
    print("                                                   @AleDiBen ")
    print("An Android Pattern Lock Breaker.\n")
    print("USAGE:")
    print("      python pbreaker.py KEYFILE\n")
    print("where KEYFILE is a file with .key extension that contains the")
    print("android unlock pattern to decrypt.\n")
    print("EXAMPLES:")
    print("      python pbreaker.py gesture.key")
    print("      python pbreaker.py privacy_password_setting.key\n")

digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
min_seq_len = 4
max_seq_len = 10

r = 20
k = 84


def draw_seq(sequence):
    img = np.zeros([250, 250, 3], dtype=np.uint8)
    img.fill(0)
    img = Image.fromarray(img, 'RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 36)
    for x in sequence:
        xval = int(ord(x) - 48) % 3
        _, yval = math.modf(int(ord(x) - 48) / 3)
        posx = 2*r + xval * k
        posy = 2*r + yval * k
        draw.ellipse((posx-r, posy-r, posx+r, posy+r), fill=(255, 0, 0, 0))
        draw.text((posx-10, posy-18), str(x), fill=(255,255,255,0), font=font)

    for x in range(0, len(sequence)-1):
        x1_val = int(ord(sequence[x]) - 48) % 3
        _, y1_val = math.modf(int(ord(sequence[x]) - 48) / 3)
        x2_val = int(ord(sequence[x+1]) - 48) % 3
        _, y2_val = math.modf(int(ord(sequence[x+1]) - 48) / 3)
        posx1 = 2*r + x1_val * k
        posy1 = 2*r + y1_val * k
        posx2 = 2*r + x2_val * k
        posy2 = 2*r + y2_val * k
        draw.line((posx1, posy1, posx2, posy2), fill=(0, 255, 0, 0), width=3)

    img.show()

def crack(android_hash):
    patterns = []

    for i in range(min_seq_len, max_seq_len):
        # Generate all permutations of length i
        permutations = it.permutations(digit_list, i)
        for p in permutations:
            # Convert each digit to a specific byte
            # - 0 --> 0x00
            # - 1 --> 0x01
            # - 2 --> 0x02
            # - ...
            # - 8 --> 0x08
            # convert bytes to a string and append the string
            # to "patterns" list
            patterns.append(''.join(chr(int(ord(x)-48)) for x in p))

    # For each pattern
    for p in patterns:
        # Calculate the unsalted sha1 hash
        p_hash = sha1(p.encode('UTF-8')).hexdigest()
        # If the calculated hash is the same as
        # the android hash we cracked the pattern
        if p_hash == android_hash:
            # Decode the pattern
            cracked = binascii.hexlify(p.encode('UTF-8')).decode('UTF-8')
            secret = ''
            # Build the string that represents the pattern
            for x in range(1, len(cracked), 2):
                secret +=  cracked[x]
            print("[ CRACKED! ] " + secret)
            draw_seq(secret)
            return

    print("[ UNLUCKY ] Pattern not found.")
    return


if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    # Check rguments
    if argc == 0:
        usage()
    elif argc == 1:
        try:
            f = open(argv[0], 'rb').read()
        except:
            print ("[  ERROR!  ] Not a valid file\n")
            exit(-1)

        # Read the hash as UTF-8 string
        hash = binascii.hexlify(f).decode('UTF-8')
        crack(hash)

    exit(0)
