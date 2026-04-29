import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Streamlit 3일차 실습 App",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Streamlit 3일차 실습")
st.write("")

container = st.container(border=True)
container.title("운영현황")
col1, col2, col3 = container.columns(3, border=True) 

with col1: 
    st.metric(
    label="매출 합계",
    value=f"45,231",
    delta=f"+20.1%"
)

with col2:
    st.metric(
        label="회원 가입",
        value=f"235",
        delta=f"-1.21%"
    )

with col3:
    st.metric(
        label="판매 수익",
        value=f"12,234",
        delta=f"+19%"
    )

# 샘플 데이터
chart_data = pd.DataFrame(
  {
      "Month" : ["1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"],
      "Sales":[4300,4500,2800,3600,3750,2700,1800,2650,1850,1300,4900,2050]
  }
)

table_data = pd.DataFrame(
  {
      "거래내역":["INV001","INV002","INV003","INV004","INV005"],
      "결제":["수금","미수금","수금","미수금","수금"],
      "총액":[500,200,150,350,400],
      "지불방법":["신용카드","현금","체크카드","신용카드","무통장입금"]
  }
)

st.header("매출 현황")

tab1, tab2, tab3 = st.tabs(["📊 Bar Chart", "📈 Line Chart", "📉 Area Chart"])

with tab1:
    # st.bar_chart(chart_data, x="Month", y="Sales")
    fig = px.bar(chart_data, x="Month", y="Sales")
    st.plotly_chart(fig)    

with tab2:
    fig = px.line(chart_data, x="Month", y="Sales", markers=True)
    st.plotly_chart(fig)

with tab3:
    # st.area_chart(chart_data, x="Month", y="Sales")
    fig = px.area(chart_data, x="Month", y="Sales", markers=True)
    st.plotly_chart(fig)


st.header("☀️ 거래내역 (Read Only)")     

container = st.container(border=True)  
container.dataframe(table_data)

st.header("✅ 거래내역 (Editable)")  

container = st.container(border=True)  
container.data_editor(
  table_data, 
  column_config={
    "결제": st.column_config.SelectboxColumn(  
        options=["수금", "미수금"],
    ),
    "총액": st.column_config.NumberColumn(
        min_value=0,
        max_value=1000,
        step=1, 
    ),
    "지불방법": st.column_config.SelectboxColumn(  
        options=["신용카드","현금","체크카드","무통장입금"],
    ),    
  },                           
  disabled=["거래내역"],
  num_rows="dynamic"
)

# st.markdown("""
# <style>
# /* dialog 전체 박스 */
# div[data-testid="stDialog"] > div {
#     border-radius: 16px;
#     border: 2px solid #4CAF50;
#     box-shadow: 0 8px 24px rgba(0,0,0,0.2); 
# } 
# </style>
# """, unsafe_allow_html=True)

@st.dialog("의견을 말씀해주세요.")
def vote(item):   
    st.write(f"{item}하는 이유는 무엇입니까?")
    reason = st.text_input("그 이유는...")
    if st.button("제출"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun() 

col4, col5 = st.columns(2)

with col4:
    container = st.container(border=True)
    container.header("지불 방법 선택") 
    genre = container.radio(
        "지불 방법", 
        options=["신용카드","현금","체크카드"],
        captions=[
                    "국민/신한/우리",
                    "현금영수증",
                    "농협/신협",
                  ],
    )
    
    if genre == "신용카드":
        container.success("신용카드를 선택하셨습니다.")
    elif genre == "현금":
        container.info("현금을 선택하셨습니다.")
    else:
        container.warning("체크카드를 선택하셨습니다.") 

with col5:
    container = st.container(border=True)
    container.header("찬/반 투표") 

    if "vote" not in st.session_state:
        container.text("찬/반 투표에 참여해주세요.")
        col6, col7 = container.columns(2)
        with col6:
            if st.button("찬성", width="stretch"):
                vote("찬성")

        with col7:
            if st.button("반대", width="stretch"):
                vote("반대")
    else:
        if st.session_state.vote["item"] == "찬성":
            container.success(f"{st.session_state.vote['item']}하시는 이유는 '{st.session_state.vote['reason']}' 입니다")
        else:
            container.error(f"{st.session_state.vote['item']}하시는 이유는 '{st.session_state.vote['reason']}' 입니다")

        if container.button("다시 투표하기"):
            del st.session_state.vote
            st.rerun()

videos = {
  "멜로":"https://www.youtube.com/watch?v=0pdqf4P9MB8",
  "미스터리":"https://www.youtube.com/watch?v=YoHD9XEInc0",
  "스릴러":"https://www.youtube.com/watch?v=6hB3S9bIaco",
  "액션":"https://www.youtube.com/watch?v=TcMBFSGVi1c",
}  

if "play" not in st.session_state:
  st.session_state.play = {"item": "멜로"}

container = st.container(border=True)
col8, col9 = container.columns([1, 10])
with col8:
    st.text("⚠️") 

with col9:
    st.markdown("""**좋아하는 영화 장르가 무엇인가요?**
                \n\n주말 넷플릭스 주도권을 룸메에게 뺏겨서야 되겠습니까?""")

container = st.container()
col10, col11, col12, col13 = container.columns(4)

with col10:
    if st.button("멜로", width="stretch") :
        st.session_state.play = {"item": "멜로"}

with col11:
    if st.button("미스터리", width="stretch") :
        st.session_state.play = {"item": "미스터리"}

with col12:
    if st.button("스릴러", width="stretch") :
        st.session_state.play = {"item": "스릴러"}

with col13:
    if st.button("액션", width="stretch") :
        st.session_state.play = {"item": "액션"}

st.write(f"현재 선택된 장르 : {st.session_state.play['item']}")
st.video(videos[st.session_state.play['item']], width="stretch")

st.header("익스팬더")

with st.expander("멜로"):
    st.write("주말엔 무조건 멜로 정주행이지")

with st.expander("미스터리"):
    st.write("한번 미스터리에 빠지면 못 헤어나와요")

with st.expander("스릴러"):
    st.write("어제 다 못 본 그 장면에서 다시 봐야지")

with st.expander("액션"):
    st.write("스트레스를 시원하게 날려버려요!")        


            