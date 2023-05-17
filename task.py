from random import *;

def generatePassword(length, chars):
    password = '';
    for _ in range(length):
        n = randint(1, len(chars));
        password += chars[n - 1];
        
    return password;

digits = '0123456789';
lowercaseLetters = 'abcdefghijklmnopqrstuvwxyz';
uppercaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
punctuation = '!#$%&*+-=?@^_';
chars = '';

print('Добро пожаловать в генератор паролей.');

print('Введите количество генерируемых паролей:', end='');
countPass = int(input());
print();

print('Введите длину паролей:', end='');
lenPass = int(input());
print();

print('Нужны ли в пароле цифры? (y=да n=нет) ', end='');
isDigit = input().lower();
if isDigit == 'y':
    chars += digits;
print();

print('Нужны ли в пароле прописные буквы? (y=да n=нет) ', end='');
isUpper = input().lower();
if isUpper == 'y':
    chars += uppercaseLetters;
print();

print('Нужны ли в пароле строчные буквы? (y=да n=нет) ', end='');
isLower = input().lower();
if isLower == 'y':
    chars += lowercaseLetters;
print();

print('Нужны ли в пароле символы? (y=да n=нет) ', end='');
isPunctuation = input().lower();
if isPunctuation == 'y':
    chars += punctuation;
print();

print('Исключать ли в пароле неоднозначные символы (il1Lo0O)? (y=да n=нет) ', end='');
isAmbiguous = input().lower();
if isAmbiguous == 'y':
    delChar = chars.find('i');
    if delChar != -1:
        tempStr = chars[:delChar] + chars[delChar + 1:];
        chars = tempStr;
        
    delChar = chars.find('l');
    if delChar != -1:
        tempStr = chars[:delChar] + chars[delChar + 1:];
        chars = tempStr;
        
    delChar = chars.find('1');
    if delChar != -1:
        tempStr = chars[:delChar] + chars[delChar + 1:];
        chars = tempStr;
        
    delChar = chars.find('L');
    if delChar != -1:
        tempStr = chars[:delChar] + chars[delChar + 1:];
        chars = tempStr;
        
    delChar = chars.find('o');
    if delChar != -1:
        tempStr = chars[:delChar] + chars[delChar + 1:];
        chars = tempStr;
        
    delChar = chars.find('0');
    if delChar != -1:
        tempStr = chars[:delChar] + chars[delChar + 1:];
        chars = tempStr;
        
    delChar = chars.find('O');
    if delChar != -1:
        tempStr = chars[:delChar] + chars[delChar + 1:];
        chars = tempStr;
print();

for i in range(countPass):
    print(generatePassword(lenPass, chars));
