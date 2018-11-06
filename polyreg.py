import numpy as np
from numpy.linalg import qr, inv, matrix_rank



def polyreg(data_x, data_y, weights = [], degree = 1, monomial = False):
    """
    type(data_x): pandas dataframe
    type(data_y): pandas dataframe
    type(weights): list of weights
    type(degree): int
    type(monomial): bool
    
    returns dict of fitted vals, coefs and few more para
    """
    data_x = polybasis(data_x, degree, monomial)
    row,col = data_x.shape
    x_col = data_x.columns
    x = np.asarray(data_x)
    
#     y_col = data_y.columns
    y = np.asarray(data_y)
    
    if len(weights) == row:
        if any([True for ele in weights if ele<=0]):
            print("Only positive weights")
        
        weights = [ele**0.5 for ele in weights]
        y = np.multiply(y,np.reshape(np.array(weights),(row,1)))
        x = np.multiply(x,np.reshape(np.array(weights),(row,1)))
    
    q, r = qr(x)
    rank_r = matrix_rank(r)
    if rank_r < col:
        print("Didn't handle this case yet")
        ##inverse would not be possible
        ##gives error: LinAlgError: Incompatible dimensions :: but not in R
        
    coef = np.dot(np.dot(inv(r), q.T), y) # betas: R^-1 Q^T y
    fitted = np.dot(x, coef)
    if len(weights) == row:
        fitted = fitted/w
        
    return {'fitted': fitted,
           'coefficients': coef,
           'degree': degree,
           'monomial': monomial,
           'df': rank_r}
        