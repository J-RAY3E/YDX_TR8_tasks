import numpy as np



def calculate_correlation_matrix(X, Y=None):
    if Y is not None:
        cov_xy = np.cov(X,Y,rowvar= False, ddof= 1)
        cov_xy = cov_xy[:X.shape[1], X.shape[1]:]  
        stdx = np.std(X, axis=0, ddof= 1) 
        stdy = np.std(Y, axis=0, ddof= 1) 
        return cov_xy/ (np.outer(stdx,stdy))

    else:
        stdx = np.std(X,axis=0,ddof=1)
    return np.cov(X,rowvar=False) / np.outer(stdx,stdx)

print(calculate_correlation_matrix(np.array([[1, 2, 3], [7, 15, 6], [7, 8, 9]])))