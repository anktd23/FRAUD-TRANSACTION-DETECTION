import sys
from utils import median,mean,dict_retrieve_,standard_dev,iqr,tran_lst,tran_lst_all


def avg_trans(data,user_id):
        """
        This method returns average of transactions from single user.`
        `===============================================================
        input_params -> user_id:str,data:dict
        output-> average transaction of single user:float
        ===============================================================
        """
        try:
            transaction = data.get(user_id,[])
            total_amt = 0
            count = 0
            for dic in transaction:
                dic['transaction_amt'] = float(dic['transaction_amt'])
                total_amt = total_amt + dic['transaction_amt']
                count+=1
                avg_trans_amt = round(total_amt/count,2)
            return avg_trans_amt
        except Exception as e:
             raise e
        
def avg_trans_all(data): 
    """
    This method returns average of transactions from all users.
    `==============================================================
    input_params -> data:dict
    output-> average transaction of all user:float
    ==============================================================
    """ 
    try:
        total_amt_all = 0
        count_all = 0
        for key in data.values():
            total_amt = 0
            count = 0
            for key1 in key:
                key1['transaction_amt'] = float(key1['transaction_amt'])
                total_amt = total_amt + key1['transaction_amt']
                count+=1
            total_amt_all = total_amt_all + total_amt
            count_all=count_all + count
            avg_trans_amt = round(total_amt_all/count_all,2)
        return avg_trans_amt
    except Exception as e:
        raise e
    
def mode_trans(data,user_id):
        """
        This method returns mode of transactions from all users.
        `=============================================================
        input_params -> data:dict, user_id:str
        output-> mode transaction of single user:float
        =============================================================
        """ 
        try:
            tran_amt = tran_lst(data,user_id)
            freq_dict = {}
            for num in tran_amt:
                if num in freq_dict:
                    freq_dict[num] += 1
                else:
                    freq_dict[num] = 1
            max_freq = max(freq_dict.values())
            mode_trans_amt = [key for key, value in freq_dict.items() if value == max_freq]
            if max_freq<2:
                return "No transaction repeated"
            else:
                return mode_trans_amt
        except Exception as e:
            raise e
def mode_trans_all(data) :
    """
    This method returns mode of transactions from all users.
    `================================================================
    input_params -> data:dict
    output-> mode transaction of all users:float
    ================================================================
    """ 
    try:
        tran_amt_all = tran_lst_all(data)
        freq_dict = {}
        for num in tran_amt_all:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        max_freq =max(freq_dict.values())
        mode_trans_amt = [key for key, value in freq_dict.items() if value == max_freq]

        if max_freq<2:
            return None
        else:
            return mode_trans_amt
    except Exception as e:
        raise e
    
def median_trans(data,user_id):
    """
    This method returns median of transactions from single user.
    `================================================================
    input_params -> data:dict, user_id:str
    output-> median transaction of single user:float
    ================================================================
    """ 
    try:
        tran_amt = tran_lst(data,user_id)
        lst1=[]
        #if length is odd
        if len(tran_amt) % 2 != 0:
            index_pos = int((len(tran_amt)+1)/2)
            lst1.append(index_pos-1)
            median_trans_amt = [tran_amt[i] for i in lst1]
            return median_trans_amt[0]
        #if length is even
        else:
            index_pos1 = int((len(tran_amt)/2)-1)
            index_pos2 = int(((len(tran_amt)/2)+1)-1)
            lst1.insert(0,index_pos1)
            lst1.insert(1,index_pos2)
            idx_element = [tran_amt[i] for i in lst1]
            sum_element = 0
            for i in idx_element:
                sum_element = sum_element + i
            median_trans_amt = round(sum_element/2,2)
            return median_trans_amt
    except Exception as e:
        raise e
    
def median_trans_all(data):
    """
    This method returns median of transactions for all users.
    `================================================================
    input_params -> data:dict
    output-> median transaction of all user:float
    ================================================================
    """ 
    try:
        tran_amt_all = tran_lst_all(data)
        lst1=[]
        #if length is odd
        if len(tran_amt_all) % 2 != 0:
            index_pos = int((len(tran_amt_all)+1)/2)
            lst1.append(index_pos-1)
            median_trans_amt = [tran_amt_all[i] for i in lst1]
        #if length is even
        else:
            index_pos1 = int((len(tran_amt_all)/2)-1)
            index_pos2 = int(((len(tran_amt_all)/2)+1)-1)
            lst1.insert(0,index_pos1)
            lst1.insert(1,index_pos2)
            idx_element = [tran_amt_all[i] for i in lst1]
            sum_element = 0
            for i in idx_element:
                sum_element = sum_element + i
            median_trans_amt = round(sum_element/2, 2)
            return median_trans_amt
    except Exception as e:
        raise e

