
import os

summ = 0

def main():
    global summ
    if os.fork() == 0:
        summ += 1
    else:
        os.wait()
        summ += 1
        print(summ)
    os.exit(0)
    


if __name__ == '__main__':
    main()
    # os._exit(0)