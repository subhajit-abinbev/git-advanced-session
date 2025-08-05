1. Follow these steps to create a new conda environment for live testing:
   conda create -n git-demo python=3.11 -y
   conda activate git-demo
   pip install requirements.txt

2. Lets add some files with secrets. Lets try to commit them.
   git reset --hard origin/main

3. Steps to install pre-commit hooks:
   pre-commit install

4. Lets try to commit the files again!

5. Lets add a notebook where we smartly read values from .env file
