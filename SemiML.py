import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt 
plt.style.use('dark_background') ; 
st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
    st.title("Semi Automated EDA WebApp")
    st.write(" Choose your activity from the sidebar.  ")
    st.sidebar.write("""<strong style="font-size:22px">About :</strong><br>This is a WebApp built using streamlit that can be used to simplify basic EDA and visualizations.<br> Made by Sai Ram.K """,unsafe_allow_html=True)
    st.sidebar.markdown('[![Sai Ram]\
					( https://img.shields.io/github/followers/am-ram?color=cyan&label=am-ram&logo=github&logoColor=white&style=for-the-badge)]\
					(https://github.com/am-ram)')
    activities = ["EDA" , "PLOT"]
    st.sidebar.write("""<strong style="font-size:18px">Select Activity To Perform : </strong>""",unsafe_allow_html=True)
    choice = st.sidebar.radio(" " ,activities)
    st.sidebar.write('**<strong style="font-size:22px"><br><br><br>FAQs**</strong>',unsafe_allow_html=True)
    st.sidebar.markdown('**What happens to my data?**')
    st.sidebar.markdown('The data you upload is not saved anywhere on this site or any 3rd party site i.e, not in any storage like DB/FileSystem/Logs.')   

    if choice == "EDA":
        st.subheader("|  Exploratory Data Analysis  |")
        st.write(""" <strong><p style="font-size: 42px">Upload Your Dataset Here</p></strong> """,unsafe_allow_html=True)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])   
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)
            if st.checkbox("SHOW SHAPE"):
                st.write(df.shape)
            if st.checkbox("SHOW SIZE"):
                st.write(df.size)
            if st.checkbox("SHOW COLUMN "):
                st.write(df.columns)
            if st.checkbox("SELECT COLUMN NAME"):
                select_columns = st.multiselect("Select Column" , df.columns)
                new_df = df[select_columns]
                st.dataframe(new_df)
            if st.checkbox("SHOW MISSING VALUES"):
                st.write(df.isna().sum())
            if st.checkbox("SHOW VALUE COUNTS"):
                column = st.selectbox("Select Columns" , df.columns)
                st.write(df[column].value_counts())
            if st.checkbox("SHOW SUMMARY"):
                st.write(df.describe())


    elif choice == "PLOT":
        st.subheader("|  Data Visualization  |")
        st.write(""" <strong><p style="font-size: 42px">Upload Your Dataset Here</p></strong> """,unsafe_allow_html=True)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)

            if st.checkbox("CORRELATION"):
                st.write(sb.heatmap(df.corr() , annot = True,cmap="Blues"))
                st.pyplot()

            if st.checkbox("BAR GRAPH"):
                x_axis = st.selectbox("Select x axis:" , df.columns)
                x_axis = df[x_axis]
                y_axis = st.selectbox("Select y axis:" , df.columns)
                y_axis = df[y_axis]
                st.write(sb.barplot(x_axis , y_axis,palette="Blues_d"))
                st.pyplot()
                plt.xticks(rotation = 90)
                plt.legend()
                plt.grid()

            
            if st.checkbox("COUNT PLOT"):
                c = st.selectbox("Select  axis:" , df.columns)
                c_main = df[c]
                st.write(sb.countplot(c_main))
                st.pyplot()
                plt.grid()
                plt.xticks(rotation = 90)
                plt.legend()
                


            if st.checkbox("PIE CHART"):
                col = st.selectbox("Select 1 column" , df.columns)
                pie = df[col].value_counts().plot.pie(autopct = "%1.1f%%")
                st.write(pie)
                st.pyplot()

            
    else:
        st.write(""" <strong><p style="font-size: 42px">Thank You For Using This WebApp.</p></strong> """,unsafe_allow_html=True)

       
if __name__ == "__main__":
    main()
