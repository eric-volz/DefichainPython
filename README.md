# Documentation of the Defichain Python Library

### **The documentation can be found at:** 
**https://docs.defichain-python.de**


---

# Components of documentation
The documentation website is hosted via GitHub Pages. 
All build files can be found on the `gh-pages` branch.

## ℹ️ /additionalInfos
A place to store additional information of the documentation such as 
reddit posts, instructions or pictures.

## 🏗️ /build
This folder is only visible n the `gh-pages` branch and contains all 
files which are necessary to display the HTML page.

## 📚 /source
This folder contains all the files that define the documentation. 
These can be compiled and are saved in the `/build` folder as HTML.


# Build Documentation
To build the documentation yourself, follow these steps:

```bash
cd docs  # change directory to docs
pip install -r requirements_docs.txt  # install dependencies

make clean html  # builds the documentation as html
```
The compiled documentation is now accessible via the `index.html` in the `/build/html` folder.