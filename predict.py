# def predict():
#     import joblib
#     import pandas as pd
#     from get_data import get_data

#     #Predict from saved model
#     loaded_model = joblib.load('random_forest_model.pkl')
#     y_pred = loaded_model.predict(x_test)
#     y_pred = pd.DataFrame(y_pred)
#     # y_pred = pd.DataFrame(y_pred, columns=['predicted_share_price'])
#     # print(y_pred)