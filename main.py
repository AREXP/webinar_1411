import sys


def main():
    count = 0
    for line in sys.stdin:
        print(line)
        count += 1
    print('-' * 20)
    print('{} were read'.format(count))


if __name__ == '__main__':
    main()
