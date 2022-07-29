import hashlib
import json

def signIn():
    print('< 로그인 >')
    id = input('아이디: ')
    password = input('비밀번호: ')

    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hashedPassword = hash_object.hexdigest()

    with open('data.json', 'r') as f:
        data = json.loads(f.read())

    if id not in data.keys():
        print('계정이 존재하지 않습니다.')
        return False

    elif data[id] != hashedPassword:
        print('비밀번호가 틀렸습니다.')
        return False

    else:
        print('로그인에 성공하였습니다.')
    


if __name__ == '__main__':
    signIn()