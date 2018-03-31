"""For Extracting android.permission features from the Android Manifest file of 4 different .apk files and writing it
into a get_permissions.txt file"""

import pprint
import re

#Extracting android.permission features from the Android Manifest file of Whatsapp.apk

file1 = open("AndroidManifestW.xml","r")
file2 = open("getPermissionsW.txt", "w")
for line in file1:
    if "android.permission" in str(line):
        permission1 = re.search("android\.permission\.[\w.]+", line).group() + '\n'
        print permission1
        file2.write(permission1)
file1.close()
file2.close()

#Extracting android.permission features from the Android Manifest file of Facebook.apk

file1 = open("AndroidManifestF.xml","r")
file2 = open("getPermissionsF.txt", "w")
for line in file1:
    if "android.permission" in str(line):
        permission2 = re.search("android\.permission\.[\w.]+", line).group() + '\n'
        print permission2
        file2.write(permission2)
file1.close()
file2.close()

#Extracting android.permission features from the Android Manifest file of FacebookOTP.apk

file1 = open("AndroidManifestO.xml","r")
file2 = open("getPermissionsO.txt", "w")
for line in file1:
    if "android.permission" in str(line):
        permission3 = re.search("android\.permission\.[\w.]+", line).group() + '\n'
        print permission3
        file2.write(permission3)
file1.close()
file2.close()

#Extracting android.permission features from the Android Manifest file of org.benews.apk

file1 = open("AndroidManifestB.xml","r")
file2 = open("getPermissionsB.txt", "w")
for line in file1:
    if "android.permission" in str(line):
        permission4 = re.search("android\.permission\.[\w.]+", line).group() + '\n'
        print permission4
        file2.write(permission4)
file1.close()
file2.close()