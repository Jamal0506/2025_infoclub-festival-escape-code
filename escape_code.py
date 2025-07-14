import streamlit as st

# Streamlit 세팅
st.set_page_config(page_title="암호 방탈출", layout="centered")
st.title("🎉 축제 암호 방탈출")
st.markdown("""
**컨셉:** 축제를 즐기던 중, 이상한 방에 갇히게 되었다. 방에 남겨진 쪽지를 해독해서 탈출하라!

---
""")

# 단계별 상태 관리
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# 스테이지 1: 도입부
if st.session_state.stage == 1:
    st.subheader("1단계: 이상한 방")
    st.markdown("""
    당신은 축제를 즐기고 있었지만, 정신을 차려보니 낯선 방 안에 있습니다.
    
    방 한켠에는 쪽지가 떨어져 있습니다:

    `암호를 풀어야 나갈 수 있다. 준비됐는가? 그렇다면 'START'를 입력하라.`
    """)

    answer1 = st.text_input("쪽지에 적힌 암호는? (힌트: START)", key="stage1")
    if answer1.strip().lower() == "start":
        st.success("정답입니다! 다음 방으로 이동합니다.")
        st.session_state.stage = 2
        st.experimental_rerun()

# 스테이지 2: 치환 암호
elif st.session_state.stage == 2:
    st.subheader("2단계: 알 수 없는 코드")
    st.markdown("""
    다음 방에는 알 수 없는 문자가 적힌 종이가 있다:

    `@#*!&`

    힌트: 간단한 치환 암호. 원문은 5글자. 축제를 즐길 때 사용하는 단어.
    """)

    answer2 = st.text_input("원문을 추측해보세요", key="stage2")
    if answer2.strip().lower() == "enjoy":
        st.success("정답입니다! 마지막 방으로 갑니다.")
        st.session_state.stage = 3
        st.experimental_rerun()

# 스테이지 3: 카이사르 암호
elif st.session_state.stage == 3:
    st.subheader("3단계: 고전 암호의 귀환")
    st.markdown("""
    마지막 방에는 쪽지와 알파벳 표가 있다:

    쪽지: `+3`

    암호문: `ihvwlYdo`

    (힌트: 대소문자 구분 없이 해독하되, 원래 단어는 모두 소문자로 입력하세요)
    """)

    answer3 = st.text_input("암호를 해독하라!", key="stage3")
    if answer3.strip().lower() == "festival":
        st.success("🎉 탈출 성공! 다시 축제로 돌아갑니다!")
        st.balloons()
        st.session_state.stage = 1
        st.markdown("[처음으로 돌아가기](./)")
