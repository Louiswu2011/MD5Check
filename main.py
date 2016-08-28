import hashlib
import checkutil


filename = input('Input file location: ')
checkmd5 = input('Input MD5 to check (Leave blank to ignore):')
checksha1 = input('Input SHA1 to check (Leave blank to ignore):')
try:
    file = open(filename, 'rb')
except FileNotFoundError as e:
    print('Cannot find file.')
    print('Program exit.')
else:
    try:
        checkutil.checkfile(file, checkmd5, checksha1)
        print('MD5 & SHA1 verify passed!')
    except checkutil.MD5NotMatch:
        print('MD5 not matched!')
    except checkutil.SHA1NotMatch:
        print('SHA1 not matched!')
    except checkutil.BothNotMatch:
        print('Both MD5 and SHA1 are not matched!')