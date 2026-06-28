@echo off
git update-index --chmod=+x %1
git add *
git commit -m "Holberton Task"
git push