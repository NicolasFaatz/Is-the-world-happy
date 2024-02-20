import pandas as pd
from datetime import datetime
import pycountry
import geopandas

def datacutting(x):
    name1="WeatherEvents_Jan2016-Dec2022.csv"
    name2="WeatherEvents_Aug16_Dec20_Publish.csv"
    name3="TrafficEvents_Aug16_Dec20_Publish.csv"

    form="%Y-%m-%d %H:%M:%S"

    df=pd.read_csv(x,parse_dates=["StartTime(UTC)","EndTime(UTC)"],date_parser=lambda x:datetime.strptime(x,form))
    if x==name1:
        y=7
        df_weather=df.drop(columns=["TimeZone","County","AirportCode","ZipCode"])
        for i in range(y):
            filt=(df_weather["StartTime(UTC)"]<pd.to_datetime(str(2017+i)+"-01-01"))&(df_weather["StartTime(UTC)"]>pd.to_datetime(str(2015+i)+"-12-31"))
            x=df_weather[filt]
            x.to_csv(str(2016+i)+".csv")
    elif x==name2:
        y=5
        df_weather=df.drop(columns=["TimeZone","County","AirportCode","ZipCode"])
        for i in range(y):
            filt=(df_weather["StartTime(UTC)"]<pd.to_datetime(str(2017+i)+"-01-01"))&(df_weather["StartTime(UTC)"]>pd.to_datetime(str(2015+i)+"-12-31"))
            x=df_weather[filt]
            x.to_csv(str(2016+i)+"_public.csv")
    elif x==name3:
        y=5
        df_traffic=df.drop(columns=["TimeZone","County","AirportCode","ZipCode","Side","Distance(mi)","Description"])
        for i in range(y):
            filt=(df_traffic["StartTime(UTC)"]<pd.to_datetime(str(2017+i)+"-01-01"))&(df_traffic["StartTime(UTC)"]>pd.to_datetime(str(2015+i)+"-12-31"))
            x=df_traffic[filt]
            x.to_csv(str(2016+i)+"_public_traffic.csv")
    
def alpha3code(column):
    CODE=[]
    for country in column:
        try:
            code=pycountry.countries.get(name=country).alpha_3
           # .alpha_3 means 3-letter country code 
           # .alpha_2 means 2-letter country code
            CODE.append(code)
        except:
            CODE.append('None')
    return CODE
# create a column for code 


df=pd.read_csv("2015.csv")
#df["Economy (GDP per Capita)"]=df["Economy (GDP per Capita)"].astype(float)
#filt=df["Economy (GDP per Capita)"]==df["Economy (GDP per Capita)"].min()
#print(df[filt],df.tail())

df['CODE']=alpha3code(df["Country"])
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.rename(columns={'iso_a3':"CODE"},inplace=True)
#world.columns=['pop_est', 'continent', 'name', 'CODE', 'gdp_md_est', 'geometry']
print(world.columns,df.columns)
# then merge with our data 
merge=pd.merge(world,df,on='CODE')
#merge.plot(column='Happiness Rank', scheme="quantiles",figsize=(25, 20),legend=True,cmap='coolwarm')
merge.plot(column='Happiness Rank', scheme="quantiles",figsize=(25, 20),legend=True,cmap='coolwarm')
#print(df.head())
#df2=df.drop(columns=["TimeZone","County","AirportCode","ZipCode"])
#print(df.isnull().sum(),len(df["Country"]))

