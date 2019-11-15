# import sqlite3
#
# connectionObjectLogin = sqlite3.connect('LoginDetails.db')
# connectionBBDetails = sqlite3.connect('BloodBankDetails.db')
# connectionObjectDonorDetails = sqlite3.connect('DonorDetails.db')
# connectionObjectStockDetails = sqlite3.connect('StockDetails.db')
# connectionObjectHDetails = sqlite3.connect('HospitalDetails.db')
#
# updateLogin = connectionObjectLogin.commit()
# updateBBDetails = connectionBBDetails.commit()
# updateDonorDetails = connectionObjectDonorDetails.commit()
# updateStockDetails = connectionObjectStockDetails.commit()
# updateHDetails = connectionObjectHDetails.commit()
#
# selectLogin = connectionObjectLogin.cursor()
# selectBBDetails = connectionBBDetails.cursor()
# selectDonorDetails = connectionObjectDonorDetails.cursor()
# selectStockDetails = connectionObjectStockDetails.cursor()
# selectHDetails = connectionObjectHDetails.cursor()
#
# # selectLogin.execute(" Create table Login(BloodBankID Integer, Password BLOB);")
# # selectBBDetails.execute(" Create table BloodBankDetails(BBID Integer, BBName BLOB, Location BLOB);")
# # selectDonorDetails.execute(" Create table DonorDetails(DID Integer, DName BLOB, DGender Text, DLocation BLOB, BloodGroup BLOB, LastDonated BLOB, Email BLOB, Phone Integer, BBID BLOB);")
# # selectStockDetails.execute(" Create table StockDetails(BBID BLOB, Ap Integer, An Integer, Bp Integer, Bn Integer, Op Integer, On Integer, ABp Integer, ABn Integer);")
# # selectHDetails.execute(" Create table HospitalDetails(HID BLOB, HName BLOB, Hlocation BLOB, AssociatedBBID BLOB);")
#
# def updateBBDetails(name,location,password):
#     # selectBBDetails.execute(" Insert into BloodBankDetail(BBName,BBLocation,BBPassword) values(?,?,?);"(name,location,password))
#     # selectBBDetails.commit()
#     selectBBDetails.execute(" Insert into BloodBankDetails (BBName,BBLocation,BBPassword) values (qwerty,xxxxx,qwerty); ")
#     selectBBDetails.commit()
#     print("Success")
#
# updateBBDetails(1,1,1)