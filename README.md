# Betteromics
Betteromics is an integrated data platform catering to the life sciences industry, offering a comprehensive solution for managing, analyzing, and visualizing multi-omics data. This platform centralizes data storage, thereby facilitating seamless collaboration and data sharing across cross-functional teams. It further offers a rich array of data management, analysis, and visualization tools, expediting the extraction of valuable insights from your data.

Within this repository, you will find resources and guidance that empower you to optimize your data analysis processes through the utilization of the Betteromics API.



# Quickstart

## Setting Up Your Environment

To be able to run the data analysis examples in this repository, you will need to have Jupyter Notebook installed for Python users and install the R kernel for R users. Follow the steps below to set up your environment.


### For Python Users:

1. **Install Python:** If you haven't already, you'll need to have Python installed. You can download and install it from the official [Python website](https://www.python.org/downloads/).

2. **Install Jupyter Notebook:** Jupyter Notebook is a popular interactive computing environment for Python. You can install it using pip, which is a Python package manager. Open your command line or terminal and run the following command:
```bash
pip install jupyter
```

3. **Launch Jupyter Notebook:** After installing Jupyter, you can start the Jupyter Notebook server by running the command below. This will open a web browser where you can navigate to the repository directory and access the Python analysis notebooks.
```bash
jupyter notebook
```

---

### For R Users:

1. **Install R:** If you haven't already, download and install R from the [R Project website](https://www.r-project.org/).

2. **Install RStudio (Optional):** RStudio is a popular integrated development environment for R. You can download it from the [RStudio website](https://www.rstudio.com/products/rstudio/download/). While not required, it provides a user-friendly interface for working with R if you do not want to use Jupyter Notebook.

3. **Install the R Kernel for Jupyter (Preferred):** To run R in Jupyter Notebook, you'll need to install the R kernel. Open your command line or terminal and run the following command:
``` R ```

4. Inside the R console, install the IRkernel package:

```R
install.packages(c("devtools", "rzmq", "knitr", "dplyr", "tidyr", "magrittr", "testthat", "pbdZMQ", "repr",),
                 dependencies=TRUE,
                 repos = c("http://irkernel.github.io/", getOption("repos")),
                 type = "source"
                 )

devtools::install_github("IRkernel/IRkernel")
devtools::install_github('IRkernel/IRdisplay')

IRkernel::installspec()
```

5. **Launch Jupyter Notebook with R kernel:** After installing the R kernel, you can launch the given Jupyter Notebook examples and/or create your own R notebooks.
---

Now you're all set to explore and run the data analysis examples using Jupyter Notebook or R in this repository!



## How to access data
The API documentation and instructions to access data on Betteromics platform can be found in the `src` directory in this repository, which contains code in both python and R. After downloading the utility file based on your programming language preference, proceed to the examples directory for further instructions. You will find how to import the `utils` file and connect to data within each of the jupyter notebooks for a given examples. 
Once you have access to the specific public data, you can further explore and analyze the data using Betteromics.



# Available Public Datasets 
* The Cancer Genome Atlas Program [TCGA](https://www.cancer.gov/ccg/research/genome-sequencing/tcga)



# Changelog
Version 0.1 (2023.10.10)
Initial release



# License
© 2023 Betteromics Examples is licensed under the [MIT license](LICENSE).




