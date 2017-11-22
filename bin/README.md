# README #

### 윈도우
* git-jira & git-win 파일을 /bin 디렉토리로 복사
** git-win 은 원하는 명령어로 이름을 변경
* python 2.x 버전을 설치
* pip install pycurl
* .bash_profile 아래 를 추가
** export JIRA_URL='http://jira.daumkakao.com/rest/api/2/issue'
** export JIRA_AUTH='YW5kcmV3LnNvbmc6d2pzcmhrZHVzMDIh'
** export JIRA_CACHE_FILE='C:\Users\kakaogames\.gitjira'
* 위에 JIRA_AUTH 는 아래 명령어로 생성
** echo -n "user_id:password" | openssl enc -base64

### MAC
* git=jira & git-mac 파일을 /usr/local/bin 디렉토리로 복사
** git-mac 는 원하는 명령어로 이름을 변경
* python 2.x 버전을 설치 (보통 Mac 에는 설치가 되어 있음)
* pip install pycurl 
* 혹시 pycurl 설치 실패시에는 아래 명령으로 설치
** sudo env ARCHFLAGS="-arch x86_64" easy_install setuptools pycurl==7.19.0
* .bash_profile 아래 를 추가
** export JIRA_URL='http://jira.daumkakao.com/rest/api/2/issue'
** export JIRA_AUTH='YW5kcmV3LnNvbmc6d2pzcmhrZHVzMDIh'
** export JIRA_CACHE_FILE='/Users/kakaogames/.gitjira'
* 위에 JIRA_AUTH 는 아래 명령어로 생성
** echo -n "user_id:password" | openssl enc -base64

