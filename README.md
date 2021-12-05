# Your NU'EST Song

**spacekay personal project #1**

https://www.youtube.com/watch?v=2-b9JK_-t00

(배포 유지가 어려운 상황으로, 시연 영상 별도 첨부)

간단한 설문조사를 통해 사용자의 취향에 맞을 법한 가수의 노래를 추천하는 사이트.

(2021. 10. 22 ~ 2021. 12. 5)


## 사용 기술
* Python Django
* SQLite3
* HTML, CSS, Bootstrap 5
* AWS EC2



## DB 구성

**SQLite3 기반 총 6개 Entity**

![yns-db](https://blog.kakaocdn.net/dn/pg9yG/btrm2okmmBq/KQRBE5oUwEC9lkoj9T7Khk/img.png)
### Case
테스트 케이스 별 결과값 및 설문 참여 여부 기록 
### Question
각 문항별 번호와 내용 저장
### Choice
각 문항별로 선택지에 따른 적용값이 다르므로, 모두 분리하여 기록
### Result
테스트 케이스 별 결과값에 따라 호출하는 결과 종류별 기록
### Song
결과 페이지 별로 추천하는 곡들을 우선순위 포함하여 기록
### ResultSong
특정 결과 페이지에서 호출되는 곡들과, 각 곡들의 배치 우선순위 값을 기록

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
* ubuntu OS 상의 오류로 초기 설정으로 원복하였으나, 지속하여 해결 방안 고민 예정

## History

1. 초기 기능 구현 완료 (21. 11. 15.)
2. DB 추가 및 결과별 좋아요/싫어요 기능 구현 완료 (21. 12. 2.)
3. Unit test code 작성 완료 (21. 12. 2.)
4. 본 프로젝트의 DB 구성, Frontend/Backend 구성 관련 README 정리 (12. 5.)
