#from sklearn import datasets
#iris = datasets.load_iris()
#X = iris.data
#y = iris.target
#target_names = iris.target_names
#X.shape = (150, 4)
#y.shape = (150,1)
#Number of Subclasses = 3

from sklearn.cluster import KMeans

def kmeans_start(x,y,subclasses):
    #For reference consider
    #x - Input , y - Dependent , Subclasses - count of classes
    #Example iris datasets
    labels            = np.unique(y)
    J                 = len(labels)
    weights           = {}
    subclasses        = np.repeat(subclasses,J)
    #array([3, 3, 3])
    R                 = sum(subclasses)
    #9
    cl                = np.repeat(np.arange(J), subclasses)
    #array([0, 0, 0, 1, 1, 1, 2, 2, 2])
    cx                = x[0:R]
    #dim cx = [9,]
    
    for j in range(J):
        
        nc    = subclasses[j]
        which = cl == j
        xx    = x[y == j,]
        
        if (nc <= 1) | (xx.shape[0] <= nc):
            cx[which,] = xx.mean(axis=1)
            #Important calculate the column mean for numpy array
            wmj        = np.ones((sum(y == j), 1))
        else :
            ### start <- xx[sample(1:nrow(xx), size = nc), ]
            start       = nc
            TT          = KMeans(n_clusters=start, random_state=0).fit(xx)
            cx[which, ] = TT.cluster_centers_
        
            wmj = np.zeros((sum(y == j), nc))
            wmj[np.arange(sum(y == j)), TT.labels_] = 1

            #wmj         = np.zeros((nc,nc))
            #np.fill_diagonal(wmj, TT.labels_)
        
        #dimnames(wmj)   = list(NULL, paste("s", seq(dim(wmj)[2]), sep = ""))
        weights[j]      = wmj
        
    return {'x':cx,'cl':cl,'weights': weights}



