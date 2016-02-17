#!/bin/bash
# Usage: call script with the path to your blog folder as an argument
cp -R css $1
cp -R _includes $1
cp -R _layouts $1
cp -R _sass $1
cp LICENSE $1
exit $?
