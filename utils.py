from logger import logging 
from exception import ProjException
import sys
def median(lst:list):
    """
    This method returns median of transactions from single user.
    `================================================================
    input_params -> lst:list
    output-> median:float
    ================================================================
    """ 
    try:

        lst1=[]
        #if length is odd
        if len(lst) % 2 != 0:
            index_pos = int((len(lst)+1)/2)
            lst1.append(index_pos-1)
            median_trans_amt = [lst[i] for i in lst1]
            return median_trans_amt[0]
        #if length is even
        else:
            index_pos1 = int((len(lst)/2)-1)
            index_pos2 = int(((len(lst)/2)+1)-1)
            lst1.insert(0,index_pos1)
            lst1.insert(1,index_pos2)
            idx_element = [lst[i] for i in lst1]
            sum_element = 0
            for i in idx_element:
                sum_element = sum_element + i
            median_trans_amt = round(sum_element/2,2)
            return median_trans_amt
    except Exception as e:
        raise ProjException(e,sys)
    
def mean(lst):
    """
    This method returns mean of transactions.`
    `===============================================================
    input_params -> lst:list
    output-> mean:float
    ===============================================================
    """
    try:
        mean_val =sum(lst)/len(lst)
        return mean_val
    except Exception as e:
        raise ProjException(e,sys)

def dict_retrieve_(file):
        """
    This method coverts .txt file to dict where key is transaction_id
    `========================================================================
    input_params -> .txt file
    output-> dict where key is transaction_id
    =========================================================================
    """
        try:
            with open(file) as f:
                data = f.read().strip().split('\n')
            keys = ['user_id','transaction_id','transaction_desc','transaction_amt','x_cord_trans','y_cord_trans','status']
            d = {}
            for row in data:
                values = row.split(":")
                transaction_id = values[1]
                if transaction_id in d:
                    d[transaction_id].append(dict(zip(keys,values)))
                else:
                    d[transaction_id] = [dict(zip(keys,values))]
            return d
        except Exception as e:
            raise ProjException(e,sys)