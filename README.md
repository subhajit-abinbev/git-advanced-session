###########################################################################################################
Basic Setup

1. Follow these steps to create a new conda environment for live testing:
   conda create -n git-demo python=3.11 -y
   conda activate git-demo
   pip install requirements.txt

2. Create a branch in the repo <https://github.com/subhajit-abinbev/git-advanced-session> and clone it
   git clone https://github.com/subhajit-abinbev/git-advanced-session.git
   git checkout <your-branch-name>
   ###########################################################################################################

###########################################################################################################
Git Ignore

1. Create a blank .env and blank .gitignore
2. Check status (git status) and it will show .env being tracked
3. Modify the .gitignore file (Will be shared over chat)
4. Remove the cache (git rm --cached <file>)
5. Modify the .env file and check status again. (Will be shared over chat)
6. Push all the changes to your branch
   ###########################################################################################################

###########################################################################################################
Pre-Commit Hooks

1. Lets add some files with secrets. Lets try to commit them. (Will be shared over chat)

2. Lets add a notebook where we smartly read values from .env file. Now, lets run the notebook. (Will be shared over chat)

3. Lets add a file over 1 MB. (Will be shared over chat)

4. Now lets reset
   git reset --hard origin/main

5. Steps to install pre-commit hooks:
   pre-commit install

6. Lets add the files and try to commit them again.
   ###########################################################################################################

###########################################################################################################
Pytest

1.  ###########################################################################################################
