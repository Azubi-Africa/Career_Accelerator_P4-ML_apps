import streamlit as st


def main():
    st.set_page_config(page_title="Demo app", page_icon="🐞", layout="centered")

    st.title("🐞 Demo app!")

    st.sidebar.write(f"Demo app")
    st.sidebar.write(f"This app shows a simple demo of a Streamlit app.")

    form = st.form(key="annotation")

    with form:
        cols = st.columns((1, 1))
        author = cols[0].text_input("Report author:")
        bug_type = cols[1].selectbox(
            "Bug type:", ["Front-end", "Back-end", "Data related", "404"], index=2
        )
        comment = st.text_area("Comment:")
        cols = st.columns(2)
        date = cols[0].date_input("Bug date occurrence:")
        bug_severity = cols[1].slider("Bug severity:", 1, 5, 2)
        submitted = st.form_submit_button(label="Submit")

    if submitted:
        st.success("Thanks!")
        st.balloons()

    expander = st.expander("See all records")
    with expander:
        pass
        # st.dataframe()


if __name__ == "__main__":
    main()
