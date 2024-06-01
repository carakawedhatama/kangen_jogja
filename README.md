# kangen_jogja

This project was initially aimed for predicting the house price in D.I. Yogyakarta. And due to incomplete data (and yet, this is my warm up to code a machine learning again), so I changed the data set using Ames House Price data source.

## Table of Contents

0. [Pre-requisites](#prerequisites)
1. [Installation](#installation)
2. [Usage](#usage)
3. [Data](#data)
4. [Model](#model)
5. [API](#api)
6. [Contributing](#contributing)
7. [License](#license)

## Prerequisites

Before you begin, you need to have these stacks installed:
- Python 3.7 or higher
- Jupyter Notebook or any other Python IDE (VSCode, PyCharm, etc)
- Django 4.2 or higher
- API tester (Postman, Thunderclient, Hoppscotch, etc)

## Installation

To install the required packages, run the following command:

```bash
pip install -r requirement.txt
```

## Usage

Before running the project, execute the following command:

```bash
python .\predictor\data\training.py
```

This will train the model and save it to a file. To run the project, run the following command:

```bash
python .\manage.py runserver
```

## Data

The data for this project is from the Ames Housing dataset from [Kaggle](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset), which contains information about houses sold in Ames, Iowa between 2006 and 2010. The dataset includes 79 features and 1 target variable (the sale price of the house).

The data is preprocessed by dropping irrelevant features, handling missing values, and one-hot encoding categorical features.

## Model

The model used in this project is a linear regression model. The model is trained on 80% of the data and evaluated on the remaining 20%. The evaluation metrics include mean absolute error, mean squared error, and R-squared.
By far, here's the initial evaluation metrics:

```bash
Mean Absolute Error (MAE): 18853.724695430483
Mean Squared Error (MSE): 1020363951.2054477
R-squared (R²): 87.27%
```

## API

The project includes a simple API for making predictions using the trained model. To make a prediction, send a POST request to the following URL:

```bash
http://127.0.0.1:8000/api/predict/
```

The request should include the following form data:

* `MSSubClass`: The building class.
* `MSZoning`: The general zoning classification.
* `LotArea`: The size of the lot in square feet.
* `Street`: The type of street access to the property.
* `LotShape`: The shape of the lot.
* `LandContour`: The flatness of the land.
* `Utilities`: The type of utilities available.
* `LotConfig`: The configuration of the lot.
* `LandSlope`: The slope of the land.
* `Neighborhood`: The physical locations of the property.
* `Condition1`: Proximity to various conditions.
* `Condition2`: Proximity to various conditions (if more than one is present).
* `BldgType`: The type of building.
* `HouseStyle`: The style of the house.
* `OverallQual`: The overall quality of the house.
* `OverallCond`: The overall condition of the house.
* `YearBuilt`: The year the house was built.
* `YearRemodAdd`: The year the house was remodeled.
* `RoofStyle`: The style of the roof.
* `RoofMatl`: The material of the roof.
* `Exterior1st`: The exterior covering on the house.
* `Exterior2nd`: The exterior covering on the house (if more than one material is present).
* `ExterQual`: The quality of the exterior covering.
* `ExterCond`: The present condition of the exterior covering.
* `Foundation`: The type of foundation.
* `Heating`: The type of heating system.
* `HeatingQC`: The quality of the heating system.
* `CentralAir`: The presence of central air conditioning.
* `1stFlrSF`: The size of the first floor in square feet.
* `2ndFlrSF`: The size of the second floor in square feet.
* `LowQualFinSF`: The size of the low quality finished area in square feet.
* `GrLivArea`: The size of the above grade (ground) living area in square feet.
* `FullBath`: The number of full bathrooms.
* `HalfBath`: The number of half bathrooms.
* `BedroomAbvGr`: The number of bedrooms above grade (does not include basement bedrooms).
* `KitchenAbvGr`: The number of kitchens above grade.
* `KitchenQual`: The quality of the kitchen.
* `TotRmsAbvGrd`: The total number of rooms above grade (does not include bathrooms).
* `Functional`: The home functionality rating.
* `Fireplaces`: The number of fireplaces.
* `PavedDrive`: The type of driveway.
* `WoodDeckSF`: The size of the wood deck in square feet.
* `OpenPorchSF`: The size of the open porch in square feet.
* `EnclosedPorch`: The size of the enclosed porch in square feet.
* `3SsnPorch`: The size of the three season porch in square feet.
* `ScreenPorch`: The size of the screen porch in square feet.
* `PoolArea`: The size of the pool area in square feet.
* `MiscVal`: The value of miscellaneous features.
* `MoSold`: The month the house was sold.
* `YrSold`: The year the house was sold.
* `SaleType`: The type of sale.
* `SaleCondition`: The condition of the sale.

Example for the body request:

```
MSSubClass=60&MSZoning=RL&LotArea=5000&Street=Pave&LotShape=Reg&LandContour=Lvl&Utilities=AllPub&LotConfig=Inside&LandSlope=Gtl&Neighborhood=NAmes&Condition1=Norm&Condition2=Norm&BldgType=1Fam&HouseStyle=2Story&OverallQual=7&OverallCond=5&YearBuilt=2003&YearRemodAdd=2003&RoofStyle=Gable&RoofMatl=CompShg&Exterior1st=VinylSd&Exterior2nd=VinylSd&ExterQual=TA&ExterCond=TA&Foundation=PConc&Heating=GasA&HeatingQC=Ex&CentralAir=Y&1stFlrSF=1000&2ndFlrSF=1000&LowQualFinSF=0&GrLivArea=2000&FullBath=2&HalfBath=1&BedroomAbvGr=3&KitchenAbvGr=1&KitchenQual=TA&TotRmsAbvGrd=6&Functional=Typ&Fireplaces=1&PavedDrive=Y&WoodDeckSF=100&OpenPorchSF=50&EnclosedPorch=50&3SsnPorch=0&ScreenPorch=0&PoolArea=0&MiscVal=0&MoSold=6&YrSold=2008&SaleType=WD&SaleCondition=Normal
```

The response will include the predicted sale price of the house.

Example for the response:

```json
{
  "price": 178709.64576348104
}
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.