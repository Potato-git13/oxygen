import os
import sys
from opts import getOpts

options = getOpts(sys.argv[1:])

makefileContents = f"""\
CFLAGS=
CC=gcc

OUTDIR=bin
OUTNAME=$(OUTDIR)/{options.binName}
FILES=src/main.c

clean: $(OUTDIR)
\trm -rf $(OUTDIR)

compile: $(FILES)
\tmkdir -p $(OUTDIR)
\t$(CC) -o $(OUTNAME) $(FILES) $(CFLAGS)

compile-debug: CFLAGS += -g
compile-debug: compile

run: compile $(OUTNAME)
\t$(OUTNAME)

install:
\tsudo cp -p $(OUTNAME) /bin/{options.binName}

uninstall: /bin/{options.binName}
\tsudo rm /bin/{options.binName}

.PHONY: clean compile compile-debug run install uninstall\
"""

def createDir(path, log):
    try:
        os.mkdir(path)
        if log:
            print(f"info: Created {path}")
    except FileExistsError:
        pass
    except PermissionError:
        print(f"oxygen: {path}: Permission denied")
        sys.exit(1)

def createFile(path, contents, log):
    try:
        with open(path, "x") as file:
            file.write(contents)
        if log:
            print(f"info: Created {path}")
    except FileExistsError:
        with open(path, "w") as file:
            file.write(contents)
    except PermissionError:
        print(f"oxygen: {path}: Permission denied")
        sys.exit(1)

createDir(options.projName, True)
createDir(f"{options.projName}/src/", True)

createFile(f"{options.projName}/src/main.c", "", True)
createFile(f"{options.projName}/Makefile", makefileContents, True)
