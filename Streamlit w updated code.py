# import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
excel_file = 'C:\\Users\\mab075\\OneDrive - University of Arkansas\\FINN\\advanced modeling\\a personal project\\Pics turned into tables.xlsx'
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Initialize a select box for the user to choose a company
selected_company = st.selectbox('Select a company', list(all_sheets.keys()))

# Display the selected company's data
st.write('Market Capitalization Data for:', selected_company)
st.write(all_sheets[selected_company])

# Plot and display the market cap comparison as a bar chart
market_caps = [{'Company': sheet, 'Mkt Cap (M)': df.iloc[0]['Mkt Cap (M)']} for sheet, df in all_sheets.items()]
market_caps_df = pd.DataFrame(market_caps)
market_caps_sorted = market_caps_df.sort_values('Mkt Cap (M)', ascending=False)

# Create a horizontal bar plot
plt.figure(figsize=(10, 8))
sns.barplot(data=market_caps_sorted, y='Company', x='Mkt Cap (M)', orient='h')
plt.title('Market Capitalization Comparison of Companies')
st.pyplot(plt)

# Save the plot as a PDF
plt.tight_layout()  # Adjust the padding to make space for rotated labels
plt.savefig('Companies_Market_Cap_Comparison.pdf', bbox_inches='tight')

# Show the plot
plt.show()
# %%
