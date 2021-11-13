################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 25-Sep-2021               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### Machine-Learning & streaming dashboard.####
####                                        ####
################################################

import os
import platform as pl

class clsConfig(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'REPORT_PATH': Curr_Path + sep + 'report',
        'FILE_NAME': Curr_Path + sep + 'data' + sep + 'TradeIn.csv',
        'SRC_PATH': Curr_Path + sep + 'data' + sep,
        'JSONFileNameWithPath': Curr_Path + sep + 'GUI_Config' + sep + 'CircuitConfiguration.json',
        'APP_DESC_1': 'Dash Integration with Ably!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'SUBDIR' : 'data',
        'ABLY_ID': 'WWP309489.93jfkT:32kkdhdJjdued79e',
        "URL":"https://corona-api.com/countries/",
        "appType":"application/json",
        "conType":"keep-alive",
        "limRec": 50,
        "CACHE":"no-cache",
        "MAX_RETRY": 3,
        "coList": "DE, IN, US, CA, GB, ID, BR",
        "FNC": "NewConfirmed",
        "TMS": "ReportedDate",
        "FND": "NewDeaths",
        "FinData": "Cache.csv"
    }
