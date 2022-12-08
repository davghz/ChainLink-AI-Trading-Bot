from sklearn.model_selection import cross_val_score

Evaluate the performance of the trained models using cross-validation
linear_reg_scores = cross_val_score(linear_reg, X, y, cv=10)
svr_scores = cross_val_score(svr_gs, X, y, cv=10)
rf_scores = cross_val_score(rf_gs, X, y, cv=10)

Print the mean and standard deviation of the scores for each model
print("Linear regression model scores: Mean = %.3f, Std = %.3f" % (linear_reg_scores.mean(), linear_reg_scores.std()))
print("SVR model scores: Mean = %.3f, Std = %.3f" % (svr_scores.mean(), svr_scores.std()))
print("Random forest model scores: Mean = %.3f, Std = %.3f" % (rf_scores.mean(), rf_scores.std()))

Select the best performing model based on cross-validation scores
if linear_reg_scores.mean() > svr_scores.mean() and linear_reg_scores.mean() > rf_scores.mean():
best_model = linear_reg
elif svr_scores.mean() > linear_reg_scores.mean() and svr_scores.mean() > rf_scores.mean():
best_model = svr_gs
else:
best_model = rf_gs

Use the best model to make predictions on new data
new_data = <code to access new data>
predictions = best_model.predict(new_data)
