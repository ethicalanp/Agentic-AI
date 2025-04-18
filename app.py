import streamlit as st 
from BasicAgent.agentMemory import get_answer


st.set_page_config(page_title="Interior Design Consultant ", page_icon="🎨")

st.title("Interior Design Consultant ")
st.markdown("Ask me anything about Interior Designing!!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


user_input = st.text_input("Ask yor question ...")

if user_input:
    with st.spinner("Thinking..."):
        response =get_answer(user_input)
        st.session_state.chat_history.append(("You",user_input))
        st.session_state.chat_history.append(("Agent",response))


for role, msg in st.session_state.chat_history:
    if role == "You" :
        st.markdown(f"You :{msg}")
    else:
        st.markdown(f"Agent :{msg}")
 