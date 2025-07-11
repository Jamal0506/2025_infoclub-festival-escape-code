import streamlit as st

# CSS를 사용하여 배경 이미지 및 스타일 적용 (선택 사항)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1517457210816-bcac576579b9?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        color: white; /* 텍스트 색상을 흰색으로 설정하여 배경과 대비되게 함 */
    }
    .stTextInput>div>div>input {
        color: black !important; /* 입력 필드 텍스트 색상을 검은색으로 */
        background-color: rgba(255, 255, 255, 0.8); /* 입력 필드 배경을 반투명 흰색으로 */
    }
    .stButton>button {
        background-color: #4CAF50; /* 버튼 배경색 */
        color: white; /* 버튼 텍스트 색상 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def room1():
    st.title("🎇 축제 속 미궁 방탈출: 첫 번째 방 🎇")
    st.header("당신은 축제를 즐기다 이상한 방에 갇혔습니다! 문을 열려면 암호를 풀어야 합니다.")
    st.write("힌트: 이 암호는 즐거운 무언가와 관련이 있습니다. 특정 글자가 다른 글자로 바뀌어 있습니다.")
    st.write("---")
    st.subheader("첫 번째 암호: 'ENJOY'를 나타내는 암호화된 단어를 찾아보세요.")
    st.markdown("""
    **암호화된 텍스트:**
    `@#$!%`
    
    **치환 규칙:**
    * `@`는 `E`
    * `#`는 `N`
    * `$`는 `J`
    * `!`는 `O`
    * `%`는 `Y`
    """)

    user_answer = st.text_input("첫 번째 방 암호를 입력하세요:", key="room1_input").lower() # 소문자로 변환

    if st.button("암호 확인!", key="room1_button"):
        if user_answer == "enjoy":
            st.success("🎉 축하합니다! 첫 번째 암호를 풀었습니다! 다음 방으로 이동합니다.")
            st.session_state.room = 2 # 다음 방으로 이동
            st.experimental_rerun() # 페이지 새로고침
        else:
            st.error("❌ 틀렸습니다. 다시 시도해보세요!")

def room2():
    st.title("🚀 축제 속 미궁 방탈출: 두 번째 방 🚀")
    st.header("첫 번째 방을 통과하셨군요! 하지만 아직 완전한 자유는 아닙니다. 마지막 암호를 풀어야 합니다.")
    st.write("힌트: 이 암호는 축제와 관련이 있으며, 글자들이 특정 규칙에 따라 밀려 있습니다.")
    st.write("---")
    st.subheader("두 번째 암호: 'FESTIVAL'을 나타내는 카이사르 암호를 풀어보세요.")
    st.markdown("""
    **암호화된 텍스트:**
    `GHVWLYDO`
    
    **힌트:** 암호화된 텍스트에서 원래 단어로 되돌아가려면 각 글자를 왼쪽으로 **1칸** 이동시키세요.
    """)

    user_answer = st.text_input("두 번째 방 암호를 입력하세요:", key="room2_input").lower() # 소문자로 변환

    if st.button("마지막 암호 확인!", key="room2_button"):
        if user_answer == "festival":
            st.balloons()
            st.success("✨ 대탈출 성공! 모든 암호를 풀고 자유를 찾았습니다! 축제를 마음껏 즐기세요! ✨")
            st.session_state.room = 3 # 게임 종료 상태로 설정
        else:
            st.error("❌ 틀렸습니다. 다시 시도해보세요!")

# Streamlit 앱의 시작 지점
if "room" not in st.session_state:
    st.session_state.room = 1 # 초기 방 설정

if st.session_state.room == 1:
    room1()
elif st.session_state.room == 2:
    room2()
elif st.session_state.room == 3:
    st.title("🎉 축제 속 미궁 방탈출: 게임 종료 🎉")
    st.header("모든 암호를 풀고 성공적으로 탈출하셨습니다!")
    st.image("https://images.unsplash.com/photo-1533174072528-067f33405786?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="축제를 즐기는 사람들")
    st.write("게임을 다시 시작하려면 페이지를 새로고침하세요.")
