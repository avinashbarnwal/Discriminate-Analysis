import numpy as np

def contr_fda(p,contrasts_):
    """
    type(p): numpy array
    type(contrasts_): numpy array of helmert contrasts
    returns np array
    """
    dim = len(p)
    sqp = np.sqrt(p/np.sum(p))
    x = np.append(np.array([[1]*dim]).T,contrasts_,1)*sqp
    tmp_y = np.append(np.zeros((1,dim-1)),np.identity(dim-1),0)
    tmp_deno = np.array([sqp]*(dim-1)).T
    
    return np.dot(qr(x)[0],tmp_y)/tmp_deno