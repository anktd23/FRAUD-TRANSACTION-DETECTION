import math
from dataset_module import dict_retrieve
from logger import logging
from exception import ProjException
import sys

class dist:
    """
    This class consist of methods to retrieve data and calculate euclidean distance.
    """
    try:
        def __init__(self):
            self.data = dict_retrieve('transaction.txt')
    except Exception as e:
        raise ProjException(e,sys)
    
    def euclidean_distance(self, trans1, trans2)->float:
        try:
            """
            This method calculated the euclidean distance between two points.
            `===========================================================================================
            input_params -> pt1,pt2  with x,y co-ordinates :str
            outputs -> euclidean dist:float
            ============================================================================================
            """
            x1 = float(trans1['x_cord_trans'])
            y1 = float(trans1['y_cord_trans'])
            x2 = float(trans2['x_cord_trans'])
            y2 = float(trans2['y_cord_trans'])
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        except Exception as e:
            raise ProjException(e,sys)

    def euclidean_dist_same(self):
        """
        This method calculate the euclidean distance between two transaction for same user.
        `================================================================================================
        input_params-> user_id,transaction_id1,transaction_id2:str
        output -> euclidean distance:float
        =================================================================================================
        """
        try:
            user_id = input("Enter the user ID:")
            transaction_id1 = input("Enter the first transaction ID: ")
            transaction_id2 = input("Enter the second transaction ID: ")
            transactions = self.data.get(user_id, [])
            trans1, trans2 = None, None
            for trans in transactions:
                if trans['transaction_id'] == transaction_id1:
                    trans1 = trans
                elif trans['transaction_id'] == transaction_id2:
                    trans2 = trans
                    break
            if trans1 and trans2:
                distance = self.euclidean_distance(trans1, trans2)
                logging.info(f"Euclidean distance between transaction {transaction_id1} and {transaction_id2} for user {user_id} is {distance:.2f}")
            else:
                logging.info("One or both of the transactions not found.")
        except Exception as e:
            raise ProjException(e,sys)
        
    def euclidean_dist_diff(self):
        """
        This method calculate the euclidean distance between two transaction for same user.
        `=============================================================================================
        input_params-> user_id1,user_id2,transaction_id1,transaction_id2:str
        output -> euclidean distance:float
        ==============================================================================================
        """
        try:
            user_id = input("Enter the first user id:")
            transaction_id1 = input("Enter the transaction ID: ")
            transactions1 = self.data.get(user_id, [])
            user_id_1 = user_id
            
            user_id = input("Enter the first second user id:")
            transaction_id2 = input("Enter the transaction ID: ")

            transactions2 = self.data.get(user_id, [])
            user_id_2 = user_id
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
                distance = self.euclidean_distance(trans1, trans2)
                logging.info(f"Euclidean distance between transaction {transaction_id1} of user {user_id_1} and {transaction_id2} of user {user_id_2} is {distance:.2f}")
            else:
                logging.info("One or both of the transactions not found.")
        except Exception as e:
            raise ProjException(e,sys)

distance = dist()
#distance.euclidean_dist_same()
distance.euclidean_dist_diff()