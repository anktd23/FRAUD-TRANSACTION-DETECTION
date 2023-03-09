import math   
def euclidean_distance(trans1, trans2)->float:
    """
    This method calculated the euclidean distance between two points.
    `===========================================================================================
    input_params -> pt1,pt2  with x,y co-ordinates :str
    outputs -> euclidean dist:float
    ============================================================================================
    """
    try:
        x1 = float(trans1['x_cord_trans'])
        y1 = float(trans1['y_cord_trans'])
        x2 = float(trans2['x_cord_trans'])
        y2 = float(trans2['y_cord_trans'])
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    except Exception as e:
        raise e

def euclidean_dist_same(data,user_id,transaction_id1,transaction_id2):
    """
    This method calculate the euclidean distance between two transaction for same user.
    `================================================================================================
    input_params-> user_id,transaction_id1,transaction_id2:str
    output -> euclidean distance:float
    =================================================================================================
    """
    try:
        transactions = data.get(user_id, [])
        trans1, trans2 = None, None
        for trans in transactions:
            if trans['transaction_id'] == transaction_id1:
                trans1 = trans
            elif trans['transaction_id'] == transaction_id2:
                trans2 = trans
                break
        if trans1 and trans2:
            distance = round(euclidean_distance(trans1, trans2),2)
            return distance
        else:
            return "One or both of the transactions not found."
    except Exception as e:
        raise e
    
def euclidean_dist_diff(data,user_id_1,user_id_2,transaction_id1,transaction_id2):
    """
    This method calculate the euclidean distance between two transaction for diff user.
    `=============================================================================================
    input_params-> user_id1,user_id2,transaction_id1,transaction_id2:str
    output -> euclidean distance:float
    ==============================================================================================
    """
    try:
        transactions1 = data.get(user_id_1, [])
        transactions2 = data.get(user_id_2, [])
        trans1, trans2 = None, None
        for trans in transactions1:
            if trans['transaction_id'] == transaction_id1:
                trans1 = trans
                break
        for trans in transactions2:
            if trans['transaction_id'] == transaction_id2:
                trans2 = trans
                break
        if trans1 and trans2:
            distance = round(euclidean_distance(trans1, trans2),2)
            return distance
        else:
            return "One or both of the transactions not found."
    except Exception as e:
        raise e
