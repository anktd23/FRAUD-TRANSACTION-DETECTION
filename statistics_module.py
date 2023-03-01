import sys
from dataset_module import dict_retrieve
from logger import logging
from exception import ProjException
from utils import median
class stats:
    """
    This class have various statistics methods.
    """
    def __init__(self):
        try:
            self.data = dict_retrieve('Transaction.txt')
            self.user_id = input('Enter the user_id :')
            transaction = self.data.get(self.user_id)
            #list of all transaction amount of single user
            self.lst = []
            for dic in transaction:
                self.lst.append(float(dic['transaction_amt']))
                self.lst.sort(reverse =False)
                
            #list of all transaction amount of all users  
            self.lst_all = []
            for values in self.data.values():
                lst = []
                for value in values:
                    lst.append(float(value['transaction_amt']))
                self.lst_all.extend(lst)
                self.lst_all.sort(reverse =False)
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
            logging.info(f"{'~'*15}AVERAGE TRANSACTION PER USER{'~'*15}")
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
            logging.info(f"{'~'*15}AVERAGE TRANSACTION OF ALL USERs{'~'*15}")
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
            logging.info(f"The average transaction of all users is {avg_trans_amt}\n")
            return avg_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def mode_trans(self):
        """
        This method returns average of transactions from all users.
        `=============================================================
        input_params -> data:dict, user_id:str
        output-> mode transaction of single user:float
        =============================================================
        """ 
        try:
            logging.info(f"{'~'*15}MODE TRANSACTION OF SINGLE USER{'~'*15}")
            freq_dict = {}
            for num in self.lst:
                if num in freq_dict:
                    freq_dict[num] += 1
                else:
                    freq_dict[num] = 1
            max_freq = max(freq_dict.values())
            mode_trans_amt = [key for key, value in freq_dict.items() if value == max_freq]
            if max_freq<2:
                logging.info(f"No transaction amount is repeated for user {self.user_id} \n")
                return None
            else:
                logging.info(f"Transaction amount {mode_trans_amt[0]} repeated {max_freq} times for the user {self.user_id} \n")
                return mode_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
    def mode_trans_all(self) :
        """
        This method returns average of transactions from all users.
        `================================================================
        input_params -> data:dict
        output-> mode transaction of all users:float
        ================================================================
        """ 
        try:
            logging.info(f"{'~'*15}MODE TRANSACTION OF ALL USER{'~'*15}")
            freq_dict = {}
            for num in self.lst_all:
                if num in freq_dict:
                    freq_dict[num] += 1
                else:
                    freq_dict[num] = 1
            max_freq =max(freq_dict.values())
            mode_trans_amt = [key for key, value in freq_dict.items() if value == max_freq]

            if max_freq<2:
                logging.info(f"No transaction amount is repeated for all users \n")
                return None
            else:
                logging.info(f"Transaction amount {mode_trans_amt[:]} repeated {max_freq} times for the all users \n") 
                return mode_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def median_trans(self):
        """
        This method returns median of transactions from single user.
        `================================================================
        input_params -> data:dict, user_id:str
        output-> mode transaction of single user:float
        ================================================================
        """ 
        try:
            logging.info(f"{'~'*15}MEDIAN TRANSACTION OF SINGLE USER{'~'*15}")  
            lst1=[]
            #if length is odd
            if len(self.lst) % 2 != 0:
                index_pos = int((len(self.lst)+1)/2)
                lst1.append(index_pos-1)
                median_trans_amt = [self.lst[i] for i in lst1]
                logging.info(f"The median of transaction of user {self.user_id} is {median_trans_amt[0]} \n")
                return median_trans_amt[0]
            #if length is even
            else:
                index_pos1 = int((len(self.lst)/2)-1)
                index_pos2 = int(((len(self.lst)/2)+1)-1)
                lst1.insert(0,index_pos1)
                lst1.insert(1,index_pos2)
                idx_element = [self.lst[i] for i in lst1]
                sum_element = 0
                for i in idx_element:
                    sum_element = sum_element + i
                median_trans_amt = round(sum_element/2,2)
                logging.info(f"The median of transaction of user {self.user_id} is {median_trans_amt} \n")
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
            logging.info(f"{'~'*15}MEDIAN TRANSACTION OF ALL USERS{'~'*15}")  
            lst1=[]
            #if length is odd
            if len(self.lst_all) % 2 != 0:
                index_pos = int((len(self.lst_all)+1)/2)
                lst1.append(index_pos-1)
                median_trans_amt = [self.lst_all[i] for i in lst1]
                logging.info(f"The median of transaction of all users is {median_trans_amt[0]}")
                return median_trans_amt
            #if length is even
            else:
                index_pos1 = int((len(self.lst_all)/2)-1)
                index_pos2 = int(((len(self.lst_all)/2)+1)-1)
                lst1.insert(0,index_pos1)
                lst1.insert(1,index_pos2)
                idx_element = [self.lst_all[i] for i in lst1]
                sum_element = 0
                for i in idx_element:
                    sum_element = sum_element + i
                median_trans_amt = round(sum_element/2, 2)
                logging.info(f"The median of transaction of all users is {median_trans_amt} \n")
                return median_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def iqr_trans(self):
        """
        This method returns IQR 
        `====================================================================================
        input_params -> data:dict, user_id=str
        ouput -> iqr:float
        """
        try:
            logging.info(f"{'~'*15} IQR OF TRANSACTION FOR SINGLE USER{'~'*15}")
            n = len(self.lst)
            lst_q1 = self.lst[:n//2]
            lst_q2 = self.lst[n//2:]
            #if length is even
            if n % 2 == 0:
                q1 = median(lst=lst_q1)
                q3 = median(lst=lst_q2)
            #if length is odd
            else:
                q1 = median(lst_q1)
                q3 = median(lst_q2)
            iqr = round((float(q3) - float(q1)),2)
            logging.info(f"The IQR of transaction for user {self.user_id} is {iqr} \n")
            return iqr
        except Exception as e:
            raise ProjException(e,sys)
    
stat = stats()
stat.avg_trans()
stat.avg_trans_all()
stat.mode_trans()
stat.mode_trans_all()
stat.median_trans()
stat.median_trans_all()
stat.iqr_trans()
