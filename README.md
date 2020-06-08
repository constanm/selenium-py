# selenium-py
Sample project using Selenium and Python

## Prerequisites

YMMV

Download and install Python i.e. https://www.python.org/downloads/release/python-382/

Install _selenium_ dependency  
`pip install selenium`

Install _pytest_ dependency  
`pip install pytest`

## Versions of software used

### Browsers
<ul>
    <li>Firefox 76.0.1 (64-bit)</li>
    <li>Chrome 81.0.4044.138 (Official Build) (64-bit)</li>
</ul>

### IDE
<ul>
    <li>Pycharm 2020.1.1 CE</li>
</ul>

### Webdrivers
Download and extract the drivers locally then update the _config.yml_ paths.
<ul>
    <li><a href="https://github.com/mozilla/geckodriver/releases/tag/v0.26.0">geckodriver</a></li>
    <li><a href="https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/">chromedriver</a></li>
</ul>

### Other
Run in terminal and check:

`py -V`
Python 3.8.2

`pip -V`
pip 20.1

`pip show selenium`
selenium   3.141.0

`pip show pytest`
pytest      5.4.2

## How to run tests

Update _config.yml_ with any local paths needed.  
Run the suite in simplest package 
If the tests pass then your environment is correctly set up.