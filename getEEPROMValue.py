#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# import address list
import addList
import math

# Read the table from I2C which connected to the optical transceiver

A0_H128 = [0x32, 0x33, 0xFF, 0xFF, 0xFF, 0x37, 0x38, 0x39, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45,
             0x22, 0x32, 0x38, 0x88, 0x55, 0x66, 0x89, 0x86, 0x66, 0x75, 0x93, 0x22, 0x32, 0x38,
           0x88, 0x55, 0x66, 0x89, 0x86, 0x66, 0x75, 0x93]

A0_table1 = [0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45,
             0x22, 0x32, 0x38, 0x88, 0x55, 0x66, 0x89, 0x86, 0x66, 0x75, 0x93]


# hex list converter to string

def hex_to_str(s):
    return ''.join([chr(i) for i in s])

# Get Transceiver Vendor Informations

Vendor_Name = hex_to_str(A0_table1[(addList.VendorName-addList.TableStart):(addList.VendorName-addList.TableStart+16)])

Vendor_OUI = ''.join([hex(i) for i in A0_table1[(addList.VendorOUI-addList.TableStart):(addList.VendorOUI-addList.TableStart+3)]])

Vendor_PN = hex_to_str(A0_table1[(addList.VendorPN-addList.TableStart):(addList.VendorPN-addList.TableStart+16)])

Vendor_Rev = hex_to_str(A0_table1[(addList.VendorRev-addList.TableStart):(addList.VendorRev-addList.TableStart+2)])

Vendor_SN = hex_to_str(A0_table1[(addList.VendorSN-addList.TableStart):(addList.VendorSN-addList.TableStart+16)])

Vendor_DateCode = hex_to_str(A0_table1[(addList.DateCode-addList.TableStart):(addList.DateCode-addList.TableStart+8)])

BitRate_Min = A0_table1[addList.BRMin-addList.TableStart]/10.00

BitRate_Max = A0_table1[addList.BRMax-addList.TableStart]/10.00

BitRate = str(BitRate_Min) + '~' + str(BitRate_Max) + 'Gbps'

# Get Transceiver Alarm and Waring Thresholds


def GetThreholdsInt(Table, Address):                    # converter the 2 byte value to int for calculation
    return Table[Address] * 256 + Table[Address + 1]

def GetThreholdsFloat(Table, Address):                    # converter the 2 byte value to float for calculation
    if Table[Address] >> 7 == 0:
        return Table[Address] * 256.0 + Table[Address + 1] / 256.0
    elif Table[Address] >> 7 == 1:
        return -(( Table[Address] ^ 0xFF ) * 256.0 + ( Table[Address + 1] ^ 0xFF ) / 256.0)
    else:
        return 'Error!'

mTempHiAlarm   = GetThreholdsFloat(A0_H128, addList.TempHiAlarm)
mTempLoAlarm   = GetThreholdsFloat(A0_H128, addList.TempLoAlarm)
mTempHiWarning = GetThreholdsFloat(A0_H128, addList.TempHiWarning)
mTempLoWarning = GetThreholdsFloat(A0_H128, addList.TempLoWarning)

mBiasHiAlarm   = GetThreholdsInt(A0_H128, addList.BiasHiAlarm) * 0.002
mBiasLoAlarm   = GetThreholdsInt(A0_H128, addList.BiasLoAlarm) * 0.002
mBiasHiWarning = GetThreholdsInt(A0_H128, addList.BiasHiWarning) * 0.002
mBiasLoWarning = GetThreholdsInt(A0_H128, addList.BiasLoWarning) * 0.002

mTxPowerHiAlarm   = math.log10( GetThreholdsInt(A0_H128, addList.TxPowerHiAlarm) * 0.0001 ) * 10
mTxPowerLoAlarm   = math.log10( GetThreholdsInt(A0_H128, addList.TxPowerLoAlarm) * 0.0001 ) * 10
mTxPowerHiWarning = math.log10( GetThreholdsInt(A0_H128, addList.TxPowerHiWarning) * 0.0001 ) * 10
mTxPowerLoWarning = math.log10( GetThreholdsInt(A0_H128, addList.TxPowerLoWarning) * 0.0001 ) * 10

mRxPowerHiAlarm   = math.log10( GetThreholdsInt(A0_H128, addList.RxPowerHiAlarm) * 0.0001 ) * 10
mRxPowerLoAlarm   = math.log10( GetThreholdsInt(A0_H128, addList.RxPowerLoAlarm) * 0.0001 ) * 10
mRxPowerHiWarning = math.log10( GetThreholdsInt(A0_H128, addList.RxPowerHiWarning) * 0.0001 ) * 10
mRxPowerLoWarning = math.log10( GetThreholdsInt(A0_H128, addList.RxPowerLoWarning) * 0.0001 ) * 10



# Test All the value is get and operation right form the above method
print Vendor_Name
print Vendor_OUI
print Vendor_PN
print Vendor_Rev
print Vendor_DateCode
print Vendor_SN
print BitRate_Min
print BitRate
print A0_H128[addList.TempHiAlarm]>>7
print -((A0_H128[addList.TempHiAlarm])^0xFF)
print -((A0_H128[addList.TempHiAlarm + 1])^0xFF)
print A0_H128[addList.TempHiAlarm]
print mTempHiAlarm