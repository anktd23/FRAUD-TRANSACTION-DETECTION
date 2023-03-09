import sys
from dataset_module import dict_retrieve
from logger import logging
from exception import ProjException
from utils import median,mean,dict_retrieve_,standard_dev,iqr
file = 'Transaction.txt'

class Stat:
    """
    This class have various statistics methods.
    """
    def __init__(self):
        try:
            self.data = dict_retrieve('Transaction.txt')
            self.user_id = input('Enter the user_id :')
            self.transaction = self.data.get(self.user_id)
            #list of all transaction amount of single user
            self.tran_amt = []
            for tran in self.transaction:
                self.tran_amt.append(float(tran['transaction_amt']))
                self.tran_amt.sort(reverse =False)
                
            #list of all transaction amount of all users  
            self.tran_amt_all = []
            for values in self.data.values():
                lst = []
                for value in values:
                    lst.append(float(value['transaction_amt']))
                self.tran_amt_all.extend(lst)
                self.tran_amt_all.sort(reverse =False)
        except Exception as e:
            raise ProjException(e,sys)
          
    def avg_trans(self):
        """
        This method returns average of transactions from single user.`
        `===============================================================
        input_params -> user_id:str,data:dict
        output-> average transaction of single user:float
        ===============================================================
        """
        try:
            logging.info(f"{'~'*15}AVERAGE TRANSACTIONS PER USER{'~'*15}")
            transaction = self.data.get(self.user_id,[])
            total_amt = 0
            count = 0
            for dic in transaction:
                dic['transaction_amt'] = float(dic['transaction_amt'])
                total_amt = total_amt + dic['transaction_amt']
                count+=1
                avg_trans_amt = round(total_amt/count,2)
            logging.info(f"The average transaction of user {self.user_id} is {avg_trans_amt} \n")
            return avg_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
    
    def avg_trans_all(self): 
        """
        This method returns average of transactions from all users.
        `==============================================================
        input_params -> data:dict
        output-> average transaction of all user:float
        ==============================================================
        """ 
        try:
            logging.info(f"{'~'*15}AVERAGE TRANSACTIONS OF ALL USERs{'~'*15}")
            total_amt_all = 0
            count_all = 0
            for key in self.data.values():
                total_amt = 0
                count = 0
                for key1 in key:
                    key1['transaction_amt'] = float(key1['transaction_amt'])
                    total_amt = total_amt + key1['transaction_amt']
                    count+=1
                total_amt_all = total_amt_all + total_amt
                count_all=count_all + count
                avg_trans_amt = round(total_amt_all/count_all,2)
            logging.info(f"The average transactions of all users is {avg_trans_amt}\n")
            return avg_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def mode_trans(self):
        """
        This method returns mode of transactions from all users.
        `=============================================================
        input_params -> data:dict, user_id:str
        output-> mode transaction of single user:float
        =============================================================
        """ 
        try:
            logging.info(f"{'~'*15}MODE TRANSACTION OF SINGLE USER{'~'*15}")
            freq_dict = {}
            for num in self.tran_amt:
                if num in freq_dict:
                    freq_dict[num] += 1
                else:
                    freq_dict[num] = 1
            max_freq = max(freq_dict.values())
            mode_trans_amt = [key for key, value in freq_dict.items() if value == max_freq]
            if max_freq<2:
                logging.info(f"No transactions amount is repeated for user {self.user_id} \n")
                return None
            else:
                logging.info(f"Transactions amount {mode_trans_amt[0]} repeated {max_freq} times for the user {self.user_id} \n")
                return mode_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
    def mode_trans_all(self) :
        """
        This method returns mode of transactions from all users.
        `================================================================
        input_params -> data:dict
        output-> mode transaction of all users:float
        ================================================================
        """ 
        try:
            logging.info(f"{'~'*15}MODE TRANSACTIONS OF ALL USER{'~'*15}")
            freq_dict = {}
            for num in self.tran_amt_all:
                if num in freq_dict:
                    freq_dict[num] += 1
                else:
                    freq_dict[num] = 1
            max_freq =max(freq_dict.values())
            mode_trans_amt = [key for key, value in freq_dict.items() if value == max_freq]

            if max_freq<2:
                logging.info(f"No transactions amount is repeated for all users \n")
                return None
            else:
                logging.info(f"Transactions amount {mode_trans_amt[:]} repeated {max_freq} times for the all users \n") 
                return mode_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def median_trans(self):
        """
        This method returns median of transactions from single user.
        `================================================================
        input_params -> data:dict, user_id:str
        output-> median transaction of single user:float
        ================================================================
        """ 
        try:
            logging.info(f"{'~'*15}MEDIAN TRANSACTIONS OF SINGLE USER{'~'*15}")  
            lst1=[]
            #if length is odd
            if len(self.tran_amt) % 2 != 0:
                index_pos = int((len(self.tran_amt)+1)/2)
                lst1.append(index_pos-1)
                median_trans_amt = [self.tran_amt[i] for i in lst1]
                logging.info(f"The median of transactions of user {self.user_id} is {median_trans_amt[0]} \n")
                return median_trans_amt[0]
            #if length is even
            else:
                index_pos1 = int((len(self.tran_amt)/2)-1)
                index_pos2 = int(((len(self.tran_amt)/2)+1)-1)
                lst1.insert(0,index_pos1)
                lst1.insert(1,index_pos2)
                idx_element = [self.tran_amt[i] for i in lst1]
                sum_element = 0
                for i in idx_element:
                    sum_element = sum_element + i
                median_trans_amt = round(sum_element/2,2)
                logging.info(f"The median of transactions of user {self.user_id} is {median_trans_amt} \n")
                return median_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def median_trans_all(self):
        """
        This method returns median of transactions for all users.
        `================================================================
        input_params -> data:dict
        output-> median transaction of all user:float
        ================================================================
        """ 
        try:
            logging.info(f"{'~'*15}MEDIAN TRANSACTIONS OF ALL USERS{'~'*15}")  
            lst1=[]
            #if length is odd
            if len(self.tran_amt_all) % 2 != 0:
                index_pos = int((len(self.tran_amt_all)+1)/2)
                lst1.append(index_pos-1)
                median_trans_amt = [self.tran_amt_all[i] for i in lst1]
                logging.info(f"The median of transactions of all users is {median_trans_amt[0]}")
                return median_trans_amt
            #if length is even
            else:
                index_pos1 = int((len(self.tran_amt_all)/2)-1)
                index_pos2 = int(((len(self.tran_amt_all)/2)+1)-1)
                lst1.insert(0,index_pos1)
                lst1.insert(1,index_pos2)
                idx_element = [self.tran_amt_all[i] for i in lst1]
                sum_element = 0
                for i in idx_element:
                    sum_element = sum_element + i
                median_trans_amt = round(sum_element/2, 2)
                logging.info(f"The median of transactions of all users is {median_trans_amt} \n")
                return median_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def iqr_trans(self):
        """
        This method returns IQR 
        `====================================================================================
        input_params -> data:dict, user_id=str
        ouput -> iqr:float
        =====================================================================================
        """
        try:
            logging.info(f"{'~'*15} IQR OF TRANSACTIONS FOR SINGLE USER{'~'*15}")
            n = len(self.tran_amt)
            lst_q1 = self.tran_amt[:n//2]
            lst_q2 = self.tran_amt[n//2:]
            #if length is even
            if n % 2 == 0:
                q1 = median(lst=lst_q1)
                q3 = median(lst=lst_q2)
            #if length is odd
            else:
                q1 = median(lst_q1)
                q3 = median(lst_q2)
            iqr = round((float(q3) - float(q1)),2)
            logging.info(f"The IQR of transactions for user {self.user_id} is {iqr} \n")
            return iqr
        except Exception as e:
            raise ProjException(e,sys)
    
    def iqr_trans_all(self):
        """
        This method returns IQR for all users
        `====================================================================================
        input_params -> data:dict
        ouput -> iqr:float
        =====================================================================================
        """
        try:
            logging.info(f"{'~'*15} IQR OF TRANSACTIONS FOR ALL USERS{'~'*15}")
            n = len(self.tran_amt_all)
            lst_q1 = self.tran_amt_all[:n//2]
            lst_q2 = self.tran_amt_all[n//2:]
            #if length is even
            if n % 2 == 0:
                q1 = median(lst=lst_q1)
                q3 = median(lst=lst_q2)
            #if length is odd
            else:
                q1 = median(lst_q1)
                q3 = median(lst_q2)
            iqr = round((float(q3) - float(q1)),2)
            logging.info(f"The IQR of transactions for all users is {iqr} \n")
            return iqr
        except Exception as e:
            raise ProjException(e,sys)
        
    def centroid(self):
        """
        This method returns centroid for any user.
        `====================================================================================
        input_params -> data:dict, user id:str
        ouput -> centroid:float
        =====================================================================================
        """
        try:
            logging.info(f"{'~'*15} LOCATION CENTROID FOR ANY USER{'~'*15}")
 
            locations = self.data.get(self.user_id)
            x_sum = 0
            y_sum = 0
            count = 0
            for loc in locations:
                    x_sum += float(loc['x_cord_trans'])
                    y_sum += float(loc['y_cord_trans'])
                    count += 1
            centroid_x = round((x_sum / count),2)
            centroid_y = round((y_sum / count),2)
            logging.info(f"The location centroid for user {self.user_id} is {centroid_x,centroid_y} \n")
            return (centroid_x, centroid_y)
        except Exception as e:
            raise ProjException(e,sys)
        
    def std_dev(self):
        """
        This method returns standard deviation of transaction for any user
        `=================================================================================
        input_params -> data:lst , user_id:str
        output -> standard deviation:float 
        ===================================================================================
        """
        try:
            logging.info(f"{'~'*15} STANDARD DEVIATION OF TRANSACTION FOR ANY USER{'~'*15}")
            sum_num = 0
            for tran in self.tran_amt:
                sum_num = sum_num + ((tran - mean(self.tran_amt))**2)
            std_dev = round((sum_num/len(self.tran_amt))**0.5, 2)
            logging.info(f"The standard deviation for user {self.user_id} is {std_dev}\n")
            return std_dev
        except Exception as e:
            raise ProjException(e,sys)
        
    def fraudulent_trans(file):
        """
        This method returns status of transaction. And if transaction is fraudulent 
        it returns transaction details.
        `=================================================================================
        input_params -> data:dict , transaction_id:str
        output -> status:str, transaction deatils:dict
        ===================================================================================
        """
        try:
            logging.info(f"{'~'*15} FRAUDULENT TRANSACTION DETECTION{'~'*15}")
            data = dict_retrieve_('Transaction.txt')
            transaction_id = input('Enter the transaction_id :')
            trans = data.get(transaction_id)
            for tran in trans:
                if tran['transaction_id'] == transaction_id:
                    if tran['status'] == 'true':
                        logging.info(f"The transaction {transaction_id} is fraud and details are {tran}")
                    else:
                        logging.info(f"The transaction {transaction_id} is not fraud.")
        except Exception as e:
            raise ProjException(e,sys)
    def abnormal_trans(self):
        """
        This method returns abnormal transaction.
        `=================================================================================
        input_params -> data:dict , user_id:str
        output -> transaction deatils:dict
        ===================================================================================
        """
        try:
            logging.info(f"{'~'*15} ABNORMAL TRANSACTION DETECTION{'~'*15}")
            abnormal_tran = []
            for tran in self.transaction:
                if abs(float(tran['transaction_amt'])- mean(self.tran_amt)) > 2*standard_dev(self.tran_amt):
                    abnormal_tran.append(tran)
                else:
                    pass
            logging.info(f"Abnormal transaction details for user {self.user_id} are {abnormal_tran}")
        except Exception as e:
            raise ProjException(e.sys)
        
    def zscore(self):
        """
        This method returns Z score of transaction for single user.
        `=================================================================================
        input_params -> data:dict , user_id:str
        output -> Z-Score:dict
        ===================================================================================

        """
        try:
            logging.info(f"{'~'*15}Z SCORE CALCULATION FOR SINGLE USER{'~'*15}")
            d ={}
            for tran in self.transaction:
                z_score = round((float(tran['transaction_amt'])- mean(self.tran_amt)) / standard_dev(self.tran_amt),2)
                d.update({tran['transaction_id']:z_score})
            logging.info(f"Z score for user {self.user_id} is {d}")
            return z_score
        except Exception as e:
            raise ProjException(e,sys)

    def zscore_all(self):
        """
        This method returns Z score of transactions for all users.
        `=================================================================================
        input_params -> data:dict 
        output ->  Z-Score:dict
        ===================================================================================

        """
        try:
            logging.info(f"{'~'*15}Z SCORE CALCULATION FOR ALL USERS{'~'*15}")
            user_id_lst = [key for key in self.data.keys()]
            d ={}
            for user in user_id_lst:
                for tran in self.data.get(user):
                        z_score = round((float(tran['transaction_amt'])- mean(self.tran_amt_all)) / standard_dev(self.tran_amt_all),2)
                        d.update({tran['transaction_id']:z_score})
            logging.info(f"Z score for all users  are {d}")
            return z_score
        except Exception as e:
            raise ProjException(e,sys)
        
    def freq_tran_loc(self):
        """
        This method frequency of transaction at any location.
        `=================================================================================
        input_params -> data:dict, location:tuple
        output ->  frequency of transaction:float
        ===================================================================================

        """
        try:
            logging.info(f"{'~'*15}FREQUENCY OF TRANSACTION AT ANY LOCATION{'~'*15}")
            user_id_lst = [key for key in self.data.keys()]
            dict_cord ={}
            for i in user_id_lst:
                for user in self.data.get(i):
                        x, y = user['x_cord_trans'], user['y_cord_trans']
                        key = (x, y)
                        if key not in dict_cord:
                            dict_cord[key] = 1
                        else:
                            dict_cord[key] += 1
            x_cord = input("Enter x_cord ")
            y_cord = input("Enter y_cord ")
            x_y_cord = (x_cord,y_cord)
            if x_y_cord in dict_cord:
                freq_tran = dict_cord.get(x_y_cord)
                logging.info(f"The frequency of transaction at location{x_y_cord} is {freq_tran}.")
                return freq_tran
            else:
                logging.info(f"Enter correct location co-ordinates.")
        except Exception as e:
            raise ProjException(e,sys)
    
    def outlier_det(self):
        """
        This method returns outliers at any location for any user.
        `=================================================================================
        input_params -> data:dict, location:tuple
        output ->  frequency of transaction:float
        ===================================================================================
        
        """
        try:
            logging.info(f"{'~'*15}OUTLIER FOR ANY LOCATION AND ANY USER {'~'*15}")
            q1,q3,iqr_val= iqr(self.tran_amt)
            lower_limit =q1-(1.5*iqr_val) 
            upper_limit =q3+(1.5*iqr_val)
            outlier = []
            for i in self.tran_amt:
                if i>upper_limit or i < lower_limit:
                    outlier.append(i)
            logging.info(f"The outliers for location and user {self.user_id} are {outlier}")
            x_cord_trans = float(input("Enter x_cord_trans: "))
            y_cord_trans = float(input("Enter y_cord_trans: "))
            transactions = self.data.get(self.user_id)
            for trans in transactions:
                if float(trans['x_cord_trans']) == x_cord_trans and float(trans['y_cord_trans']) == y_cord_trans:
                    if float(trans['transaction_amt']) in outlier:
                        logging.info(f"For user {self.user_id} and location {x_cord_trans,y_cord_trans} the transaction_amt {(float(trans['transaction_amt']))} is outlier")
                    else:
                        logging.info(f"For user {self.user_id} and location {x_cord_trans,y_cord_trans} the transaction_amt {(float(trans['transaction_amt']))} is not outlier")
        
        except Exception as e:
            raise ProjException(e,sys)
        
    def nth_percentile(self):
        """
        This method returns percentile for any user.
        `=================================================================================
        input_params -> data:dict, user_id = str, percentile:str
        output ->  nth percentile:float
        ===================================================================================
        """
        try:
            logging.info(f"{'~'*15}Nth PERCENTILE FOR ANY USER {'~'*15}")
            percentile = input('Enter the percentile: ')
            ordinal_rank = (int(percentile)*len(self.tran_amt))/100
            idx = int(ordinal_rank-1)
            nth_percentile = self.tran_amt[idx]
            logging.info(f"{percentile}th percentile for user {self.user_id} is {nth_percentile}")
            return nth_percentile
        except Exception as e:
            raise ProjException(e,sys)
        
    def nth_percentile_all(self):
        """
        This method returns percentile for all user.
        `=================================================================================
        input_params -> data:dict,percentile:str
        output ->  nth percentile:float
        ===================================================================================
        """
        try:
            logging.info(f"{'~'*15}Nth PERCENTILE FOR ALL USERS {'~'*15}")
            percentile = input('Enter the percentile: ')
            ordinal_rank = (int(percentile)*len(self.tran_amt_all))/100
            idx = int(ordinal_rank-1)
            nth_percentile = self.tran_amt_all[idx]
            logging.info(f"{percentile}th percentile for all users is {nth_percentile}")
            return nth_percentile
        except Exception as e:
            raise ProjException(e,sys)

