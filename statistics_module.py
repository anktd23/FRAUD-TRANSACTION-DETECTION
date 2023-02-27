import sys
from dataset_module import dict_retrieve
from logger import logging
from exception import ProjException
class stats:
    """
    This class have various statistics methods.
    """
    def __init__(self):
        try:
            self.data = dict_retrieve('Transaction.txt')
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
            user_id = input('Enter the user_id :')
            transaction = self.data.get(user_id,[])
            total_amt = 0
            count = 0
            for dic in transaction:
                dic['transaction_amt'] = float(dic['transaction_amt'])
                total_amt = total_amt + dic['transaction_amt']
                count+=1
                avg_trans_amt = round(total_amt/count,2)
            logging.info(f"The average transaction of user {user_id} is {avg_trans_amt} \n")
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
            user_id = input('Enter the user_id :')
            transaction = self.data.get(user_id,[])
            lst = []
            for dic in transaction:
                trans_amt  = float(dic['transaction_amt'])
                lst.append(trans_amt)

            freq_dict = {}
            for num in lst:
                if num in freq_dict:
                    freq_dict[num] += 1
                else:
                    freq_dict[num] = 1
            max_freq = max(freq_dict.values())
            mode_trans_amt = [key for key, value in freq_dict.items() if value == max_freq]
            if max_freq<2:
                logging.info(f"No transaction amount is repeated for user {user_id} \n")
                return None
            else:
                logging.info(f"Transaction amount {mode_trans_amt[0]} repeated {max_freq} times for the user {user_id} \n")
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
            lst_final = []
            for values in self.data.values():
                lst = []
                for value in values:
                    lst.append(float(value['transaction_amt']))
                lst_final.extend(lst)
            
            freq_dict = {}
            for num in lst_final:
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
            user_id = input('Enter the user_id :')           
            transaction = self.data.get(user_id,[])
            lst  =[]
            for dic in transaction:
                lst.append(float(dic['transaction_amt']))
                lst.sort(reverse =False)
            lst1=[]
            if len(lst) % 2 != 0:
                index_pos = int((len(lst)+1)/2)
                lst1.append(index_pos-1)
                median_trans_amt = [lst[i] for i in lst1]
                logging.info(f"The median of transaction of user {user_id} is {median_trans_amt[0]} \n")
                return median_trans_amt[0]
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
                logging.info(f"The median of transaction of user {user_id} is {median_trans_amt} \n")
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
            lst_final = []
            for values in self.data.values():
                lst = []
                for val in values:
                    val['transaction_amt'] = float(val['transaction_amt'])
                    lst.append(val['transaction_amt'])
                lst_final.extend(lst)
            lst_final.sort(reverse =False)
            lst1=[]
            if len(lst_final) % 2 != 0:
                index_pos = int((len(lst_final)+1)/2)
                lst1.append(index_pos-1)
                median_trans_amt = [lst_final[i] for i in lst1]
                logging.info(f"The median of transaction of all users is {median_trans_amt[0]}")
                return median_trans_amt
            else:
                index_pos1 = int((len(lst_final)/2)-1)
                index_pos2 = int(((len(lst_final)/2)+1)-1)
                lst1.insert(0,index_pos1)
                lst1.insert(1,index_pos2)
                idx_element = [lst_final[i] for i in lst1]
                sum_element = 0
                for i in idx_element:
                    sum_element = sum_element + i
                median_trans_amt = round(sum_element/2, 2)
                logging.info(f"The median of transaction of all users is {median_trans_amt} \n")
                return median_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
    
stat = stats()
stat.avg_trans()
stat.avg_trans_all()
stat.mode_trans()
stat.mode_trans_all()
stat.median_trans()
stat.median_trans_all()