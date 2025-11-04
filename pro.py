import streamlit as st 
import pandas as pd 


new_movies =pd.read_csv(r"C:\Users\hp\Downloads\new_movies (1).csv")

# get vote category
vot_cat=new_movies["Vote_Avg"].unique().tolist()
vot_cat.insert(0,"all movies")

# for adult coloumn
def change_adult(x):
  if x==True:
    return "Adult Movie"
  else:
    return "Not Adult Movie"


new_movies["adult_cat"]=new_movies["adult"].apply(change_adult)
adult_cart=new_movies["adult_cat"].unique().tolist()
adult_cart.insert(0,"all movies")

# revenue cater
revenue_cart=new_movies["revenue_category"].unique().tolist()
revenue_cart.insert(0,"all movies")




st.sidebar.header("Movies Filter")
votes=st.sidebar.selectbox("Choose a vote filter",vot_cat)
adult=st.sidebar.selectbox("Choose Adult or Not",adult_cart)
revenue=st.sidebar.selectbox("Chooose Revenue Option",revenue_cart)

filltered_data=new_movies.copy()

if votes!="all movies":
  filltered_data=filltered_data[filltered_data["Vote_Avg"]==votes].reset_index(drop=True)


if adult!="all movies":
  filltered_data=filltered_data[filltered_data["adult_cart"]==adult].reset_index(drop=True)



if revenue!="all movies":
  filltered_data=filltered_data[filltered_data["revenue_category"]==revenue].reset_index(drop=True)





st.sidebar.button("Get Movies")
st.header(f"Total Movies({filltered_data.shape[0]})")



for i in range(0,new_movies[0 : 30].shape[0],3):
  rows=new_movies.iloc[i : i + 3]
  cols=st.columns(3)

  if votes=="all movies" and adult=="all movies" and revenue=="all movies":


    
    for idx,movie in rows.iterrows():
      with cols[idx % 3]:
    
    

      #  for idx,movie in rows.iterrows():
        st.image(f"https://image.tmdb.org/t/p/original/{movie.poster_path}")
        st.write(f"{movie.title}")
        st.write(f"Total Revenue:{movie.revenue}")
        st.markdown(f"""
                  -{movie.tagline}
                  -Total Revenue of movie is:{movie.revenue} and Movie 
                  release date :{movie.release_date}

                    """)













# st.dataframe(new_movies)