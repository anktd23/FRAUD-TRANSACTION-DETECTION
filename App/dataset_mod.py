import sys

def dict_retrieve(file)-> dict:
    """
    This function coverts text file to dict.
    ===========================================================================
    input_params -> .txt file
    output-> dict where key is user_id
    ===========================================================================
    """
    try:
        with open(file) as f:
            data = f.read().strip().split('\n')
        keys = ['user_id','transaction_id','transaction_desc','transaction_amt','x_cord_trans','y_cord_trans','status']
        d = {}
        for row in data:
            values = row.split(":")
            user_id = values[0]
            if user_id in d:
                d[user_id].append(dict(zip(keys,values)))
            else:
                d[user_id] = [dict(zip(keys,values))]
        return d
        
    except Exception as e:
        raise e
    