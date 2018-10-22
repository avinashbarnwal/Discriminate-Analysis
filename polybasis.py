import numpy as np
import pandas as pd

def polybasis(data, degree=1, monomial = False):
    """
    type(x): pandas dataframe
    type(degree): int
    type(monomial): Bool
    
    returns: polybasis of x as pandas dataframe
    """
    col_names = data.columns
    x = np.asarray(data)
    row,col = data.shape
    
    if degree >= 3:
        print("This is not a smart polynomial routine.\
        You may get numerical problems with a degree of 3 or more")
    
    if col==1:
        monomial = True
    if degree > 1:
        if monomial:
            ini_data = data
            tmp_data = ini_data
            cc = ['1']
            for _ in range(1,degree):
                tmp_data*=ini_data
                x = np.concatenate((x,tmp_data),axis=1)
                cc.append(str(_+1))
        else:
            matarray = np.repeat(x[:,:,np.newaxis], degree, axis=2)
            for _ in range(1,degree):
                matarray[:, :, _] =np.power(x,_+1) 
            matarray = np.transpose(matarray,(0,2,1))
            
            x = matarray[:, :, col-1 ]
            
            ad0 = list(range(1,degree+1))
            ad = ad0
            ncol_mat0 = degree
            ncol_x = degree
            d0 = [str(item) for item in ad0]
            cc = d0

            for _ in range(col-2,-1,-1):
                index0 = list(range(1,ncol_mat0+1))*ncol_x
                index = [item for item in range(1,ncol_x+1) for _ in range(ncol_mat0)]
                newad = [ad0[index0[i]-1]+ad[index[i]-1] for i in range(len(index0))]
                retain = [ True if newad[i]<=degree else False for i in range(len(newad))]
                
                mat0 = matarray[:, :, _]
                tmp_index0 = [index0[i]-1 for i in range(len(index0)) if retain[i]]
                tmp_index = [index[i]-1 for i in range(len(index)) if retain[i]]
                if any(retain):
                    newmat = np.multiply(mat0[:, tmp_index0 ], x[:,tmp_index])
                

                ddn = [ele+val for ele,val in zip([d0[ele] for ele in tmp_index0],\
                                                 [cc[ele] for ele in tmp_index])]        
                zeros = '0'*sum(retain)
                cc = ['0'+ele for ele in cc]
                d00 = [ele+zeros for ele in d0]
                x = np.concatenate((mat0,x,newmat), axis=1)
                cc = d00+cc+ddn
                ad = ad0+ad+ [newad[i] for i in range(len(newad)) if retain[i]]
                ncol_x = len(ad)
#             if dn:
    col_names = cc
    
    data = pd.DataFrame(x,columns=col_names)
    data['intercept'] = 1

    
    return data