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

<pre>$ virtualenv venv
</pre>

<pre>$ source venv/bin/activate
</pre>

**virtualenv** is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

## 2.  install requests

<pre>$ pip install requests
</pre>


**requests** allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor. 
There is no need to manually add query strings to your URLs, or to form-encode your POST data.


## 3.  install BeautifulSoup4

<pre>$ pip install BeautifulSoup4
</pre>

 
**Beautiful Soup** is a library that makes it easy to scrape information from web pages. 
 
 It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.


## 4.  install openpyxl

<pre>$ pip install openpyxl
</pre>

 **openpyxl** is a Python library to read/write Excel xlsx/xlsm/xltx/xltm files.

It was born from lack of existing library to read/write natively from Python the Office Open XML format.

## 5. Run the main.py in venv

<pre>$ (venv) python main.py
</pre>

Give a minimun input rating score that you want to lists movies such as **8.4**


## 6. See The Result

You can find the excel sheet on your project directy whose name is **imdb_your_chooses.xlsx**
