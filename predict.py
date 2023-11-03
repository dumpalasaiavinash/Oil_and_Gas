# def predict(x_test):
#     import joblib
#     import pandas as pd
#     from get_data import get_data

#     #Predict from saved model
#     loaded_model = joblib.load('20231017103237_random_forest_model.pkl')
#     # x_test = pd.read_csv('test.csv')
#     y_pred = loaded_model.predict(x_test)
#     y_pred = pd.DataFrame(y_pred)
#     y_pred = pd.DataFrame(y_pred, columns=['predicted_share_price'])
#     print(y_pred)

# # predict()
