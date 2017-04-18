#!/usr/bin/env python
import sys
import emul8

def main():
    emul8.sysinit()
    try:
        emul8.loadProgram(sys.argv[1])
    except IndexError:
        print("Usage: ./emul8 asmprogram");
        return 1
    emul8.execLoop()


if __name__ == "__main__":
    main()
