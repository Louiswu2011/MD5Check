import hashlib


filename = input('Input file location: ')
check = input('Input MD5 to check (Leave blank to ignore):')
try:
    file = open(filename, 'rb')
except FileNotFoundError as e:
    print('Cannot find file.')
    print('Program exit.')
else:
    md5 = hashlib.md5(file.read()).hexdigest()
    file.close()
    if check == '':
        print('MD5: ', md5)
    else:
        if md5 == check:
            print('MD5: ', md5)
            print('CHK: ', check)
            print('--------------------------------------')
            print('File untouched!')
        else:
            print('MD5: ', md5)
            print('CHK: ', check)
            print('--------------------------------------')
            print('File modified!')