import pymel.core as pm

#array list
jointArray = pm.ls (sl=True)
CTRLArray = [] #This is a blank array that will hold the CTRLs

#description strings
assetName = "Tentacle"
assetType = "Character"
description = "Arm"
objType = "skinBone"
divider = "_"

#rename joints
for i in range (0,len(jointArray), 1):
    pm.rename ("joint" + str(i+1), assetName + divider + assetType + divider + description + str(i+1) + divider + objType )
    
# create CTRLs
for i in range (1, len(jointArray), 1):
    CTRL = pm.circle (name = assetName + divider + assetType + divider + description + str(i) + divider + "_CTRL", ch=False)
    CTRLArray.append (CTRL) #This will place the new control shape into the blank array
    ConstrainCTRL = pm.parentConstraint (jointArray[i-1],CTRL, mo=False) # mo=False so CTRL shape moves to joint
    pm.delete (ConstrainCTRL) # constrint no longer needed
    pm.makeIdentity (apply=True, t=True, r=True) #apply to translation and rotation of CTRL
    
    



