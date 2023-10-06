def train(data):
    from sklearn.ensemble import RandomForestRegressor
    import pandas as pd
    import joblib
    from sklearn.pipeline import Pipeline
    from sklearn.metrics import mean_squared_error
    import datetime

    # data.to_csv('file1.csv')
    # 1.- Data Preparation
    train_df=pd.DataFrame()
    train_df=data[(data['name']=="REP.MC")]
    train_df=train_df[["share_price","oil_price"]].reset_index()

    # Load share price of other variables
    train_df = train_df.dropna()
    train_df['PMO.L']=data[(data['name']=="PMO.L")].reset_index()['share_price']
    train_df['CNE.L']=data[(data['name']=="CNE.L")].reset_index()['share_price']
    train_df['FP.PA']=data[(data['name']=="FP.PA")].reset_index()['share_price']
    # train_df['ENGI.PA']=data[(data['name']=="ENGI.PA")].reset_index()['share_price']

    from sklearn.model_selection import train_test_split
    x = train_df[["oil_price","PMO.L","CNE.L","FP.PA"]]
    y = train_df['share_price']
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,shuffle=True)
    x_train = x_train.dropna()
    y_train = y_train.dropna()
    y_train = y_train[:len(x_train)]
    x_test = x_test.dropna()

    print("len of train: ",len(x_train))
    print("len of test:", len(x_test))

    # 2.- Create Randomforest object usinig a max depth=5
    regressor = RandomForestRegressor(n_estimators=200, max_depth=5 )

    # 3.- Train data
    clf=regressor.fit(x_train, y_train)

    # Generate a timestamp to create a unique blob name
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # 4.- Save the trained model to storage using joblib
    model_filename = str(timestamp) +'_random_forest_model.pkl'
    joblib.dump(clf, model_filename)

    y_pred = regressor.predict(x_test)
    y_pred = pd.DataFrame(y_pred)

    print("mean_squared_error: ",mean_squared_error(y_train,regressor.predict(x_train)))

    return(model_filename)

