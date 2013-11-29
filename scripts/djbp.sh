#!/bin/bash

# djbp bash script to install django-boilerplate to your django project.
#
############################################################################
# Usage:
#   djbp.sh [options]
#
# Options:
#   -h              Help
#   -p <project_path>  Install django-boilerplate to a specified project path
############################################################################
# Example to install on <your_project/docs>
# $ cd <your_project>
# $ wget https://raw.github.com/teracy-official/django-boilerplate/master/scripts/djbp.sh && chmod +x ./djbp.sh && ./djbp.sh -p .
#

function command_exists() {
    type "$1" &> /dev/null;
}

function require() {
    if ! command_exists git ; then
        echo "Error: 'git' is required for installation, please install 'git' first."
        echo "Installation aborted!"
        exit 1
    fi
}

function usage() {
    echo "Usage:"
    echo "  djbp.sh [options]"
    echo ""
    echo "Options:"
    echo "  -h                Help"
    echo "  -p <project_path> Install django-boilerplate to a specified project path"
}

function install() {
    # assume that the current working directory is the root git repository directory
    # to copy travis-ci stuff into this directory
    local project_root_path=`pwd`
    # relative or absolute <project_path>?
    if [[ $1 =~ ^\/ ]]; then
        local project_path=$1
    else
        local project_path="$project_root_path/$1"
    fi

    echo "installing django-boilerplate to '$project_path'..."
    cd /tmp
    rm -rf django-boilerplate
    git clone https://github.com/teracy-official/django-boilerplate.git
    cd django-boilerplate
    git fetch origin
    git checkout origin/master
    # test
    #git clone https://github.com/hoatle/django-boilerplate.git
    #cd django-boilerplate
    #git fetch origin
    #git checkout origin/tasks/10_installation_bash_script
    # copy required stuff

    echo "copying required files..."
    mkdir -p $project_path
    mv CHANGELOG.md CHANGELOG_django_boilerplate.md
    mv LICENSE LICENSE_django_boilerplate
    mv README.rst README_django_boilerplate.rst
    mv AUTHORS.md AUTHORS_django_boilerplate.md
    mv CONTRIBUTORS.md CONTRIBUTORS_django_boilerplate.md
    cp -r ./* $project_path
    #copy misisng .* files
    cp .travis.yml $project_path
    cp .pylintrc $project_path
    cp .gitignore $project_path
    #mkdir -p $project_root_path/.travis
    #cp -r .travis/* $project_root_path/.travis

    # clean up
    rm $project_root_path/djbp.sh
    cd ..
    rm -rf django-boilerplate

    echo ''
    echo "installation completed, please read $project_path/README_django_boilerplate.md for usage."
}

# check requirements
require

while getopts ":p:h" opt; do
    case $opt in
        p)
            install $OPTARG
            exit 0
            ;;
        h)
            usage
            exit 0
            ;;
        \?)
            echo "Invalid options -$OPTARG" >&2
            exit 1
            ;;
        :)
            if [ $OPTARG == "p" ]; then
                echo "Option -$OPTARG requires <project_path> argument." >&2
            fi
            exit 1
            ;;
    esac
done