def iqr_trans(data,user_id):
    """
    This method returns IQR 
    `====================================================================================
    input_params -> data:dict, user_id=str
    ouput -> iqr:float
    =====================================================================================
    """
    try:
        tran_amt = tran_lst(data,user_id)
        n = len(tran_amt)
        lst_q1 = tran_amt[:n//2]
        lst_q2 = tran_amt[n//2:]
        #if length is even
        if n % 2 == 0:
            q1 = median(lst=lst_q1)
            q3 = median(lst=lst_q2)
        #if length is odd
        else:
            q1 = median(lst_q1)
            q3 = median(lst_q2)
        iqr = round((float(q3) - float(q1)),2)
        return iqr
    except Exception as e:
        raise e
    
def iqr_trans_all(data):
    """
    This method returns IQR for all users
    `====================================================================================
    input_params -> data:dict
    ouput -> iqr:float
    =====================================================================================
    """
    try:
        tran_amt_all = tran_lst_all(data)
        n = len(tran_amt_all)
        lst_q1 = tran_amt_all[:n//2]
        lst_q2 = tran_amt_all[n//2:]
        #if length is even
        if n % 2 == 0:
            q1 = median(lst=lst_q1)
            q3 = median(lst=lst_q2)
        #if length is odd
        else:
            q1 = median(lst_q1)
            q3 = median(lst_q2)
        iqr = round((float(q3) - float(q1)),2)
        return iqr
    except Exception as e:
        raise e
        
def centroid(data,user_id):
    """
    This method returns centroid for any user.
    `====================================================================================
    input_params -> data:dict, user id:str
    ouput -> centroid:float
    =====================================================================================
    """
    try:

        locations = data.get(user_id)
        x_sum = 0
        y_sum = 0
        count = 0
        for loc in locations:
                x_sum += float(loc['x_cord_trans'])
                y_sum += float(loc['y_cord_trans'])
                count += 1
        centroid_x = round((x_sum / count),2)
        centroid_y = round((y_sum / count),2)
        return (centroid_x, centroid_y)
    except Exception as e:
        raise e
    
def std_dev(data,user_id):
    """
    This method returns standard deviation of transaction for any user
    `=================================================================================
    input_params -> data:lst , user_id:str
    output -> standard deviation:float 
    ===================================================================================
    """
    try:
        tran_amt = tran_lst(data,user_id)
        sum_num = 0
        for tran in tran_amt:
            sum_num = sum_num + ((tran - mean(tran_amt))**2)
        std_dev = round((sum_num/len(tran_amt))**0.5, 2)
        return std_dev
    except Exception as e:
        raise e
    
def fraudulent_trans(file,transaction_id):
    """
    This method returns status of transaction. And if transaction is fraudulent 
    it returns transaction details.
    `=================================================================================
    input_params -> file:dict , transaction_id:str
    output -> status:str, transaction deatils:dict
    ===================================================================================
    """
    try:
        data = dict_retrieve_(file)
        trans = data.get(transaction_id)
        for tran in trans:
            if tran['transaction_id'] == transaction_id:
                if tran['status'] == 'true':
                    return (f"Yes & details {tran}")
                else:
                    return("NO")
    except Exception as e:
        raise e
    
def abnormal_trans(data,user_id):
    """
    This method returns abnormal transaction.
    `=================================================================================
    input_params -> data:dict , user_id:str
    output -> transaction deatils:dict
    ===================================================================================
    """
    try:
        transaction = data.get(user_id)
        tran_amt = tran_lst(data,user_id)
        abnormal_tran = []
        for tran in transaction:
            if abs(float(tran['transaction_amt'])- mean(tran_amt)) > 2*standard_dev(tran_amt):
                abnormal_tran.append(tran)
            else:
                pass
        if len(abnormal_tran) > 0:
            return abnormal_tran
        else:
            return "No abnormal transaction"
    except Exception as e:
        raise e
    
def zscore(data,user_id):
    """
    This method returns Z score of transaction for single user.
    `=================================================================================
    input_params -> data:dict , user_id:str
    output -> Z-Score:dict
    ===================================================================================

    """
    try:
        transaction = data.get(user_id)
        tran_amt = tran_lst(data,user_id)
        d ={}
        for tran in transaction:
            z_score = round((float(tran['transaction_amt'])- mean(tran_amt)) / standard_dev(tran_amt),2)
            d.update({tran['transaction_id']:z_score})
        return d
    except Exception as e:
        raise e

def zscore_all(data):
    """
    This method returns Z score of transactions for all users.
    `=================================================================================
    input_params -> data:dict 
    output ->  Z-Score:dict
    ===================================================================================
    """
    try:
        user_id_lst = [key for key in data.keys()]
        tran_amt_all = tran_lst_all(data)
        d ={}
        for user in user_id_lst:
            for tran in data.get(user):
                    z_score = round((float(tran['transaction_amt'])- mean(tran_amt_all)) / standard_dev(tran_amt_all),2)
                    d.update({tran['transaction_id']:z_score})
        return d
    except Exception as e:
        raise e
    
def freq_tran_loc(data,x_cord,y_cord):
    """
    This method frequency of transaction at any location.
    `=================================================================================
    input_params -> data:dict, location:x_cord,y_cord:str
    output ->  frequency of transaction:float
    ===================================================================================

    """
    try:
        user_id_lst = [key for key in data.keys()]
        dict_cord ={}
        for i in user_id_lst:
            for user in data.get(i):
                    x, y = user['x_cord_trans'], user['y_cord_trans']
                    key = (x, y)
                    if key not in dict_cord:
                        dict_cord[key] = 1
                    else:
                        dict_cord[key] += 1
        x_y_cord = (x_cord,y_cord)
        if x_y_cord in dict_cord:
            freq_tran = dict_cord.get(x_y_cord)
            return freq_tran
        else:
            return "No transaction repeated"
    except Exception as e:
        raise e

def outlier_det(data,user_id,x_cord,y_cord):
    """
    This method returns outliers at any location for any user.
    `=================================================================================
    input_params -> data:dict, location:x_cord,y_cord:str
    output ->  outlier transaction:float
    ===================================================================================
    """
    try:
        tran_amt = tran_lst(data,user_id)
        q1,q3,iqr_val= iqr(tran_amt)
        lower_limit =q1-(1.5*iqr_val) 
        upper_limit =q3+(1.5*iqr_val)
        outlier = []
        for i in tran_amt:
            if i>upper_limit or i < lower_limit:
                outlier.append(i)
        x_cord_trans = float(x_cord)
        y_cord_trans = float(y_cord)
        transactions = data.get(user_id)
        for trans in transactions:
            if float(trans['x_cord_trans']) == x_cord_trans and float(trans['y_cord_trans']) == y_cord_trans:
                if float(trans['transaction_amt']) in outlier:
                    return (f"transaction_amt {(float(trans['transaction_amt']))} is outlier")
                else:
                    return (f" the transaction_amt {(float(trans['transaction_amt']))} is not outlier")
            else:
                return "Enter correct co ordinates"
    
    except Exception as e:
        raise e
    
def nth_percentile(data,user_id,percentile):
    """
    This method returns percentile for any user.
    `=================================================================================
    input_params -> data:dict, user_id = str, percentile:str
    output ->  nth percentile:float
    ===================================================================================
    """
    try:
        tran_amt = tran_lst(data,user_id)
        p = float(percentile)
        ordinal_rank = (p*len(tran_amt))/100
        idx = int(ordinal_rank-1)
        nth_percentile = tran_amt[idx]
        return nth_percentile
    except Exception as e:
        raise e
    
def nth_percentile_all(data,percentile):
    """
    This method returns percentile for all user.
    `=================================================================================
    input_params -> data:dict,percentile:str
    output ->  nth percentile:float
    ===================================================================================
    """
    try:
        tran_amt_all = tran_lst_all(data)
        p = float(percentile)
        ordinal_rank = (p*len(tran_amt_all))/100
        idx = int(ordinal_rank-1)
        nth_percentile = tran_amt_all[idx]
        return nth_percentile
    except Exception as e:
        raise e