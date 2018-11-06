from sklearn.metrics import confusion_matrix
def predict_fda(fda_object):

    lambd = fda_object['values']
    alpha = np.sqrt(lambd)
    sgima = np.sqrt(1-lambd)
    new_data = np.matmul(fda_object['fit']['fitted'],fda_object['theta_mod'])/(sgima*alpha)
    prior = 2*np.log(fda_object['prior'])

    dist_mat = np.zeros((150,3))
    dim = 3
    for i in range(dim):
        dist_mat[:,i] = np.sqrt(np.sum((new_data - fda_object['means'][i,])**2,axis=1))

    pclass = np.argmin(dist_mat,axis=1)
    
    return (confusion_matrix(pclass, np.array(data_y)), pclass)