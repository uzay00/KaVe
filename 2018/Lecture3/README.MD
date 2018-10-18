
## Titanic Dataset
 - https://www.dataquest.io/blog/kaggle-fundamentals/
 
## Basic Statistics in Python
 - https://www.dataquest.io/blog/basic-statistics-in-python-probability/

## Polynomial Regression
 - https://medium.com/coinmonks/polynomial-regression-11bec9262d64
 
 
### Notes

> Note: Why use df.iloc [:,0:1] instead of simple df.iloc[:,0] the reason is than when we use df.iloc[:,0] is creates a 1D array which cannot be fitted into the polynomial model like [1,2,3,4,…n] . We need a 2D array to fit_transform() the X_axis data thus using df.iloc[:,0:1] creates a 2D matrix [[1,2,3,4,…n]].
 
 
