# predict_concrete_strength

1.Problem_Statement:

To predict concrete strength based on following parameters:

    1.cement: 
        a substance used for construction that hardens to other materials to bind them together.
        Data Type -- quantitative
        Measurement -- kg in a m3 mixture
        Description -- input variable

    2.slag: 
        Mixture of metal oxides and silicon dioxide.
        Data Type -- quantitative
        Measurement -- kg in a m3 mixture
        Description -- input variable

    3.Flyash:
        coal combustion product that is composed of the particulates that are driven out of coal-fired boilers together with the flue gases.
        Data Type -- quantitative
        Measurement -- kg in a m3 mixture
        Description -- input variable

    4.Water:
        It is used to form a thick paste.
        Data Type -- quantitative
        Measurement -- kg in a m3 mixture
        Description -- input variable

    5.Superplasticizer:
        used in making high-strength concrete.
        Data Type -- quantitative
        Measurement -- kg in a m3 mixture
        Description -- input variable

    6.Coaseseaggregate:
        prices of rocks obtain from ground deposits.
        Data Type -- quantitative
        Measurement -- kg in a m3 mixture
        Description -- input variable

    7.fineaggregate:
        the size of aggregate small than 4.75mm.
        Data Type -- quantitative
        Measurement --kg in a m3 mixture
        Description -- input variable

    8.age:
        Rate of gain of strength is faster to start with and the rate gets reduced with age.
        Data Type -- quantitative
        Measurement --kg in a m3 mixture
        Description -- input variable

    9.Concrete compressive strength:
         Measurement unit of concrete strength.
         Data Type -- quantitative
         Measurement -- psi
         Description -- output variable

2.Dataset:

    The dataset was downloade from kaggle website
["CONCRETE_DATASET"](https://www.kaggle.com/datasets/elikplim/concrete-compressive-strength-data-set/download?datasetVersionNumber=1)

3.Packages_Required:

    All the packages required for model building are mentioned in requirement.txt file

4.Dataset_Reading:

    Done using pandas library as follows:

        df = pd.read_excel(' Concrete_data.xlsx')

        df

5.Model_Building:

    Algorithm used : Linear Regression

    Steps:

    Following steps involved in model building

    1.Exploratory_Data_Analysis

    2.Feature_Engineering

    3.Feature_selection

    4.Data_Splitting

    5.Model_Training

    6.Model_Evaluation

    7.Assumption_Check

    8.Single_Row_Check

    9.Pickle file_Creation

6.API_Writing:

    API writing for builded model was done in VS Code with help of flask web framework, along with HTML code.

    Model data required for writing api importted through pickle file

    It was then tested using Postman app.

    command to run flask app in vs code:

    flask run

    or

    python app.py

7.Deployment_On_Cloud:

    Build model was deployed on cloud using Amazon web services's EC2 instance and Git Bash terminal

    command to run app in Git Bash

    python3 app.py
