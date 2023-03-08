
from statistics_module import Stat
if __name__=="__main__":
     try:
        stat = Stat()
        stat.avg_trans()
        stat.avg_trans_all()
        stat.mode_trans()
        stat.mode_trans_all()
        stat.median_trans()
        stat.median_trans_all()
        stat.iqr_trans()
        stat.iqr_trans_all()
        stat.centroid()
        stat.std_dev()
        stat.fraudulent_trans()
        stat.abnormal_trans()
        stat.zscore()
        stat.zscore_all()
        stat.freq_tran_loc()
        stat.outlier_det()
        stat.nth_percentile()
        stat.nth_percentile_all()
     except Exception as e:
          print(e)