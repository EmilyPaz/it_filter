import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

def train_test_dfs():
    main_df = pd.read_csv('data/processed_df.csv')

    non_null_salary = main_df.dropna(subset=['salary'])
    non_null_salary_df = non_null_salary.to_csv('data/filtered_df.csv', index=False)

    null_salary = main_df[main_df['salary'].isna()]
    null_salary.drop(columns='salary', inplace=True)
    null_salary_df = null_salary.to_csv('data/salary_test.csv', index=False)

    return non_null_salary_df, null_salary_df

def predict_salaries():
    salaries = pd.read_csv('data/filtered_df.csv')
    predict = pd.read_csv('data/salary_test.csv')

    TARGET = 'salary'
    CAT_FEATS = ['stack', 'profile', 'level']
    NUM_FEATS = ['experience']
    FEATURES = NUM_FEATS + CAT_FEATS

    numerical_transformer = Pipeline(steps=[('imputer', SimpleImputer()),
                                            ('scaler', RobustScaler())])
    categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                                              ('encoder', OrdinalEncoder(handle_unknown='ignore'))])
    preprocessor = ColumnTransformer(transformers=[('numerical_preprocessor', numerical_transformer, NUM_FEATS),
                                                   ('categorical_preprocessor', categorical_transformer, CAT_FEATS)])
    preprocessor.fit_transform(salaries[FEATURES])

    salaries_train, salaries_test = train_test_split(salaries)

    model = Pipeline(steps=[('preprocessor', preprocessor),
                            ('regressor', RandomForestRegressor(n_jobs=-1))])

    X_train = salaries_train[FEATURES]
    y_train = salaries_train[TARGET]

    model.fit(X_train, y_train);

    X_test = salaries_test[FEATURES]
    y_test = salaries_test[TARGET]

    y_test_predict = model.predict(X_test)
    mean_squared_error(y_true=y_test, y_pred=y_test_predict, squared=False)

    X = salaries[FEATURES]
    y = salaries[TARGET]
    cross_val_score(model, X, y, scoring='neg_root_mean_squared_error', cv=4, n_jobs=-1).mean()

    model.predict(predict[FEATURES])

    parameter_grid = {'regressor__max_depth': [2, 4, 6, 8, 11, 16, 20, 24, 28, 32],
                      'regressor__n_estimators': [16, 32, 64, 128, 256, 512],
                      'preprocessor__numerical_preprocessor__imputer__strategy': ['mean', 'median']}
    grid_search = RandomizedSearchCV(model, parameter_grid, cv=5, scoring='neg_root_mean_squared_error', n_jobs=-1,
                                     n_iter=32)

    grid_search.fit(X, y);

    prediction = grid_search.predict(predict[FEATURES])
    predict['salary'] = prediction


    predict_df = predict.to_csv('data/predicted_salaries.csv', index=False)

    return predict_df


def concat_dfs():
    prediction_df = pd.read_csv('data/predicted_salaries.csv')
    filtered_df = pd.read_csv('data/filtered_df.csv')

    cols = filtered_df.columns.to_list()

    prediction_df = prediction_df[cols]

    complete_df = pd.concat([prediction_df, filtered_df], ignore_index=True)

    complete_df.salary = complete_df.salary.round(2)

    return complete_df.to_csv('results/complete_df.csv', index=False)

def analysis():
    train_test_dfs()
    predict_salaries()
    concat_dfs()

