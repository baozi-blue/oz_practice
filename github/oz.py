print("testing...")


# CLI ⇒ Command Line Interface 글자를 입력해서 컴퓨터에 명령을 내리는 방식
#    - 사용 환경 : Visual studio code
#        - Window : Gitbash  터미널 사용
#        - Mac : zsh 터미널 사용
# GUI ⇒ Graphical User Interface 아이콘, 메뉴 등 그래픽 요소를 이용해 상호 작용하는 방식
#    - 사용 환경 : SourceTree


# commit 명령어 :

# commit을 만드는 명령어 : -m은 뒤에 commit 메시지를 입력할 수 있도록 해주는 옵션
# git commit -m "커밋 메시지"

# 변경된 모든사항을 바로 add하고 commit하는 명령어
#  git commit -am "커밋 메시지"

# commit 메시지 예시
#  git commit -m "first commit"
#  git commit -am "first commit"

### vim 편집기로 commit 메시지 입력해보기

# “git commit -m” 명령어에서 “-m” 옵션을 제외하고 “git commit”만 입력할 경우 vim이라는 문서 편집기 화면이 나타납니다.
# Vim 편집기 화면이 노출되면 아래 순서대로 진행하시면 메시지를 입력할 수 있습니다.

#- i 키를 눌러서 문서 편집 모드로 진입합니다.
#- first commit를 최상단에 입력합니다.
#- ESC 키를 눌러서 문서 편집 모드에서 빠져나옵니다.
#- shift + : 을 누른 후 w와 q를 동시에 입력해줍니다. 여기서 wq는 메시지를 저장(write)하고 편집을 종료(quit)한다는 의미입니다.

# Vim 명령어
# https://tartan-steel-3da.notion.site/10-Git-commit-e7aa012e3fd84a6fbbfe9ee8d1b7bd31




# commit 이력을 확인할 수 있는 git log 명령어 설정
#  git log
  
# 각 커밋마다의 변경사항 함께 보기
#  git log -p
​
# 최근 n개 커밋만 보기
#  git log -(갯수)
​
# 통계와 함께 보기
#  git log --stat
​
# 한 줄로 보기
#  git log --oneline
​
# 변경사항 내 단어 검색
#  git log -S (검색어)
​
# 커밋 메시지로 검색
#  git log --grep (검색어)
​
# 자주 사용되는 그래프 로그 보기
#  git log --all --decorate --oneline --graph






