import hashlib
import json

def signup():
    print('< 회원가입 >')
    id = input('아이디: ')
    password = input('비밀번호: ')

    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hashedPassword = hash_object.hexdigest()

    with open('data.json', 'r') as f:
        data = json.loads(f.read())
        data[id] = hashedPassword
        
    with open('data.json', 'w') as ff:
        ff.write(json.dumps(data, indent=2))

    print('계정을 만들었습니다.')

if __name__ == '__main__':
    signup()