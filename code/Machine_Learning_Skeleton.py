# Load packages
from mysql.connector import connection
from sqlalchemy import create_engine
import pandas as pd

# Database connection info
dsn_database = "property" #'demographic' or 'property'
dsn_hostname = "georgetownanalyticscapstone.c50pz9jksixq.us-east-1.rds.amazonaws.com"
dsn_port = 3306
dsn_uid = "sanemkabaca"
dsn_pwd = "georgetowndmv"


# Make connection to database
db_connection = connection.MySQLConnection(user=dsn_uid, password=dsn_pwd,
                                 host=dsn_hostname,
                                 database=dsn_database)
# Make query
query = ("""SELECT * FROM full_dataset""")

# Read data from query
df_original = pd.read_sql(query, con=db_connection)

del(dsn_database, dsn_hostname, dsn_port, dsn_pwd, dsn_uid, query)

###############################################################################
#                               ML Skeleton                                   #
###############################################################################

# Import packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression, LassoCV, RidgeCV, ElasticNetCV, SGDRegressor
from sklearn.svm import LinearSVR, NuSVR, SVR
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, BaggingRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from yellowbrick.regressor import PredictionError, ResidualsPlot, AlphaSelection


# Average rent and average sq ft column
df_original["rent"] = (df_original.minrent + df_original.maxrent)/2
df_original["sqft"] = (df_original.minsqft + df_original.maxsqft)/2

# Get target
y = df_original.rent

# Columns to remove
Columns_To_Remove = ["unit_id", "pid", "property_name", "zip_code", "property_type", "metro_distance", "commuter_distance", 
                     "parent_company_name", "num_units", "year_built", "num_stories", "zip", "minrent", "maxrent", "minsqft", "maxsqft",
                     "rent"]
cols = [col for col in df_original.columns if col not in Columns_To_Remove]
df_for_ml = df_original[cols]
del(Columns_To_Remove, cols)

# Train - Test - Split
X_train, X_test, y_train, y_test = train_test_split(df_for_ml, y, test_size=0.33, random_state=42)

# For now...
X_train = X_train[["property_amenities_dogs", "property_amenities_cats"]]
y_train[pd.isnull(y_train)] = 0
X_test = X_test[["property_amenities_dogs", "property_amenities_cats"]]
y_test[pd.isnull(y_test)] = 0

###############################################################################
#                              Linear Models                                  #
###############################################################################

#########################
#   Linear Regression   #
#########################

# Fit Model
LinRegr = LinearRegression()
LinRegr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(LinRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(LinRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

#########################
#   Lasso Regression    #
#########################

# Fit Model
LassoRegr = LassoCV()
LassoRegr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(LassoRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(LassoRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

# Visualization 3 - Selecting Alpha for Regularization
# Create a list of alphas to cross-validate against
alphas = np.logspace(-12, -0.5, 400)

# Instantiate the linear model and visualizer
LassoRegr = LassoCV(alphas=alphas)
visualizer = AlphaSelection(LassoRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
g = visualizer.poof()             # Draw/show/poof the data

#########################
#   Ridge Regression    #
#########################

# Fit Model
RidgeRegr = RidgeCV()
RidgeRegr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(RidgeRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(RidgeRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

# Visualization 3 - Selecting Alpha for Regularization
# Create a list of alphas to cross-validate against
alphas = np.logspace(-12, -0.5, 400)

# Instantiate the linear model and visualizer
RidgeRegr = RidgeCV(alphas=alphas)
visualizer = AlphaSelection(RidgeRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
g = visualizer.poof()             # Draw/show/poof the data

#########################
# ElasticNet Regression #
#########################

# Fit Model
ElastNet = ElasticNetCV()
ElastNet.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(ElastNet)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(ElastNet)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   


#########################
#     SGD Regression    #
#########################

# Fit Model
SGDRegr = SGDRegressor()
SGDRegr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(SGDRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(SGDRegr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

###############################################################################
#                              SVM Models                                     #
###############################################################################

#########################
#     Linear SVRn       #     
#########################
from sklearn.model_selection import cross_val_score
# Fit Model
LinSVR = LinearSVR()
LinSVR.fit(X_train, y_train)

scores = cross_val_score(LinSVR, X_train, y_train, cv=12)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(LinSVR)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(LinSVR)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

#########################
#        Nu SVR         #
#########################

# Fit Model
Nu_SVR = NuSVR()
Nu_SVR.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(Nu_SVR)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(Nu_SVR)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

#########################
#     SVR Regression    #
#########################

# Fit Model
SVR_Regr = SVR()
SVR_Regr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(SVR_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(SVR_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   


###############################################################################
#                              Ensemble Models                                #
###############################################################################

#########################
#     Random Forest     #
#########################

# Fit Model
RF = RandomForestRegressor()
RF.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(RF)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(RF)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

#########################
#       ADA Boost       #
#########################

# Fit Model
ADA_Regr =  AdaBoostRegressor()
ADA_Regr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(ADA_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(ADA_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

#########################
#  Bagging Regression   #
#########################

# Fit Model
Bag_Regr = BaggingRegressor()
Bag_Regr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(Bag_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(Bag_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

#########################
#     Extra Trees       #
#########################

# Fit Model
XtraTrees = ExtraTreesRegressor()
XtraTrees.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(XtraTrees)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(XtraTrees)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   

#########################
#   Gradient Boosting   #
#########################
# Fit Model
GradBoost_Regr = GradientBoostingRegressor()
GradBoost_Regr.fit(X_train, y_train)

# Visualization 1 - Residual Plot
visualizer = ResidualsPlot(GradBoost_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof() 

# Visualization 2 - Prediction Error Plot
visualizer = PredictionError(GradBoost_Regr)

visualizer.fit(X_train, y_train)  # Fit the training data to the visualizer
visualizer.score(X_test, y_test)  # Evaluate the model on the test data
g = visualizer.poof()   


###############################################################################
#                         Cross Validation Code                               #
###############################################################################
from sklearn.model_selection import KFold, cross_val_score
kf = KFold(n_splits=12)
kf.get_n_splits(df_for_ml)

for train_index, test_index in kf.split(df_for_ml):
    print("TRAIN:", train_index, "TEST:", test_index)
    #X_train, X_test = df_for_ml[train_index], df_for_ml[test_index]
    #y_train, y_test = y[train_index], y[test_index]

cross_val_score(model, data_input, data_output, cv = 12)







