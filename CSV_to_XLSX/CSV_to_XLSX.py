import streamlit as st
import pandas as pd

# Title of the web app
st.title("CSV to XLSX Converter")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the contents of the CSV file
    st.write("Contents of the CSV file:")
    st.dataframe(df)

    # Convert the DataFrame to XLSX format
    xlsx_file = f"{uploaded_file.name.split('.')[0]}.xlsx"
    
    # Create a download button for the XLSX file
    if st.button("Convert to XLSX"):
        with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Provide a download link for the XLSX file
        st.download_button(
            label="Download XLSX file",
            data=open(xlsx_file, 'rb').read(),
            file_name=xlsx_file,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
