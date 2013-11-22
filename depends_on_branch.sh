#!/bin/bash

if [[ $TRAVIS_BRANCH = 'master' ]] ; then
    echo "master here"
elif [[ $TRAVIS_BRANCH = 'test1' ]] ; then
    echo "test1 here"
elif [[ $TRAVIS_BRANCH = 'test2' ]] ; then
    echo "test2 here"
elif [[ $TRAVIS_BRANCH = 'test3' ]] ; then
    echo "test3 here"
else
    echo $TRAVIS_BRANCH
fi
