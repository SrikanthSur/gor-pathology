# gor-pathology

## Installation <a name='installation'></a>

### Prerequisites <a name='prerequisites'></a>

1. Pycharm
2. Python 3.12
3. Selenium web driver

### Technologies Used <a name='technologies-used'></a>

1. <b>Selinium (Python)</b>
2. Pytest
3. Allure Report

## Steps for executing Autoation script></a>

1. Open a Project in Pycharm
2. Go to the file 🡪 settings 🡪 Open Project 🡪 python interpreter 
        Here by clicking on the + sign, we add the required packages.
3.        Package 1: Search for selenium and install it.
          Package 2: Search for Pytest and install it.
          Package 3: Search for Pytest-html and install it.
    Package 4: Search for allure-pytest and install it.
4. Open Project in terminal (Left click -> Open In -> Terminal)
5. Command to execute -> <b>pytest</b> in Terminal window

## Steps for Generate HTML Report></a>
1. Open a project in Teminal
2. Comand to generate HTML Report -> <b>pytest –html=”folderpath\reportname.html”</b>

## Steps for Generate Allure Report></a>
1. Download Allure Report (.zip) file -> https://github.com/allure-framework/allure2/releases/tag/2.24.1
2. Extract the downloaded zip file and save it in the C drive.
3. Go inside the Allure folder 🡪 go inside the bin folder 🡪 copy the path
4. Open Environment Variables 🡪 click on the path under system variable 🡪 click on edit 🡪 add path there 🡪 click ok
5. Open Terminal window
6. Execute thos command -> <b>pytest - -alluredir=”folderPath/allureReport” </b>
7. The report will be generated in the “allureReport” folder.
8. Now, to view the generated Allure report in a readable format, go through the following steps.
   1. Copy the absolute path of the allureReport folder.
   2.  Open the command prompt and execute the following command.
                  <b>allure serve allureReportFolderPath</b>
      E.g.: allure serve C:\Users\shoeb\OneDrive\Desktop\hybrid_framework_03\Reports\allureReport
    
    <b>Note: To execute the above command successfully, we also need to install JDK and we need to add the path to the Environmental variable.</b>
