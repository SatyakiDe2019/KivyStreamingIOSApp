##############################################
#### Updated By: SATYAKI DE               ####
#### Updated On: 12-Nov-2021              ####
####                                      ####
#### Objective: Publishing Streaming data ####
#### to Ably channels & captured IoT      ####
#### events from the simulator & publish  ####
#### them in Dashboard through measured   ####
#### KPIs.                                ####
####                                      ####
##############################################

import random
import time
import json
import clsPublishStream as cps
import datetime
from clsConfig import clsConfig as cf
import logging

# Invoking the IoT Device Generator.
def main():

    ###############################################
    ###           Global Section                ###
    ###############################################

    # Initiating Ably class to push events
    x1 = cps.clsPublishStream()

    ###############################################
    ###    End of Global Section                ###
    ###############################################

    # Initiating Log Class
    general_log_path = str(cf.conf['LOG_PATH'])
    msgSize = int(cf.conf['limRec'])

    # Enabling Logging Info
    logging.basicConfig(filename=general_log_path + 'IoTDevice.log', level=logging.INFO)

    # Other useful variables
    cnt = 1
    idx = 0
    debugInd = 'Y'

    x_value = 0
    total_1 = 100
    total_2 = 100

    var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # End of usefull variables

    while True:

        srcJson = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

        tmpJson = str(srcJson)

        if cnt == 1:
            srcJsonMast = '{' + '"' + str(idx) + '":'+ tmpJson
        elif cnt == msgSize:
            srcJsonMast = srcJsonMast + '}'
            print('JSON: ')
            print(str(srcJsonMast))

            # Pushing both the Historical Confirmed Cases
            retVal_1 = x1.pushEvents(srcJsonMast, debugInd, var)

            if retVal_1 == 0:
                print('Successfully IoT event pushed!')
            else:
                print('Failed to push IoT events!')

            srcJsonMast = ''
            tmpJson = ''
            cnt = 0
            idx = -1
            srcJson = {}
            retVal_1 = 0
        else:
            srcJsonMast = srcJsonMast + ',' + '"' + str(idx) + '":'+ tmpJson

        cnt += 1
        idx += 1

        time.sleep(1)

if __name__ == "__main__":
    main()
