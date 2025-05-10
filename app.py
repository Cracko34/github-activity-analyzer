import streamlit as st
from github_api import fetch_contributors, fetch_commits
from data_analysis import process_contributors, process_commits

st.set_page_config(page_title="GitHub Activity Analyzer", layout="wide")
st.title("📊 GitHub Activity Analyzer")

owner = st.sidebar.text_input("Owner", "pandas-dev")
repo  = st.sidebar.text_input("Repo", "pandas")

if st.sidebar.button("Actualizar datos"):
    with st.spinner("Obteniendo datos…"):
        contribs = fetch_contributors(owner, repo)
        commits = fetch_commits(owner, repo, per_page=200)

        df_contribs = process_contributors(contribs)
        df_commits = process_commits(commits)

        st.subheader("🏆 Top Contribuidores")
        st.dataframe(df_contribs)

        st.subheader("📈 Commits por Día")
        st.line_chart(df_commits.set_index('day'))

        st.success("¡Datos actualizados!")
