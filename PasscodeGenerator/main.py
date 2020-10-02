# PasscodeGenerator
# Sep 27, 2020

def main():

    file = open("passcode_1+.txt", "w+")

    # range 10000000000 -> from 0000000000 - 9999999999
    # file too large, split for sub 0 - 1000000000

    # 0000000000,0373862315, 1000000000 - > passcode_0+.txt
    # 1000000000, 2000000000 - > passcode_1+.txt
    # ...........
    # 9000000000, 10000000000 - > passcode_9+.txt

    for i in range(1370000000, 2000000000):
        file.write("{:010d}\n".format(i))

    file.close()
    print('Done')


if __name__ == "__main__":
    main()
