# apartment_entrance_system

## Description
- 아파트 출입관련 시스템에 대한 API 입니다.

## Environment
- python 3.8
- djnago 3.2

## Prerequisite
- `.dockerenv.db.dev` : mysql 환경 설정을 위한 파일
```bash
MYSQL_DATABASE=apartmentsystem   # DB명
MYSQL_USER=apartadmin            # mysql 계정 이름
MYSQL_PASSWORD=adminpassword     # mysql 계정 비밀번호
MYSQL_ALLOW_EMPTY_PASSWORD=true
```

- `.dockerenv.web.dev` : django 환경 설정을 위한 파일
```bash
DJANGO_APP_DEBUG=1                    # 장고 Debug 실행환경 유무
DJANGO_SECRECT_KEY="xxxxxx".          # 장고프로젝트 시크릿 키
SQL_ENGINE="django.db.backends.mysql"
SQL_DATABASE="apartmentsystem"        # 접속할 DB명
SQL_USER="apartadmin"                 # 접속할 DBMS의 계정 이름
SQL_PASSWORD="adminpassword"          # 접속할 DBMS의 계정 비밀번호    
SQL_PORT="3306"                       # 접속할 DBMS의 PORT 정보
```

## Usage

1. 현재 이 프로젝트를 로컬 저장소에 클론을 한다.
```bash
git clone .....
```
2. 프로젝트 위치에 `.dockerenv.web.dev`와 `.dockerenv.db.dev` 파일을 붙여 넣는다.
3. docker-compose up 을 통해서 실행을 시킨다. 


## API
https://www.postman.com/wecode-21-1st-kaka0/workspace/apartment-system/overview

### admin romms
- api/admin/doors/
  - GET : list 조회
  - POST : 등록
    ```json
    {
      "door_number" : "1201", # door 번호
      "password" : "1235",    # 비밀번호 4자리
      "fee" : 1000            # 관리비
    }
    ```
- api/admin/doors/<room_number>
  - GET : 상세 조회
  - DELETE : 삭제
  - UPDATE : 업데이트

### public room
- POST api/public/door : 일반 user의 상세조회
    ```json
    {
      "door_number" : "1201", # door 번호
      "password" : "1235",    # 비밀번호 4자리
    }
    ```
### 관리자 계정 - 테스트를 위해 세션 로그인과 Token을 같이 사용함
- POST /api/users/login/ : 로그인
    ```json
    {
      "username" : "admin",  # user_id
      "password" : "1",      # 비밀번호
    }
    ```
- POST /api/users/registration/ : 회원가입
    ```json
    {
      "username" : "admin",  # user_id
      "password1" : "1",     # 비밀번호,
      "password2" : "1"      # 비밀번호 확인
    }
    ```    
- POST /api/users/logout/ : 로그아웃
