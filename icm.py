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

df = pd.read_csv("D:/Study/Guvi/MDTM33/0 03 Projects/1 04 Copper Data Modeling/icm_preprocessed.csv")

country_values=list(set(df['country']))
country_values.sort()
# print(country_values)

status_values=list(set(df['status']))
# print(status_values)

status_encoded = {'Lost':0, 'Won':1, 'Draft':2, 'To be approved':3, 'Not lost for AM':4,'Wonderful':5, 'Revised':6,
                    'Offered':7, 'Offerable':8}
item_type_values=list(set(df['item_type']))
# print(item_type_values)

item_type_encoded = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}
product_ref_values=list(set(df['product_ref']))
product_ref_values.sort()
# print(product_ref_values)

application_values=list(set(df['application']))
application_values.sort()
# print(application_values)

#-------------------------------------#
# Title                               #
#-------------------------------------#
st.markdown('<h1 style="color:#B22222;text-align: center;">Industrial Copper Modelling</h1>', unsafe_allow_html=True)

#-------------------------------------------#
# Build Streamlit web application           #
#-------------------------------------------#
#-------------------------------------#
# set up the sidebar with optionmenu  #
#-------------------------------------#
with st.sidebar:
    selected = option_menu("Menu",options=["Home","Price Prediction","Status Prediction","About"],
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
    title_text = '''<h1 style='font-size: 30px;text-align: center; color:#B22222;'> COPPER : Properties & Applications </h1>'''
    st.markdown(title_text, unsafe_allow_html=True)

    st.subheader(":green[Copper :]")

    st.markdown('''Copper is one of the few metals that can occur in nature in a directly usable metallic form (native metals).
                This led to very early human use in several regions, from 8000 BC. Thousands of years later, it was the first metal to be smelted from sulfide ore in
                5000 BC; the first metal to be cast into a shape in a mold in 4000 BC; and the first metal to be purposely alloyed with another metal, tin,
                to create bronze 3500 BC.
                Copper is a versatile and widely used metal known for its excellent electrical conductivity,thermal conductivity, malleability
                and resistance to corrosion.
                Copper is a chemical element; it has symbol Cu (from Latin cuprum) and atomic number 29.
                It is a soft, malleable, and ductile metal with very high thermal and electrical conductivity.
                A freshly exposed surface of pure copper has a pinkish-orange color. Copper is used as a conductor of heat and electricity, as a building material
                and as a constituent of various metal alloys, such as sterling silver used in jewelry, cupronickel used to make marine hardware and coins
                and constantan used in strain gauges and thermocouples for temperature measurement.''')

    st.subheader(':green[Properties of Copper :]')

    st.markdown(''':orange[**Electrical Conductivity :**] Copper has the highest electrical conductivity of any non-precious metal,
                        making it ideal for electrical wiring.''')
    
    st.markdown(''':orange[**Thermal Conductivity :**] It is an excellent conductor of heat, which makes it useful in heat exchangers and cookware.''')
    st.markdown(''':orange[**Corrosion Resistance :**] Copper forms a protective oxide layer that helps resist corrosion, especially in moist environments.''')
    st.markdown(''':orange[**Malleability and Ductility :**] Copper can be easily shaped and drawn into wires without breaking.''')
    st.markdown(''':orange[**Antimicrobial Properties :**] Copper has natural antimicrobial properties, which help reduce the spread of harmful bacteria..''')
    st.subheader(":green[Applications of Copper :]")

    st.write("1. Electrical and Electronics")
    st.write("2. Construction and Architecture")
    st.write("3. Transportation")
    st.write("4. Industrial Machinery")
    st.write("5. Consumer Products")
    st.write("6. Renewable Energy")

    st.subheader(":green[Environmental and Health Considerations :]")
    st.markdown(''':orange[**Recyclability :**] Copper is 100 Percent recyclable without any loss of quality, making it an environmentally friendly material.''')
    st.markdown(''':orange[**Health Benefits :**] Copper's antimicrobial properties are utilized in healthcare settings to reduce the spread of infections.''')

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

            Item_Date=st.date_input(label='**Item Date**',format='DD/MM/YYYY')
            Country=st.selectbox(label='**Country**',options=country_values,index=None)
            Item_Type=st.selectbox(label='**Item Type**',options=item_type_values,index=None)
            Application=st.selectbox(label='**Application**',options=application_values,index=None)
            Product_Ref=st.selectbox(label='**Product Ref**',options=product_ref_values,index=None)
            Customer_Id=st.number_input('**Customer ID**',min_value=10000)

        with col2:

            Delivery_Date=st.date_input(label='**Delivery Date**',format='DD/MM/YYYY')
            Status=st.selectbox(label='**Status**',options=status_values,index=None)
            Quantity=st.number_input(label='**Quantity**',min_value=0.1)
            Width=st.number_input(label='**Width**',min_value=1.0)
            Thickness=st.number_input(label='**Thickness**',min_value=0.1)

            st.markdown('<br>', unsafe_allow_html=True)
            button=st.form_submit_button(':red[**Predict Selling Price**]',use_container_width=True)

    if button:
        #check whether user fill all required fields
        if not all([Item_Date, Delivery_Date, Country, Item_Type, Application, Product_Ref,
                    Customer_Id, Status, Quantity, Width, Thickness]):
            st.error("Data Missing, Complete all the information above.")

        else:
            
            #opened pickle model and predict the selling price with user data
            with open('D:/Study/Guvi/MDTM33/0 03 Projects/1 04 Copper Data Modeling/Random_forest_regressor.pkl','rb') as files:
                predict_model=pickle.load(files)

            # customize the user data to fit the feature 
            Status=status_encoded[Status]
            Item_Type=item_type_encoded[Item_Type]
            Delivery_Time_Taken=abs((Item_Date - Delivery_Date).days)
            Quantity_Log=np.log(Quantity)
            Thickness_Log=np.log(Thickness)
            #predict the selling price with regressor model
            user_data=np.array([[Customer_Id, Country, Status, Item_Type ,Application, Width, Product_Ref,
                                Delivery_Time_Taken, Quantity_Log, Thickness_Log]])
            pred=predict_model.predict(user_data)
            selling_price_pred=np.exp(pred[0])

            #display the predicted selling price 
            st.subheader(f":green[Predicted Selling Price :] {selling_price_pred:.2f}") 

#-------------------------------#
# Status Prediction             #
#-------------------------------# 
if selected == 'Status Prediction':
    title_text = '''<h1 style='font-size: 32px;text-align: center;color:#B22222;'>Copper Status Prediction</h1>'''
    st.markdown(title_text, unsafe_allow_html=True)
    st.markdown("<h5 style=color:#006400;>Provide the following information:",unsafe_allow_html=True)
    st.write('')

    #creted form to get the user input 
    with st.form('classifier'):
        col1,col2=st.columns(2)
        with col1:

            Item_Date=st.date_input(label='**Item Date**',format='DD/MM/YYYY')
            Country=st.selectbox(label='**Country**',options=country_values,index=None)
            Item_Type=st.selectbox(label='**Item Type**',options=item_type_values,index=None)
            Application=st.selectbox(label='**Application**',options=application_values,index=None)
            Product_Ref=st.selectbox(label='**Product Ref**',options=product_ref_values,index=None)
            Customer_Id=st.number_input('**Customer ID**',min_value=10000)

        with col2:

            Delivery_Date=st.date_input(label='**Delivery Date**',format='DD/MM/YYYY')
            Quantity=st.number_input(label='**Quantity**',min_value=0.1)
            Width=st.number_input(label='**Width**',min_value=1.0)
            Thickness=st.number_input(label='**Thickness**',min_value=0.1)
            Selling_Price=st.number_input(label='**Selling Price**',min_value=0.1)

            st.markdown('<br>', unsafe_allow_html=True)      
            button=st.form_submit_button(':red[**Predict Copper Status**]',use_container_width=True)

    if button:
        #check whether user fill all required fields
        if not all([Item_Date, Delivery_Date, Country, Item_Type, Application, Product_Ref,
                    Customer_Id,Quantity, Width,Selling_Price]):
            st.error("Please fill in all required fields.")

        else:
            #opened pickle model and predict status with user data
            with open('D:/Study/Guvi/MDTM33/0 03 Projects/1 04 Copper Data Modeling/Extra_trees_classifier.pkl','rb') as files:
                model=pickle.load(files)

            # customize the user data to fit the feature 
            Item_Type=item_type_encoded[Item_Type]
            Delivery_Time_Taken=abs((Item_Date - Delivery_Date).days)
            Quantity_Log=np.log(Quantity)
            Thickness_Log=np.log(Thickness)
            Selling_Price_Log=np.log(Selling_Price)
            #predict the status with classifier model
            user_data=np.array([[Customer_Id, Country,Item_Type ,Application, Width, Product_Ref,
                                Delivery_Time_Taken, Quantity_Log, Thickness_Log,Selling_Price_Log]])
            status=model.predict(user_data)

            #display the predicted status 
            if status==1:
                st.subheader(f":green[Status of the Copper :] Won")

            else:
                st.subheader(f":red[Status of the Copper :] Lost")

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