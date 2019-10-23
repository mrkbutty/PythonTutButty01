Install Anaconda or Python
==========================

| Download from: https://www.python.org/downloads/release/python-380/
| Or https://www.anaconda.com/download/
| Or install minimal: https://docs.conda.io/en/latest/miniconda.html
| (Note: installing with dual x login means that administrator install is prefered) 

* Reccomend Python or Miniconda (they will need other packages installing)::

     > for %i in (ipython,click,pandas) do pip install %i
     > for %i in (jupyterlab,click,pandas) conda install %i

* Select latest version 3+ package!
     - Most new programmers should use latest python 3
     - Python 2 still around and python 2.7 version is the best bridge to version 3

* Initializing shells::

     > <path to anaconda>\condabin\conda init --all
     (Note that uninstall does not clean this up)

* Activating an environment::

     > conda activate [env]

* If upgrading run the "Anaconda Prompt" and type::

     > conda update conda
     > conda update anaconda

* Clean up old Anaconda packages from prompt using::

     > conda clean -a --dry-run
     > conda clean -a -y

* Rebuild Anaconda Start menu::

     > "C:\Anaconda3\pythonw.exe" "C:\Anaconda3\Lib\_nsis.py" mkmenus

* Anaconda is the most popular Data Science Python (and 'R') distribution
* Full Anaconda is rather bloated and Miniconda is much smaller.
* "Conda" is a distribtion and package management system containing 1000+ popular modules for python
* Most noteable packges are:
     - click (CLI interface)
     - pandas (data wrangling)
     - matplotlib + seaborn (charting)
     - xlsxwriter (Excel file creation)
     - flask (lightweight web framework)

        
    