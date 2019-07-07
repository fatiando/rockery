r"""
mcmurray_facies: Preprocessed well log and facies data for facies predictions
=============================================================================

    This is a preprocessed dataframe of well log & core information focused on facies prediction.

    **What is this Dataset**
    The dataset consists of well log curves, in other words 1D geophysical measurements made
    with a variety of different tool types pulled slowly up a well, and lithology IDs, which
    are basically visible interpretations of the lithology made by geologists looking at core.
    Core is a cylinder of rock taken as the well is drilled.

    **For What Analysis**
    Cores are expensive to collect, so they are not collected on every well. Well log
    curves are cheaper, so a number of well logs are collected on every well. A
    machine-learning model that predicts lithology/facies from well log curves accurately
    can provide facies without the expense of coring the well.

    **Where is this Dataset From?**
    The preprocessed data is coming from here:
    https://github.com/JustinGOSSES/McMurray-Wabiskaw-preprocessed-datasets

    The original dataset, unprocessed, comes from a collection of over 2000 wells made public
    by the Alberta Geological Survey’s Alberta Energy Regulator. To quote their webpage, “In 1986,
    Alberta Geological Survey began a project to map the McMurray Formation and the overlying
    Wabiskaw Member of the Clearwater Formation in the Athabasca Oil Sands Area. The data that
    accompany this report are one of the most significant products of the project and will
    hopefully facilitate future development of the oil sands.” It includes well log curves as LAS
    files and tops in txt files and xls files. There is a word doc and a text file that
    describes the files and associated metadata.

    [Wynne1995]_
    Wynne, D.A., Attalla, M., Berezniuk, T., Brulotte, M., Cotterill, D.K., Strobl, R.
    and Wightman, D. (1995): Athabasca Oil Sands data McMurray/Wabiskaw oil sands deposit
    - electronic data; Alberta Research Council, ARC/AGS Special Report 6.

    Please go to the links below for more information and the original dataset:

        Report for Athabasca Oil Sands Data McMurray/Wabiskaw Oil Sands Deposit
        http://ags.aer.ca/document/OFR/OFR_1994_14.PDF

        Electronic data for Athabasca Oil Sands Data McMurray/Wabiskaw Oil Sands Deposit
        http://ags.aer.ca/publications/SPE_006.html

    **Original Dataset License**
    In the metadata file (SPE_006_originalData/Metadata/SPE_006.txt) the dataset is described as
    Access Constraints: Public and Use Constraints: Credit to originator/source required.
    Commercial reproduction not allowed.

    **Dataset Changes and Additions**
    The Latitude and longitude of the wells is not in the original dataset.
    https://github.com/dalide -> @dalide used the Alberta Geological Society’s UWI
    conversion tool to find lat/longs for each of the well UWIs. A CSV with the
    coordinates of each well’s location can be found
    https://github.com/JustinGOSSES/MannvilleGroup_Strat_Hackathon/blob/master/well_lat_lng.csv.
    These were then used to find each well’s nearest neighbors.

    Please note that there are a few misformed .LAS files in the full dataset, so the code
    in this repository skips those.

    Additionally, all wells in the original dataset that didn't have facies are excluded here.

    **Notes on Returns**
    Depending on whether the abbreviations_only argument is set to True or False, the columns
    of the dataframe returned will either be the standard abbreviations for well log curve
    names or the abbreviations and the full spelled out names. Default value is True.

    You can find the long names for most any well log curve abbreviation here:
    https://www.apps.slb.com/cmd/ChannelItem.aspx?code=SN

    When this function runs, if the file isn't already in your data directory, it will be
    downloaded automatically.

    **Parameters**
    Parameters
    ----------
    load : bool
        Wether to load the data into a :class:`pandas.DataFrame` or just return the
        path to the downloaded data.

    **Returns**
    Returns
    -------
    mcmurray_facies : :class:`pandas.DataFrame` or str
        The loaded data or the file path to the downloaded data.
        The :class:`pandas.DataFrame` contains the following data:

        If abbreviationsOnly=True, then function returns dataframe columns of:
        ['CALI', 'COND', 'DELT', 'DEPT','DPHI', 'DT', 'GR', 'ILD', 'ILM', 'NPHI', 'PHID',
        'RHOB', 'SFL','SFLU', 'SN', 'SP','UWI', 'SitID','lat', 'lng', 'Depth', 'LithID',
        'W_Tar', 'SW', 'VSH','PHI', 'RW','lithName']

        If abbreviationsOnly=False, then functin returns dataframe columns of : ['CALI=Caliper',
        'COND=Fluid Conductivity', 'DELT=Travel Time Interval between Successive Shots',
        'DEPT=Depth', 'DPHI=Density Porosity',
        'DT=Delta-T also called Slowness or Interval Transit Time', 'GR=Gamma Ray',
        'ILD=Induction Deep Resistivity', 'ILM=Induction Medium Resistivity',
        'NPHI=Thermal Neutron Porosity (original Ratio Method) in Selected Lithology',
        'PHID=Porosity-LDT NGT Tools', 'RHOB=Bulk Density',
        'SFL=Spherically Focused Log Resitivity', 'SFLU=SFL Resistivity Unaveraged',
        'SN=Short Normal Resistivity (16 inch spacing)', 'SP=Spontaneous Potential',
        'UWI=Unique Well Identifier', 'SitID=Site Identification Number','lat=latitude',
        'lng=longitude','Depth=Depth', 'LithID=Lithology Identity Number',
        'W_Tar=Weight Percent Tar', 'SW=Water Saturation', 'VSH=Volume of Shale',
        'PHI=Porosity', 'RW=Connate Water Resistivity','lithName=Lithology Name']

"""
import matplotlib.pyplot as plt
import rockhound as rh

# Load mcmurray_facies into a DataFrame
facies = rh.fetch_mcmurray_facies(abbreviations_only=True)
print("first few rows of facies dataframe", facies.head())
print("facies columns", facies.columns)

# Example Plots
facies.plot(kind="scatter", x="GR", y="DPHI", color="red")
plt.show()
