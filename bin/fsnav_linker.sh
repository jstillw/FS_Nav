#!/bin/bash


# Build information
__AUTHOR__='Kevin Wurster'
__VERSION__='0.1'
__EMAIL__='wursterk@gmail.com'
__LICENSE__='See LICENSE.txt from original package'
__SOURCE__='https://github.com/geowurster/FS_Nav'


# Functions to print out helpful information
PRINT_HELP_INFO() {
    echo ""
    echo "The following flags print help information:"
    echo "  --help-info"
    echo "  --version"
    echo "  --license"
    echo "  --help"
    echo ""
    exit 1
}

PRINT_HELP() {
    echo ""
    echo "Help"
    echo ""
    exit 1
}

PRINT_VERSION() {
    echo ""
    echo "Version"
    echo ""
    exit 1
}

PRINT_LICENSE() {
    echo ""
    echo ${__LICENSE__}
    echo ""
    exit 1
}


# Loop through any arguments
for ARG in $@; do
    case ${ARG} in

        # Help options
        "--help" | "-help")
            PRINT_HELP()
            exit 1
            ;;
        "--help-info" | "-help-info")
            PRINT_HELP_INFO()
            exit 1
            ;;
        "--version" | "-version")
            PRINT_VERSION()
            exit 1
            ;;
        "--license" | "-license")
            PRINT_LICENSE()
            exit 1
            ;;
    esac
done


# Create functions that map to specific nav.py calls
function apps() { cd `nav.py apps` ; }
function cyghome() { cd `nav.py cyghome` ; }
function desktop() { cd `nav.py desktop` ; }
function documents() { cd `nav.py documents` ; }
function downloads() { cd `nav.py downloads` ; }
function dropbox() { cd `nav.py dropbox` ; }
function extdrive() { cd `nav.py extdrive` ; }
function gdrive() { cd `nav.py gdrive` ; }
function hd() { cd `nav.py hd` ; }
function home() { cd `nav.py home` ; }
function movies() { cd `nav.py movies` ; }
function music() { cd `nav.py music` ; }
function pictures() { cd `nav.py pictures` ; }
function public() { cd `nav.py public` ; }
function systembin() { cd `nav.py systembin` ; }
function userapps() { cd `nav.py userapps` ; }
function userbin() { cd `nav.py userbin` ; }
function googledrive() { cd `nav.py gdrive` ; }
function google_drive() { cd `nav.py gdrive` ; }
function mydocuments() { cd `nav.py documents` ; }
function my_documents() { cd `nav.py documents` ; }
function mymusic() { cd `nav.py music` ; }
function my_music() { cd `nav.py music` ; }
function mypictures() { cd `nav.py pictures` ; }
function my_pictures() { cd `nav.py pictures` ; }
function myvideos() { cd `nav.py movies` ; }
function my_videos() { cd `nav.py movies` ; }
function videos() { cd `nav.py movies` ; }
function extvol() { cd `nav.py extdrive` ; }
function extvolume() { cd `nav.py extdrive` ; }

exit 0