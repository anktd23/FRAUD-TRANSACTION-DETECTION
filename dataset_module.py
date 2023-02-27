import sys
from logger import logging
from exception import ProjException

file = 'Transaction.txt'

def dict_retrieve(file:file)-> dict:
    """
    This function coverts text file to dict.
    ===========================================================================
    input_params -> .txt file
    output-> dict
    ===========================================================================
    """
    try:
        logging.info(f"{'~'*15}Reading text file {'~'*15}")
        with open(file) as f:
            data = f.read().strip().split('\n')
        logging.info(f"Rows in {file} : {data[0:2]}")
        logging.info(f"converting text file to dict")
        keys = ['user_id','transaction_id','transaction_desc','transaction_amt','x_cord_trans','y_cord_trans','status']
        logging.info(f"assigning keynames {keys}")
        d = {}
        for row in data:
            values = row.split(":")
            user_id = values[0]
            if user_id in d:
                d[user_id].append(dict(zip(keys,values)))
            else:
                d[user_id] = [dict(zip(keys,values))]
        logging.info(f"dict - {d['21'][0]} \n")
        return d
        
    except Exception as e:
        raise ProjException(e,sys)
    
#dict_retrieve(file)