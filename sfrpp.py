#-------------------------------------------------------------------------#
# Pre Processed data and the pkl file generated                           #
# Will be used for Predicting price and Status.                           #
# This is achived using Streamlit application                             #
#-------------------------------------------------------------------------#
# Import all the required components                                      #
#-------------------------------------------------------------------------#
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

#-------------------------------------------#
# Read Preprecessed csv data as dataframe   #
#-------------------------------------------#

df = pd.read_csv("D:/Study/Guvi/MDTM33/0 03 Projects/1 05 Singapore Resale Flat Prices Predicting/sfrpp.csv")

town_values=list(set(df['town']))
town_values.sort()
# print(town_values)

town_encoded={town: index for index, town in enumerate(town_values)}
# print(town_encoded)

flat_type_values=list(set(df['flat_type']))
flat_type_values.sort()
# print(flat_type_values)

flat_type_encoded={flat_type: index for index, flat_type in enumerate(flat_type_values)}
# print(flat_type_encoded)

floor_area_sqm_values=list(set(df['floor_area_sqm']))
floor_area_sqm_values.sort()
# print(floor_area_sqm_values)

flat_model_values=list(set(df['flat_model']))
flat_model_values.sort()
# print(flat_model_values)

flat_model_encoded={flat_model: index for index, flat_model in enumerate(flat_model_values)}
# print(flat_model_encoded)

lease_commence_year_values=list(set(df['lease_commence_year']))
lease_commence_year_values.sort()
# print(lease_commence_year_values)

remaining_lease_values=list(set(df['remaining_lease']))
remaining_lease_values.sort()
# print(remaining_lease_values)

year_values = [year for year in range(1990, 2025)]
# print(years)

month_values = [year for year in range (1, 12)]
# print(month_values)

#-------------------------------------#
# Title                               #
#-------------------------------------#
st.markdown('<h1 style="color:#B22222;text-align: center;">Singapore Flats - Resale Price Predictor</h1>', unsafe_allow_html=True)

#-------------------------------------------#
# Build Streamlit web application           #
#-------------------------------------------#
#-------------------------------------#
# set up the sidebar with optionmenu  #
#-------------------------------------#
with st.sidebar:
    selected = option_menu("Menu",options=["Home","Price Prediction","About"],
                        icons=["house","cash",'check',"info-circle"],
                        default_index=0,
                        orientation="vertical",
                            styles={"container": {"width": "100%", "border": "2px ridge", "background-color": "#E69E7F"},
                                    "icon": {"color": "#FFFFFF", "font-size": "20px"}, 
                                    "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "color": "#000000"},
                                    "nav-link-selected": {"background-color": "#5D2D24", "color": "#E69E7F"}})


#-------------------------------#
# Home                          #
#-------------------------------#
if selected == 'Home':

    st.write('')

    st.subheader('''Singapore's public housing, managed by the Housing and Development Board (HDB),plays a crucial role in providing affordable homes to the majority of Singaporeans.
                    Here are some information about Singapore flats and the Housing landscape:''')

    st.subheader(':green[HDB Flats :]')

    st.markdown(''' These are public housing apartments built and managed by the Housing and Development Board. They come in various types, such as:''')
    
    st.markdown('''**Build-To-Order (BTO) :** Newly constructed flats offered for sale directly by HDB. Buyers can select the location and type of flat before construction begins.''')

    st.markdown('''**Sale of Balance Flats (SBF) :** Unsold flats from previous BTO launches or repossessed flats put up for sale.''')

    st.markdown('''**Resale Flats :** Flats sold by current HDB flat owners in the resale market.''')

    st.subheader(':green[Flat Types :]')

    st.markdown('''**1-Room and 2-Room Flexi :** Smaller flats suitable for singles or elderly residents.''')

    st.markdown('''**3-Room, 4-Room, and 5-Room :** Standard family-sized flats with varying numbers of bedrooms.''')

    st.markdown('''**Executive Flats :** Larger flats with additional features like balconies and study rooms.''')

    st.subheader(':green[Leasehold :]')

    st.write('''HDB flats are typically sold on a 99-year leasehold basis, meaning buyers own the flat for 99 years.''')

    st.subheader(':green[Resale Market :]')

    st.write('''In the resale market, buyers can purchase flats directly from existing owners. Prices are influenced by factors such as location, size, age of the flat, and remaining lease duration.''')

    st.subheader(':green[**New Developments :**]')

    st.write('''HDB regularly launches new BTO projects in different estates across Singapore, catering to the housing needs of different demographics.''')

    st.subheader(':green[**Ugrading Programs :**]')

    st.write('''HDB implements upgrading programs to improve the living environment of older estates, including amenities like playgrounds, fitness corners, and upgraded common areas''')

    st.subheader(':green[**Home Ownership :**]')

    st.write('''Singapore encourages home ownership through schemes like the Central Provident Fund (CPF) Housing Grant and Housing Loan for first-time buyers''')

    st.subheader(':green[**Integrated Townships :**]')

    st.write('''HDB estates are often integrated with amenities such as schools, shopping centers (like HDB Hub), transportation hubs, and parks.''')

    st.subheader(':green[**Green Initiatives :**]')

    st.write('''Recent developments focus on sustainability and green living, incorporating features like energy-efficient lighting, solar panels, and eco-friendly designs.''')

    st.subheader('''Overall, Singapore's public housing system aims to provide affordable, quality homes for its residents while promoting community living and sustainable urban development.''')

