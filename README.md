# Photography Client Quote Generator

### A CLI tool to automatically generate formatted PDFs to send to potential new clients.

## Info

I found myself creating a never-ending amount of google sheets documents to cater to every possible permutation of deliverables for new clients. I would input all their relevant information manually, and use the print command to save it as a PDF. This required a lot of navigation and manual data entry, as well as moving files and information around continuously.

I decided to build this PDF generator that automates this work for me. It includes deliverables based on conditionals that I set through the CLI. It has easily saved me hours per month and increased my response time in sending quotes to potential new clients.

# How to use this tool:

First clone the repo to your local machine. Make sure you have Python 3.7+ installed. I suggest using a virtual environment like 'VirtualENV' available from pip.

You'll then want to 'pip install -r requirements.txt' to make sure you install the correct versions of the necessary libraries this tool is built on (namely Pillow and Reportlab).

Finally, simply run 'python app.py' from your terminal and answer the questions to produce a PDF in the same directory.