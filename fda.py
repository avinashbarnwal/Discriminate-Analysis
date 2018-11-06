from numpy.linalg import svd

def fda(df_x,df_y):
    """
    type(df_x): pandas dataframe
    type(df_y): pandas dataframe
    """
    x_dim,y_dim = df_x.shape
    t=Helmert()
    theta = t.code_without_intercept(levels = np.unique(df_y)).matrix
    prior = np.array([1/3]*3)
    
    theta = contr_fda(prior,theta)
    
    level_counts = df_y[df_y.columns[0]].value_counts().sort_index()
    lvl_count = 0
    i=0
    Theta = np.empty((df_y.shape[0],level_counts.shape[0]-1))
    for item in level_counts:
        Theta[lvl_count:lvl_count+item] = theta[level_counts.index[i]]
        i+=1
        lvl_count+=item
    
    fit =  polyreg(df_x,Theta)
    ssm = np.matmul(Theta.T, (fit['fitted']/x_dim))
    thetan, lambd, _ = svd(ssm)
    
    discr_eigen = lambd/(1-lambd)
    pe = 100*np.cumsum(discr_eigen)/np.sum(discr_eigen)
    
    ##not yet implemented
#     dimension = lambd.size
    dimension = 3
    alpha = np.sqrt(lambd)
    sgima = np.sqrt(1-lambd)
    means = np.matmul(theta, thetan)/(sgima/alpha)
    obj = {
        "percent_explained": pe,
        'values' : lambd,
        'means' : means,
        'theta_mod' : thetan,
        'dimension' : dimension,
        'prior' : prior,
        'fit': fit
    }
    confusion, predictions = predict_fda(obj)
    obj['confusion_matrix'] = confusion
    obj['predicted_class'] = predictions
    return obj
    
    
    
    