#-------------------------------#
# Price Prediction              #
#-------------------------------#
if selected == 'Price Prediction':
    title_text = '''<h1 style='font-size: 32px;text-align: center;color:#B22222;'>Copper Selling Price Prediction</h1>'''
    st.markdown(title_text, unsafe_allow_html=True)
    

    st.markdown("<h5 style=color:#006400>Provide the following Information:",unsafe_allow_html=True)
    st.write('')

    with st.form('prediction'):
        col1,col2=st.columns(2)

        with col1:

            Town_Name=st.selectbox(label='**Town Name**',options=town_values,index=None)
            Flat_type=st.selectbox(label='**Flat Type**',options=flat_type_values,index=None)
            Floor_area_sqm=st.selectbox(label='**Floor Area in Sqm [min=28.0 , max=173.0]**',options=floor_area_sqm_values,index=None)
            Flat_model=st.selectbox(label='**Flat Model**',options=flat_model_values,index=None)
            Lease_Commence_year=st.selectbox(label='**Lease Commence Year**',options=lease_commence_year_values,index=None)
        

        with col2:

            Year=st.selectbox(label='**Year [From 1990 to 2024]**',options=year_values,index=None)
            Month=st.selectbox(label='**Month [Jan - Dec]**',options=month_values,index=None)
            Remaining_Lease = st.selectbox(label='**Remaining Lease**',options=remaining_lease_values,index=None)
            Price_per_sqm=st.number_input(label='**Price Per Sqm [min=22.87 , max=89.32]**',min_value=22.869193252058544,max_value=89.31965069345043)

            st.markdown('<br>', unsafe_allow_html=True)
            button=st.form_submit_button(':red[**PREDICT**]',use_container_width=True)

    if button:
        #check whether user fill all required fields
        if not all([Town_Name, Flat_type, Flat_type, Flat_model, Lease_Commence_year, Year,
                    Month, Remaining_Lease, Price_per_sqm]):
            st.error("Data Missing, Complete all the information above.")

        else:
            
            #opened pickle model and predict the selling price with user data
            with open('D:/Study/Guvi/MDTM33/0 03 Projects/1 05 Singapore Resale Flat Prices Predicting/sfrpp_randomforestregressor.pkl','rb') as files:
                predict_model=pickle.load(files)

            # customize the user data to fit the feature 
            Town_Name=town_encoded[Town_Name]
            Flat_type=flat_type_encoded[Flat_type]
            Flat_model=flat_model_encoded[Flat_model]

            #predict the selling price with regressor model
            input_data=np.array([[Town_Name, Flat_type, Flat_type, Flat_model, Lease_Commence_year, Year,
                                    Month, Remaining_Lease, Price_per_sqm]])
            
            input=predict_model.predict(input_data)

            predict_resale_price = input[0] ** 2

            #display the predicted selling price 
            st.subheader(f":green[Predicted Resale Price :] {predict_resale_price:.2f}") 
            st.balloons()

#-------------------------------#
# About Tab                     #
#-------------------------------#
if selected == "About":
    st.subheader(':green[Project Title :]')
    st.markdown('<h5> Industrial Copper Modelling',unsafe_allow_html=True)

    st.subheader(':green[Processes :]')
    st.markdown(' <h5> Python scripting, Data Preprocessing, Machine learning, Exploratory Data Analysis, Streamlit',unsafe_allow_html=True)

    st.subheader(':green[Information :]')
    st.markdown('''**This Project - Industrial Copper Modelling was done by myself, :red[**Dinesh P K**]**''')
    st.markdown('''**To refer codes of this project, refer my Github page by clicking on the button below**''')
    st.link_button('**Go to Github**','https://github.com/vpkdinesh')