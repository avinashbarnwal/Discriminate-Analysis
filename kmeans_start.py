def kmeans_start(x,y,subclasses):
    
    labels            = np.unique(y)
    J                 = len(labels)
    #g                  as.numeric(g)
    weights           =  labels
    #names(weights)    <- cnames
    subclasses        = np.repeat(subclasses,J)
    

    R                 = sum(subclasses)
    cl                = np.repeat(np.arange(J), subclasses)
    cx                = x[seq(R), , drop = FALSE]
    for (j in seq(J)) {
        nc <- subclasses[j]
        which <- cl == j
        xx <- x[g == j, , drop = FALSE]
        if ((nc <= 1) || (nrow(xx) <= nc)) {
            cx[which, ] <- apply(xx, 2, mean)
            wmj <- matrix(1, sum(g == j), 1)
        }
        else {
###            start <- xx[sample(1:nrow(xx), size = nc), ]
          start=nc
          TT <- kmeans(xx, start)
            cx[which, ] <- TT$centers
            wmj <- diag(nc)[TT$cluster, ]
        }
        dimnames(wmj) <-
            list(NULL, paste("s", seq(dim(wmj)[2]), sep = ""))
        weights[[j]] <- wmj
    }
    list(x = cx, cl = factor(cl, labels = cnames), weights = weights)
}

