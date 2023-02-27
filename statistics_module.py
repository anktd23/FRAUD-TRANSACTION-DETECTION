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
        This method calcuate average of transactions from single user.`
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
            logging.info(f"The average transaction of user {user_id} is {avg_trans_amt}")
            return avg_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
    
    def avg_trans_all(self): 
        """
        This method calcuate average of transactions from all users.
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
            logging.info(f"The average transaction of all users is {avg_trans_amt}")
            return avg_trans_amt
        except Exception as e:
            raise ProjException(e,sys)
        
    def mode_trans(self):
        """
        This method calucate average of transactions from all users.
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
            mode = [key for key, value in freq_dict.items() if value == max_freq]
            if max_freq<2:
                logging.info(f"No transaction amount is repeated for user {user_id}")
            else:
                logging.info(f"Transaction amount {mode[0]} repeated {max_freq} times for the user {user_id}")
        except Exception as e:
            raise ProjException(e,sys)
    def mode_trans_all(self) :
        """
        This method calucate average of transactions from all users.
        `================================================================
        input_params -> data:dict, user_id:str
        output-> mode transaction of single user:float
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
            mode = [key for key, value in freq_dict.items() if value == max_freq]

            if max_freq<2:
                logging.info(f"No transaction amount is repeated for all users")
            else:
                logging.info(f"Transaction amount {mode[:]} repeated {max_freq} times for the all users") 
        except Exception as e:
            raise ProjException(e,sys)
    
stat = stats()
stat.avg_trans()
stat.avg_trans_all()
stat.mode_trans()
stat.mode_trans_all()