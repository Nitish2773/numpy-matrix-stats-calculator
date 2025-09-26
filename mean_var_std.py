import numpy as np 

def calculate(list_nums):
    if len(list_nums)<9:
        raise ValueError('List must contain at least nine numbers.')
    np_arrays=np.array(list_nums).reshape(3,3)
    calcuations={
        'mean':[np.mean(np_arrays,axis=0).tolist(),np.mean(np_arrays,axis=1).tolist(),np.mean(np_arrays)],
        'variance':[np.var(np_arrays,axis=0).tolist(),np.var(np_arrays,axis=1).tolist(),np.var(np_arrays)],
        'standard deviation':[np.std(np_arrays,axis=0).tolist(),np.std(np_arrays,axis=1).tolist(),np.std(np_arrays)],
        'max':[np.max(np_arrays,axis=0).tolist(),np.max(np_arrays,axis=1).tolist(),np.max(np_arrays)],
        'min':[np.min(np_arrays,axis=0).tolist(),np.min(np_arrays,axis=1).tolist(),np.min(np_arrays)],
        'sum':[np.sum(np_arrays,axis=0).tolist(),np.sum(np_arrays,axis=1).tolist(),np.sum(np_arrays)]
    }

    return calcuations