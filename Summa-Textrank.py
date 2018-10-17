from summa import keywords
import os
import glob
import re
import winsound
import operator
import traceback
import SSGLog

mypath = 'C:\\Users\\sidharth.m\\Desktop\\WikiData\\wikiremaining'

logger = SSGLog.setup_custom_logger('TagTest2-TextRank-Logger')

with open('TextFilter1.log', "r") as myfile:
                data = myfile.read().replace('\n', '')

                logger.info(keywords.keywords(data))