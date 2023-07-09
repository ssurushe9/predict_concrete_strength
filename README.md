# predict_concrete_strength

1.Problem_Statement:

To predict concrete strength based on following parameters:

    1.cement: 
        a substance used for construction that hardens to other materials to bind them together.

    2.slag: 
        Mixture of metal oxides and silicon dioxide.

    3.Flyash:
        coal combustion product that is composed of the particulates that are driven out of coal-fired boilers together with the flue gases.

    4.Water:
        It is used to form a thick paste.

    5.Superplasticizer:
        used in making high-strength concrete.

    6.Coaseseaggregate:
        prices of rocks obtain from ground deposits. 

    7.fineaggregate:
        the size of aggregate small than 4.75mm.

    8.age:
        Rate of gain of strength is faster to start with and the rate gets reduced with age.

    9.csMPa:
         Measurement unit of concrete strength.

2.Dataset:
    The dataset was downloade from kaggle website
    ["CONCRETE_DATASET"](https://www.kaggle.com/datasets/elikplim/concrete-compressive-strength-data-set/download?datasetVersionNumber=1)

3.Dataset_Reading:
    Done using pandas library as follows:

        df = pd.read_excel(' Concrete_data.xlsx')

        df

4.Model was build using linear regression algorithm with following steps:

    1.Exploratory_Data_Analysis

    2.Feature_Engineering

    3.Feature_selection

    4.Data_Splitting

    5.Model_Training

    6.Model_Evaluation

    7.Assumption_Check

    8.Single_Row_Check

5.After model building it was stored in pickle file

6.API_Writing:

API writing for builded model was done in VS Code with help of flask web framework.

It was then tested using Postman app.

command to run flask app in vs code:

flask run

or

python app.py

7.Deployment_On_Cloud:

Build model was deployed on cloud using Amazon web services's EC2 instance.
