###########################################################################################################
Basic Setup

1. Follow these steps to create a new conda environment for live testing:
   conda create -n git-demo python=3.11 -y
   conda activate git-demo

   or

   py -3.11 -m venv git_essentials
   .\git_essentials\Scripts\activate

2. git clone https://github.com/subhajit-abinbev/git-advanced-session.git
   Change the path directory to git-advanced-session (press tab after cd)
   Create a branch in your local (git checkout -b <your-branch-name>)
   pip install -r requirements.txt

###########################################################################################################

###########################################################################################################
Git Ignore

1. Create a blank .env and blank .gitignore
2. Check status (git status) and it will show .env being tracked
3. Modify the .gitignore file (Will be shared over chat)
4. Remove the cache (git rm --cached <file>)
5. Modify the .env file and check status again. (Will be shared over chat)

###########################################################################################################

###########################################################################################################
Pre-Commit Hooks

1. Lets add some files (python notebook + python file) with secrets. (Will be shared over chat)

2. A notebook is already added (env_secrets_demo) where we smartly read values from .env file. Now, lets run the notebook. (Will be shared over chat)

3. Lets add a file over 1 MB. (Will be shared over chat)

4. Lets try to commit these files.

5. Now lets reset
   git reset --hard origin/main
   Lets add the files shared over chat again

6. Steps to install pre-commit hooks:
   pre-commit install

7. Lets add the files and try to commit them again.

###########################################################################################################

###########################################################################################################
Pytest

1. pytest tests/test_calculator.py 

###########################################################################################################
