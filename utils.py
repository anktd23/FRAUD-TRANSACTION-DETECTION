from logger import logging 
from exception import ProjException
import sys
def median(lst:list):
    """
    This method returns median of transactions from single user.
    `================================================================
    input_params -> data:dict, user_id:str
    output-> mode transaction of single user:float
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
        