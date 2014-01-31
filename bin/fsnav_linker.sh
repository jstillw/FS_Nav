#!/bin/bash

# Build information
__AUTHOR__='Kevin Wurster'
__VERSION__='0.1'
__EMAIL__='wursterk@gmail.com'
__SOURCE__='https://github.com/geowurster/FS_Nav'


# Functions to print out helpful information
PRINT_HELP_INFO() {
    echo "Help info"
    exit
}

PRINT_HELP() {
    echo "Help"
    exit
}

PRINT_VERSION() {
    echo "Version"
    exit
}

PRINT_LICENSE() {
    echo ""
    echo ${__SOURCE__}
    echo ""
    exit
}

# Create aliases
