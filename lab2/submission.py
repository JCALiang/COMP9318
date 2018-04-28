## import modules here 
import pandas as pd
import numpy as np


################# Question 1 #################

# helper functions
def project_data(df, d):
    # Return only the d-th column of INPUT
    return df.iloc[:, d]

def select_data(df, d, val):
    # SELECT * FROM INPUT WHERE input.d = val
    col_name = df.columns[d]
    return df[df[col_name] == val]

def remove_first_dim(df):
    # Remove the first dim of the input
    return df.iloc[:, 1:]

def slice_data_dim0(df, v):
    # syntactic sugar to get R_{ALL} in a less verbose way
    df_temp = select_data(df, 0, v)
    return remove_first_dim(df_temp)

def buc_rec(df, pre, init):# do not change the heading of the function
    dims = df.shape[1]
    
    if dims == 1:
        # only the measure dim
        isum = sum( project_data(df, -1) )
        pre.append(isum)
        init.loc[len(init)] = pre

    else:
        # the general case
        dim0_vals = set(project_data(df, 0).values)
        t1=pre[:]
        for dim0_v in dim0_vals:
            sub_data = slice_data_dim0(df, dim0_v)
            t2=t1[:]
            t2.append(dim0_v)
            buc_rec(sub_data, t2, init)
        ## for R_{ALL}

        sub_data = remove_first_dim(df)
        t3=t1[:]
        t3.append('ALL')
        buc_rec(sub_data, t3, init)
    


def buc_rec_optimized(df):  # do not change the heading of the function
	if df.shape[0] == 1:
		df_final = single(df)
	else:
		df_final=pd.DataFrame(columns=list(df))
		buc_rec(df, [], df_final)
	return df_final
        
        
def single(df):
    all_row=[]
    enulist=[]
    single_tuple=df.iloc[0]
    for i in single_tuple:
        enulist.append(i)
    enulist=[enulist]
    
    for i, oli in enumerate(enulist):
        row=oli[:-1]
        if oli not in all_row:
            all_row.append(oli)

        for i2 in range(len(row)):
            new_row=oli[:]
            if new_row[i2]!="ALL":
                new_row[i2]="ALL"
                if new_row not in enulist:
                    enulist.append(new_row)
    
    result = pd.DataFrame(data=all_row, columns=list(df))
    return result 

################# Question 2 #################

def v_opt_dp(x, num_bins):# do not change the heading of the function
    opt=[[-1 for x in range(len(x))] for y in range(num_bins)]
    opt_index=[[-1 for x in range(len(x))] for y in range(num_bins)]
    global full_list, full_bin
    full_list=x
    full_bin= num_bins

    v_opt_rec(0, num_bins-1, opt, opt_index)
    
    #reassemble the index
    binning=[]
    index=0
    for i in range(num_bins-1, 0, -1):
        bins=full_list[index:opt_index[i][index]]
        binning.append(bins)
        index=opt_index[i][index]
    last_bin= full_list[index:]
    binning.append(last_bin)

    return opt, binning


def sse(arr):
    if len(arr) == 0: # deal with arr == []
        return 0.0
    avg = np.average(arr)
    val = sum( [(x-avg)*(x-avg) for x in arr] )
    return val

def v_opt_rec(xx, b, opt, opt_index):
    global full_list, full_bin
    if (full_bin - b - xx < 2) and (len(full_list) - xx > b):
        v_opt_rec(xx+1, b, opt, opt_index)
        if(b == 0):
            opt[b][xx] = sse(full_list[xx:])
            return 

        v_opt_rec(xx, b-1, opt, opt_index)  

        min_cost = 100000000000
        min_pos=-1
        for i in range(xx+1, len(full_list)):
            cost= opt[b-1][i] +  sse(full_list[xx:i])
            if cost<min_cost:
                min_cost=cost
                min_pos=i                   

        opt[b][xx] = min_cost
        opt_index[b][xx]=min_pos
