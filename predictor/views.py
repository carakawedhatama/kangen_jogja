import os
import joblib
import numpy as np
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Load the model
model_path = os.path.join(settings.BASE_DIR, 'predictor', 'models', 'house_price_model.pkl')
model = joblib.load(model_path)

columns_path = os.path.join(settings.BASE_DIR, 'predictor', 'models', 'columns.pkl')
columns = joblib.load(columns_path)

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:

            data = request.POST
            MSSubClass = int(data.get('MSSubClass'))
            MSZoning = data.get('MSZoning')
            LotArea = int(data.get('LotArea'))
            Street = data.get('Street')
            LotShape = data.get('LotShape')
            LandContour = data.get('LandContour')
            Utilities = data.get('Utilities')
            LotConfig = data.get('LotConfig')
            LandSlope = data.get('LandSlope')
            Neighborhood = data.get('Neighborhood')
            Condition1 = data.get('Condition1')
            Condition2 = data.get('Condition2')
            BldgType = data.get('BldgType')
            HouseStyle = data.get('HouseStyle')
            OverallQual = int(data.get('OverallQual'))
            OverallCond = int(data.get('OverallCond'))
            YearBuilt = int(data.get('YearBuilt'))
            YearRemodAdd = int(data.get('YearRemodAdd'))
            RoofStyle = data.get('RoofStyle')
            RoofMatl = data.get('RoofMatl')
            Exterior1st = data.get('Exterior1st')
            Exterior2nd = data.get('Exterior2nd')
            ExterQual = data.get('ExterQual')
            ExterCond = data.get('ExterCond')
            Foundation = data.get('Foundation')
            Heating = data.get('Heating')
            HeatingQC = data.get('HeatingQC')
            CentralAir = data.get('CentralAir')
            FirstFlrSF = int(data.get('1stFlrSF'))
            SecondFlrSF = int(data.get('2ndFlrSF'))
            LowQualFinSF = int(data.get('LowQualFinSF'))
            GrLivArea = int(data.get('GrLivArea'))
            FullBath = int(data.get('FullBath'))
            HalfBath = int(data.get('HalfBath'))
            BedroomAbvGr = int(data.get('BedroomAbvGr'))
            KitchenAbvGr = int(data.get('KitchenAbvGr'))
            KitchenQual = data.get('KitchenQual')
            TotRmsAbvGrd = int(data.get('TotRmsAbvGrd'))
            Functional = data.get('Functional')
            Fireplaces = int(data.get('Fireplaces'))
            PavedDrive = data.get('PavedDrive')
            WoodDeckSF = int(data.get('WoodDeckSF'))
            OpenPorchSF = int(data.get('OpenPorchSF'))
            EnclosedPorch = int(data.get('EnclosedPorch'))
            ScreenPorch = int(data.get('ScreenPorch'))
            PoolArea = int(data.get('PoolArea'))
            MiscVal = int(data.get('MiscVal'))
            MoSold = int(data.get('MoSold'))
            YrSold = int(data.get('YrSold'))
            SaleType = data.get('SaleType')
            SaleCondition = data.get('SaleCondition')

            # Preprocess the input and create feature array for prediction
            input_data = pd.DataFrame([[MSSubClass, MSZoning, LotArea, Street, LotShape, LandContour, Utilities, LotConfig, LandSlope, Neighborhood, Condition1, Condition2, BldgType, HouseStyle, OverallQual, OverallCond, YearBuilt, YearRemodAdd, RoofStyle, RoofMatl, Exterior1st, Exterior2nd, ExterQual, ExterCond, Foundation, Heating, HeatingQC, CentralAir, FirstFlrSF, SecondFlrSF, LowQualFinSF, GrLivArea, FullBath, HalfBath, BedroomAbvGr, KitchenAbvGr, KitchenQual, TotRmsAbvGrd, Functional, Fireplaces, PavedDrive, WoodDeckSF, OpenPorchSF, EnclosedPorch, ScreenPorch, PoolArea, MiscVal, MoSold, YrSold, SaleType, SaleCondition]], columns=['MSSubClass', 'MSZoning', 'LotArea', 'Street', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'ExterQual', 'ExterCond', 'Foundation', 'Heating', 'HeatingQC', 'CentralAir', 'FirstFlrSF', 'SecondFlrSF', 'LowQualFinSF', 'GrLivArea', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition'])
            # Assume the model was trained with one-hot encoded location, you need to do the same here
            input_data = pd.get_dummies(input_data)

            #feature_array = feature_array.flatten()
            input_data = input_data.reindex(columns=columns, fill_value=0)
            
            # Make prediction
            prediction = model.predict(input_data)[0]
        
            return JsonResponse({'price': prediction})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
