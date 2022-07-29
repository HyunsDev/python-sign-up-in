# python-sign-up-in
친구의 부탁으로 인해 간단하게 구현했습니다.

동작 원리를 설명하기 위해 만든 코드로, 실제 서비스에 이 코드 그대로 쓰면 큰일납니다. 

## 실제 서비스에서 로그인을 사용하려면
- [ ] _**데이터베이스(mysql 등)을 사용하십시오.**_ : 이 코드에서는 JSON을 사용하고 있는데 이건 너무 비효율적입니다.. 나만 쓰려고 하는 거면 괜찮긴 합니다.
- [ ] _**해싱을 여러번 (최소 5회 이상) 하십시오.**_ : 해싱된 문자열을 다시 해시에 넣고 돌리면 보안성이 더욱 강화됩니다.. (특히 레인보우테이블)
- [ ] _**SALT(솔트, 소금)을 사용하십시오.**_ : 별 건 아니고 원래 비밀번호 뒤에 추가로 붙이는 랜덤 문자열입니다.. 랜덤으로 아무 문자열을 생성하고 비밀번호 뒤에 붙여서 같이 해싱한뒤 데이터베이스에 저장할 때 해싱된 비밀번호와 솔트를 같이 저장하고, 로그인할 때는 역순으로 하면 됩니다.
- [ ] _**DB든 파일이든 보안을 신경쓰십쇼**_ : 아무리 SHA256 * n차 해싱 * 매우 긴 솔트해도 데이터베이스 자체의 보안이 제일 중요합니다.. 개인정보에는 비밀번호만 있는게 아니거든요.
 
# 실행 방법
1. 파이썬 필요
2. `python - m pip install fastapi "uvicorn[standard]"` 입력
3. `uvicorn main:app --reload` 으로 실행

![2](https://user-images.githubusercontent.com/46562466/181715591-f27c6bbe-0e73-489a-9bfc-48d950172593.gif)
![1](https://user-images.githubusercontent.com/46562466/181696990-d3951151-433f-4d45-ba01-b2e5204bc619.gif)

기본으로 있는 계정은 id: `hyuns`, pw: `123123` 입니다.
