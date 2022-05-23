# Boat-Vote
Boat-Vote 서비스는 투표기반 SNS입니다.
django-rest-framework를 사용하여 RESTful API기반으로 제작되었습니다.
JWT기반 인증을 포함하고 있습니다.

# 주요 기능
- 회원, 보드, 댓글 CRUD

# 기술스택
- Django
- django-rest-framework
- django-simplejwt
- swagger(openDocs 3.0)
- Docker

# How to Run
### Local Server
1. `$ cd voteSite`
2. `$ python manage.py runserver`

### Docker Container
1. `$ docker pull seyoung8239/boat-vote-be`
2. `$ docker run -p 8000:8000 seyoung8239/boat-vote-be`

## API docs
We used a OpenDocs3.0 based `Swagger API`. You can access docs with the below path after run a server

`http://0.0.0.0:8000/swagger/` 

`http://0.0.0.0:8000/redoc/`

# Contribution
### [남도하] (waroad)
- DB 스키마 설계 (회원, 글, 댓글, 투표 항목)
- REST API 설계 (회원, 글, 댓글, 투표 항목)
- 비지니스 로직 구현 (회원, 글, 댓글, 투표 항목)

### [박세영] (seyoung8239)
- JWT 도입
- OpenDocs3.0 Swagger API 도입
- Docker image 관리
- AWS EC2로 배포

### [오영선]
