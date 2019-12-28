# python-imdb-to-excel

- This application gives you an excel contains to IMDB movie details according to rating score higher than you choose in project directory.


 # Getting Started

## 1. Download or clone this repo with

```
git clone https://github.com/oktydag/python-imdb-to-excel.git

```


# Steps For Run
## 1.  virtualenv

Create a virtualenv and activate it.

<pre>$ pip install virtualenv
</pre>

<pre>$ virtualenv venv
</pre>

<pre>$ source venv/bin/activate
</pre>

Activate venv for **Windows**
<pre>$ cd venv
</pre>

<pre>$ source Scripts/activate
</pre>

**virtualenv** is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

## 2.  Installing Requirement Packages

You can use this command to be able to install necessary modules for python. There is a requirement text which includes the packages which have been used. The only thing you need to do is to run the given command for all packages you need.

<pre>$ pip install -r requirements.txt
</pre>


## 3. Run the main.py in venv

<pre>$ (venv) python main.py
</pre>

Give a minimun input rating score that you want to lists movies such as **8.4**


## 4. See The Result

You can find the excel sheet on your project directy whose name is **imdb_your_chooses.xlsx**
