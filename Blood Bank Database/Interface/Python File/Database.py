import sqlite3

connObj = sqlite3.connect('BloodBank.db')
cur = connObj.cursor()

bbid = 0

def dbVerify(id):
    print("id : " + id)
    dbID = id
    password = cur.execute('SELECT Password FROM BloodBankDetails WHERE BBID = ?', (dbID))
    print("Password : " + password)
    return password

def bloodbank(name, location,password):

    cur.execute('INSERT INTO BloodBankDetails (bbname, location, password) VALUES (?,?,?)', (name, location,password))
    connObj.commit()
    connObj.close()

def hospital(name, location, associatedBB):
    cur.execute('INSERT INTO HospitalDetails (Name, Location, BBID) VALUES (?,?,?)', (name, location, associatedBB))
    connObj.commit()
    connObj.close()

def donorDetails(name,address,phone,email,gender,bloodGroup,lastDonated):

    cur.execute('INSERT INTO DonorDetails (Name, Location, Gender, BloodGroup, LastDonated, Email, Phone, BBID) VALUES (?,?,?,?,?,?,?,?)', (name, address, gender, bloodGroup, lastDonated, email, phone, bbid))
    connObj.commit()
    connObj.close()
