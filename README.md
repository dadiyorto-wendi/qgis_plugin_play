### QGIS Plugin Feasibility Investigation

A look into how feasible it might be to build a QGIS Plugin for the hydrological team.

#### Installation

QGIS Plugins are written in python

    conda env create -f environment.yml
    conda activate qgis-env

and see this confluence page

https://confluence.ecmwf.int/pages/viewpage.action?pageId=340770726

#### Usage

    # run QGIS inside environment with python dependencies
    (qgis-env)$ qgis

Once QGIS is running install the hydrological_analysis_tools plugin

Plugins > Manage and Install Plugins..

![Screenshot 2023-07-14 at 11 57 42](https://github.com/ecmwf-projects/qgis-playground/assets/16657983/cb6f1349-ac9d-4afe-a2dc-3f9414337abd)
