Streamlit Cloud는 로컬 환경을 복제하지 않고, 

requirements.txt에 적힌 패키지만 새로 설치해서 실행합니다.

로컬에서는 잘 되는데 배포 환경에서만 깨질 때 특히 흔해요.


 
**핵심은 의존성 파일(requirements.txt) 입니다.**


# 해결 방법

프로젝트 루트에 requirements.txt 파일을 만들거나 수정해서 아래를 포함하세요:

streamlit
plotly

이미 파일이 있다면 plotly가 빠져 있을 가능성이 큽니다.

# 추가로 체크할 것

파일 이름이 정확히 requirements.txt인지
같은 폴더(루트)에 있는지
