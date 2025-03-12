# pdf_split_pages
Split multi-page PDF.

pdf_split_pages is a small python script that splits a multi-page PDF into multiple smaller, user defined, PDF files. 

Uses pypdf.  

[pypdf Home](https://pypdf2.readthedocs.io/en/3.x/index.html)  
[pypdf GitHub](https://github.com/py-pdf/pypdf)


## Installation
pypdf installation is required.  
pypdf requires Python 3.8+ to run.

**Create virtual environment**  
[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)  
Linux:  

    python -m venv /path/to/new/virtual/environment
    $ source <venv>/bin/activate

Windows:  

    PS> python -m venv C:\path\to\new\virtual\environment
    PS C:\> <venv>\Scripts\Activate.ps1

**Install pypdf**  
Typically Python comes with pip, a package installer. Using it you can install pypdf:

    pip install pypdf

## Usage

**Designate input folder:**

    input_folder = "path/to/inputfolder"

**Designate output folder:**

    output_folder = "path/to/outputfolder" 

**Define settings:**  
Settings are defined as a dictionary. The keys are input file names. Each value is a list of tuples consisting of a page count and output file name.

    output_settings = {
        "input_file_1.pdf": [
            (2, "output_file_1.pdf"),
            (3, "output_file_2.pdf"),
            (1, "output_file_3.pdf")
        ],
        "input_file_2.pdf": [
            (10, "other_output_file.pdf"),
            (999, "output_file_other.pdf")
        ],
        "input_file_3.pdf": [
            (15, "names_are_hard.pdf"),
            (2, "Im_not_that_creative.pdf"),
            (6, "outfile.pdf"),
            (2, "ok_Im_done.pdf")
        ]
    }

