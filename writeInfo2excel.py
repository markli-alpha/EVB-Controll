#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

# set the workbook name and sheet name
VendorSN = '0123'
VendorPN = 'XFP'
sheetName  = VendorSN
workbookName = VendorPN + '.xlsx'

# create datas for address colum
loAddress = np.linspace(0,127,128,dtype=int)
hiAddress = np.linspace(128,256,128,dtype=int)

# add list to write to the excel
name=['Vendor Name','Vendor SN','Vendor PN','Vendor Rev']
Values=[1,2,3,4]

eepromValues = {'A0':hiAddress, 'Add_128Bytes':hiAddress,
                'Table_0':loAddress,'Table_1':hiAddress,'Table_2':loAddress}

productInfo = {'Names':name, 'Value':Values}


# format datas to write in the excel

df1 = pd.DataFrame(eepromValues)
df2 = pd.DataFrame(productInfo,)

# wirte the data to the same workbook by each sheets

sheetWrite = pd.ExcelWriter(workbookName)
df1.to_excel(sheetWrite, sheet_name=sheetName)
df2.to_excel(sheetWrite, sheet_name=sheetName,startcol= 8)
sheetWrite.save()

#df = pd.read_excel('path_to_file.xlsx', index_col=(0, 1))
# df