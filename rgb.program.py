# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a loop a for loop


def main():
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # process
    for counter3 in range(0, 256):
        for counter2 in range(0, 256):
            for counter1 in range(0, 256):
                print("RGB ({0},{1},{2})."
                      .format(counter3, counter2, counter1))


if __name__ == "__main__":
    main()
