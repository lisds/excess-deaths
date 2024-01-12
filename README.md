# DSIP template repository

To set up builds for this report, run this command in the root directory of this repository (the directory containing this `README.md` file):

```bash
pip3 install -r build_requirements.txt
```

This will install all the prerequisites.

To fetch the vaccination data, run:

```bash
python3 fetch_data.py
```
Since there is no direct download URL for the excess deaths data, complete the following instructions to fetch the data:

 1. Navigate to the following site https://ec.europa.eu/eurostat/databrowser/view/DEMO_MEXRT__custom_1210067/bookmark/table?lang=en&bookmarkId=fc27a3a9-082b-461d-830b-a4c7b36caf4f
 2. Of the download options, select 'Full dataset [demo_mexrt]' in xlsx format
 3. Save this file in the following directory 'excess_deaths/data'


To build the book, run:

```
jupyter-book build .
```

The book build appears in the `_build/html` directory.  You can open it with your browser.
