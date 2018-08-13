# Developer guide for RubikVN project

After following the installation guide (either README.md or windows_install.md), this document will show you the practices we will be using in our project, namely understanding our project structure, using Git for version control, writing good code, commenting. They will only help us in the long run when we need to maintain our website regularly, so I hope you all will spend some time perusing this document.

### Table of contents
* [Project structure](#project-structure)
  * [General](#general)
  * [Backend](#backend)
  * [Frontend](#frontend)
* [Git](#git)
* [Code formatting](#code-formatting)
* [Continuous Integrations](#continuous-integrations)

### Project structure

##### General

Since this is a Django project, which is simply a Python framework, we will structure our repo the Python way, i.e take advantage of packages and modules. When you clone the repository from Gitlab and finish installing, the directory tree will look something similar to the thing below. I will list everything that appears and explain their use:

```
    rubikvn/
      .git/               # This contains version control information
                          # so that Git can keep track of your repo
      RubikVNdotOrg/      # Contains Django project settings
      apps/               # Consists of smaller apps for website
      docs/               # Documentations for the project will be
                          # put here
      lib/                # Libraries and packages that our project
                          # may depend on
      rbvn-env/           # Virtual environment for python
      static/             # Includes CSS, Javascripts, static files
      templates/          # Html templates for rendering
      .gitignore          # Specify which files or patterns to ignore
      README.md           #
      install.sh          # Script for installation and regular updates
      manage.py           # Python script to use Django
      requirements.txt    # List of project dependencies
```

##### Backend

If you want to contribute to back end development, I highly recommend visiting the Django documentation website and finishing their tutorial (the one that builds a poll app). It's very simple to understand and should not take too long if you already now Python, or any other programming language. Our structure, as well as practices, try to follow that of Django documentations, and object oriented programming practices.

I will just go through the structure for back end, since I want to include everything in this guide. Open `apps/results`, and you will see an example of one simple app.

```
      migrations/         # Has info about our database
      models/             # Define our models
      __init__.py         # Tell python that this directory is
                          # a package
      admin.py            # Administrate the app
      apps.py             # Register the app on our project
      tests.py            # For unit testing
      urls.py             # For URL routing
      views.py            # Define website behavior
```

##### Frontend

I assume you already know a few things about Html, CSS, and Javascripts, or want to learn something about front end development. It's fine either way. Our repo structure is also very simple for that purpose. CSS and Javascripts, as well as static files such as images, audio or text files go to `static/APP_NAME`, and Html templates go to `templates/APP_NAME`. For example, if you are writing a template for our `results` app, put the Html file in `templates/results`. It is possible to put base layouts in `templates` and it is really good practice to do so, since it keeps our design for every web page consistent.

One more thing you need to know, because we are writing Html templates, instead of static pages, you need to know the [Django built-in language](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/) to manipulate data sent from back end. That's all for now.

### Git

There is a [Youtube tutorial](https://www.youtube.com/watch?v=HVsySz-h9r4&t=1540s&list=PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx&index=2) that I found really helpful when I first started working with Git. You can just spend 30 minutes watching the first video of the playlist. If you prefer reading documentation, [the one from the creator of Git](https://git-scm.com/docs/gittutorial) is undoubtedly among the best resources. This is the most important part of the project, so I want to make sure that you know the concept of version control, and some basic Git commands before starting.

```
      git clone
      git fetch
      git pull
      git branch
      git checkout
      git add
      git commit
      git push
      git log
```

In addition to the functionalities of git listed above, you might want to get yourself used to Gitlab, and the idea of making Issues and Merge requests for your code.

### Code formatting

Python tries to encourage writing code with indentation. So if you are a sensible programmer who follows good practices, you will be fine. Otherwise you code won't even run because of bad indenting. Right, and don't forget to leave comments if you want people to understand your code. When you commit and push your code, there will be other people who read and comment on your writing style. We all hope to improve in the long run.

This section will be updated, and more contents on Continuous Integration to come.

### Continuous Integrations
