import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kangen_jogja.settings')
import django
django.setup()

from django.conf import settings

csv_path = os.path.join(settings.BASE_DIR, 'predictor', 'data', 'AmesHousing.csv')
df = pd.read_csv(csv_path)

# drop irrelevant feature
df.drop(['Order'], axis=1, inplace=True)
df.drop(['PID'], axis=1, inplace=True)

# drop missing value's column
df.drop(['Electrical'], axis=1, inplace=True)
missing = df.isnull().sum()
missing = missing[missing>0]
df.drop(missing.index, axis=1, inplace=True)

X = df[['MSSubClass','MSZoning','LotArea','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope',
        'Neighborhood','Condition1','Condition2','BldgType','HouseStyle','OverallQual','OverallCond','YearBuilt','YearRemodAdd',
        'RoofStyle','RoofMatl','Exterior1st','Exterior2nd','ExterQual','ExterCond','Foundation',
        'Heating','HeatingQC',
        'CentralAir','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea','FullBath','HalfBath',
        'BedroomAbvGr','KitchenAbvGr','KitchenQual','TotRmsAbvGrd','Functional','Fireplaces',
        'PavedDrive','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch',
        'ScreenPorch','PoolArea','MiscVal','MoSold','YrSold','SaleType','SaleCondition']]  # Features
y = df['SalePrice']  # Target

X = pd.get_dummies(X)

columns = X.columns
columns_path = os.path.join(settings.BASE_DIR, 'predictor', 'models', 'columns.pkl')
joblib.dump(columns, columns_path)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
accuracy_percentage = r2*100

print(f"Model evaluation metrics:")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {accuracy_percentage:.2f}%")

model_path = os.path.join(settings.BASE_DIR, 'predictor', 'models', 'house_price_model.pkl')
joblib.dump(model, model_path)

print("Model training complete. Model saved to", model_path)
