# RubikVN.org

Source code for the soon-to-be new rubikvn.org, written in python3.6

## Under development

TODO: write scripts for other installation work besides `pip`

### Cloning the repo & running the server (first time)

0. Before cloning the repository, installing and starting the development process, please make sure you have these few things installed on your computer (I personally prefer developing on a \*NIX environment):
  - **[Python 3.6:](https://www.python.org/downloads/)** Python version >= 3.6 is required to run the project, on Ubuntu 18.04, it is the default version when you use `python3`. For other operating systems or distributions however, you may need to specifically write `python3.6`.

  - **[MySQL:](https://www.mysql.com/downloads/)** Download and install MySQL before hand, with a username `root` and use `admin` as password. Of course, you're free to choose a better password for your own good, but you might need to manually change a few things in our code base after that. I will edit our code so that you can use whatever password you want, but not now.

  - **[Git:](https://git-scm.com/)** We're using git for version control, so basic understanding of version control, git and gitlab is required.

Those 3 things are essential for running the website, so make sure you have all of them ready before following the next steps.

1. Clone the repository:
```bash
git clone https://gitlab.com/rubikvn/rubikvn.git
```
OR use SSH
```bash
git clone git@gitlab.com:rubikvn/rubikvn.git
```

2. Run installation script to have the database set up and project requirements downloaded for you
```bash
chmod 755 install.sh
./install.sh
```

3. Activate virtual environment
```bash
source rbvn-env/bin/activate
```
After that your terminal prompt will look like this:
```bash
(rbvn-env)
```


4. Run the server (on your localhost). Ctrl-C to stop the server
```bash
(rbvn-env) python3 manage.py runserver
```

5. Terminate virtualenv
```bash
(rbvn-env) deactivate
```
