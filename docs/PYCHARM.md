# Pycharm setup

- [Pycharm setup](#pycharm-setup)
- [Prerequisites](#prerequisites)
- [Getting started](#getting-started)

# Prerequisites

- [Pycharm](https://www.jetbrains.com/pycharm/)

# Getting started

1. Clone your repository in a folder: `git clone git@github.com:GeniALE/SiteWebGeniALE.git`
2. Open Pycharm
3. Open the project folder
4. Click on **File** > **Settings** > **Project settings** > **Project interpreter**
5. On the right panel bar, click on the **gear** icon and select `Add...`
6. Select *Virtual env*, select you Python 3.X interpreter and make sure the virtualenv folder is named `venv`. 
    ![Example](https://i.imgur.com/luyIarS.png)
    
7. You need to create a `.env` file to store your environment's variables.
    
    You can also copy `.env.example` to `.env`. It contains some of the default env variables.
    
    > *Note: As this file is mandatory, you don't have to put variables in it. As long as it exists, it's fine.*
8. Open a terminal [and make sure it's prefixed by `(venv`)] and install the dependencies:

    ```shell
    pip install requirements.txt
    ```
9. To run the application, you can select the run configuration (`Run with migrations`) and click on **Play**
10. The DjangoCMS should be running at [http://localhost:8000](localhost:8000)
11. To create the superuser, you can execute the running task: `Create Super User`
