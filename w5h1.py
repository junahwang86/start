import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# API 키 입력 받기
api_key = st.text_input("Google API Key를 입력하세요", type="password")

if api_key:
    # 6하원칙 입력 받기
    st.subheader("6하원칙을 입력해주세요")
    who = st.text_input("누가")
    what = st.text_input("무엇을") 
    when = st.text_input("언제")
    where = st.text_input("어디서")
    why = st.text_input("왜")
    how = st.text_input("어떻게")

    # 생성 버튼
    if st.button("작문 생성하기"):
        try:
            # Gemini 모델 초기화
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-pro-latest",
                google_api_key=api_key,
                temperature=0.7
            )

            # 프롬프트 템플릿 생성
            template = """
            다음 6하원칙을 바탕으로 자연스러운 글을 작성해주세요:
            - 누가: {who}
            - 무엇을: {what}
            - 언제: {when}
            - 어디서: {where}
            - 왜: {why}
            - 어떻게: {how}
            """

            prompt = PromptTemplate(
                input_variables=["who", "what", "when", "where", "why", "how"],
                template=template
            )

            # 최종 프롬프트 생성
            final_prompt = prompt.format(
                who=who,
                what=what,
                when=when,
                where=where,
                why=why,
                how=how
            )

            # 결과 생성
            response = llm.invoke(final_prompt)
            
            # 결과 출력
            st.subheader("생성된 작문")
            st.write(response.content)

        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
else:
    st.warning("API 키를 입력해주세요.")

