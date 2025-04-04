import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt 
import streamlit as st 

st.title("Esto es una app")

tgp_MASC = gpd.read_file("hombres.geojson")
tgp_FEM = gpd.read_file("mujeres.geojson")

fig, ax = plt.subplots(1,2,figsize=(10,6))

tgp_MASC.plot(column="FT", ax=ax[0], legend=True, vmin = 0.2, vmax = 1)
tgp_FEM.plot(column="FT", ax=ax[1], legend=True, vmin = 0.2, vmax = 1)

ax[0].set_title("TGP = HOMBRES")
ax[1].set_title("TGP = MUJERES")



st.pyplot(fig)