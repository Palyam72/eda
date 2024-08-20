import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

class Report:
    def __init__(self):
        pass

    def create_report(self, times):
        for i in range(times):
            dataset = st.sidebar.file_uploader(f"Upload CSV File {i+1}", type=["csv"])
            if dataset:
                df = pd.read_csv(dataset)
                profile = ProfileReport(df, title=f"Dataset {i+1} Profiling Report")
                st_profile_report(profile)

# Main Streamlit app
times = st.number_input("Enter the number of datasets you want to visualize", min_value=1, step=1)
if times:
    report = Report()
    report.create_report(times)
