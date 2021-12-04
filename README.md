# Your NU'EST Song

**spacekay personal project #1**

http://ec2-3-38-180-26.ap-northeast-2.compute.amazonaws.com

간단한 설문조사를 통해 사용자의 취향에 맞을 법한 가수의 노래를 추천하는 사이트.

(2021. 10. 22 ~ 2021. 12. 5)


## 사용 기술
* Python Django
* SQLite3
* HTML, CSS, Bootstrap 5
* AWS EC2



## DB 구성

![yns-db](https://blog.kakaocdn.net/dn/pg9yG/btrm2okmmBq/KQRBE5oUwEC9lkoj9T7Khk/img.png)

**SQLite3 기반 총 6개 Entity**

* 테스트 별 결과값 및 설문 참여 여부 기록 : Case

* 다음 모델...


## Frontend

* Django Framework에서 기본적으로 제공하는 Django Template를 사용
* Bootstrap 기반으로 HTML/CSS로 원하는 디자인을 구현함
* Result page에서 결과 호불호 조사할 때에는  Ajax로 REST api 호출하여 사용

## Backend

* Django, Django Rest Framework를 사용하여, url mapping 기반 서버 구성
* Session에 해당 테스트 케이스 번호를 기록하고, 각 설문이 진행될 때마다 해당 케이스의 parameter값을 가감
* 결과 페이지에 도달했을 때에 해당 케이스에 기록된 값을 기반으로 DB에서 결과를 호출함

## Deployment

* AWS EC2를 통하여 배포한 uWSGI, nginx 기반 실행 확인 1차 완료
* 서버 재부팅 시 오류가 발생하는 것을 확인하여 nginx에 proxy buffer 설정 완료하였으나, uwsgi service가 일부 영향받아 테스트는 추후 재진행 예정 (12/5 4:38)

## History

1. 초기 기능 구현 완료 (21. 11. 15.)
2. DB 추가 및 결과별 좋아요/싫어요 기능 구현 완료 (21. 12. 2.)
3. Unit test code 작성 완료 (21. 12. 2.)
4. 본 프로젝트의 DB 구성, Frontend/Backend 구성 관련 README 정리 예정
   (~ 12. 5.)
