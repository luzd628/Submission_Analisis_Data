import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 


# Helper Function
def total_rent_bike_by_hour(df):
    rent_bike_by_hour_df = df.groupby(by='hr').cnt.sum().reset_index()
    return rent_bike_by_hour_df

def total_rent_bike_by_day(df):
    rent_bike_by_day_df = df.groupby(by='weekday').cnt.sum().reset_index()
    return rent_bike_by_day_df

def total_rent_bike_by_weather(df):
    rent_bike_by_weather = df.groupby(by='weathersit').cnt.sum().reset_index()
    return rent_bike_by_weather

def total_rent_bike_by_season(df):
    rent_bike_by_season_df = df.groupby(by='season').cnt.sum().reset_index()
    return rent_bike_by_season_df



st.header('Bike Sharing Dashboard :sparkles:')

st.markdown(
    """
    Hai, Welcome into Bike Sharing Data Dashboard
    This page presents some data related to the use of bicycle rentals with several variables. These variables include Time, Day, Weather and Season

    Hopefully the data presented below can help to provide new insights for you
    """
)

# Load Csv
df = pd.read_csv("dashboard/main_data.csv")


min_date = df["dteday"].min()
max_date = df["dteday"].max()

# Sidebar
with st.sidebar:
    st.image("logo.jpg")
    start_date, end_date = st.date_input(
        label="Rentang Waktu", min_value=min_date,
        max_value=max_date,
        value=[min_date,max_date]
    )

main_df = df[(df["dteday"] >= str(start_date)) &
             (df["dteday"] <= str(end_date))]

rent_by_hour = total_rent_bike_by_hour(main_df)
rent_by_day = total_rent_bike_by_day(main_df)
rent_by_weather = total_rent_bike_by_weather(main_df)
rent_by_season = total_rent_bike_by_season(main_df)

st.subheader("Hourly Bike Rental Users")
st.text('The number of times a bicycle rental service is used within a time span of hours per day.')

fig, ax = plt.subplots(figsize=(16,8))
ax.plot(
    rent_by_hour["hr"],
    rent_by_hour["cnt"],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)

ax.set_xlabel("Hours in a day")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xticks(rent_by_hour['hr'])
 
st.pyplot(fig)

fig2, ax = plt.subplots(figsize=(20, 10))
st.subheader(" Number of Bike Renters Each Day of the Week ")
sns.barplot(
    x="weekday", 
    y="cnt",
    data=rent_by_day.sort_values(by="cnt", ascending=False),
    palette=["#4D55CC", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"],
    ax=ax
)
ax.set_title("Number of Renters by Day", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig2)

st.subheader("Renters by Weather and Season")
col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
 
    sns.barplot(
        y="cnt", 
        x="weathersit",
        data=rent_by_weather.sort_values(by="weathersit", ascending=True),
        palette=["#4D55CC", "#D3D3D3", "#D3D3D3", "#D3D3D3"],
        ax=ax
    )
    ax.set_title("Number of Renters by Weather", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=28)
    ax.tick_params(rotation=10)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    sns.barplot(
        y="cnt", 
        x="season",
        data=rent_by_season.sort_values(by="season", ascending=True),
        palette=["#4D55CC", "#D3D3D3", "#D3D3D3", "#D3D3D3"],
        ax=ax
    )
    ax.set_title("Number of Renters by Season", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

st.subheader ("Conclusion")
st.markdown(
    """
    1. Users renting bicycles in one day experience fluctuations where, renters will increase at 8 am then decrease until it will increase to its highest number at 5 pm. This is related to the 9-5 working hours in the United States at that time, so the use of rental bicycles will increase during the departure and return hours of the office.

    2. Weathers greatly influences the number of bike renters, renters tend to rent a bike when the weather is sunny, and will drop significantly when the weather is cloudy and even no renters when the weather is heavy rain and stormy. In autumn, the number of bike renters is also at its highest compared to other seasons, where the season tends to have friendly weather.

    """)