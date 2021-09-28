import pandas as pd
import csv

df=pd.read_csv("final.csv")
print(df.shape)
"""
del df["hyperlink"]
del df["temp_planet_mass"]
del df["pl_letter"]
del df["pl_controvflag"]
del df["pl_name"]
del df["pl_orbper"]
del df["pl_pnum"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbperlim"]
del df["pl_orbsmax"]
del df["pl_orbsmaxerr1"]
del df["pl_orbsmaxerr2"]
del df["pl_orbsmaxlim2"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df["pl_orbeccenerr"]
del df["pl_orbeccenlim"]
del df["pl_orbinclerr1"]
del df["pl_orbinclerr2"]
del df["pl_orbincllim"]
del df["pl_bmassj"]
del df["pl_bmassjerr1"]
del df["pl_bmassjerr2"]
del df["pl_bmassjlim"]
del df["pl_bmassprov"]
del df["pl_radj"]
del df["pl_radjerr1"]
del df["pl_radjerr2"]
del df["pl_radjlim"]
del df["pl_denserr1"]
del df["pl_denserr2"]
del df["pl_denslim"]
del df["pl_ttvflag"]
del df["pl_kepflag"]
del df["pl_k2flag"]
del df["pl_nnotes"]
del df["radec"]
del df["st_dist"]
del df["st_disterr1"]
del df["st_disterr2"]
del df["st_distlimgaia_dist"]
del df["gaia_disterr1"]
del df["gaia_disterr2"]
del df["gaia_distlim"]
del df["st_optmag"]
del df["st_optmagerr"]
del df["st_optmaglim"]
del df["st_optband"]
del df["gaia_gmag"]
del df["gaia_gmagerr"]
del df["gaia_gmaglim"]
del df["st_tefferr1"]
del df["st_tefferr2"]
del df["st_tefflim"]
del df["st_masserr1"]
del df["st_masserr2"]
del df["st_masslim"]
del df["st_raderr1"]
del df["st_raderr2"]
del df["st_radlim"]
del df["rowupdate"]
del df["pl_facility"]

"""
a = list(df)
b=['hyperlink', 'temp_planet_date', 'pl_letter', 'pl_name', 'pl_controvflag', 'pl_pnum', 'pl_orbper', 'pl_orbpererr1', 'pl_orbpererr2', 'pl_orbperlim', 'pl_orbsmax', 'pl_orbsmaxerr1', 'pl_orbsmaxerr2', 'pl_orbsmaxlim', 'pl_orbeccen', 'pl_orbeccenerr1', 'pl_orbeccenerr2', 'pl_orbeccenlim',  'pl_orbinclerr1', 'pl_orbinclerr2', 'pl_orbincllim', 'pl_bmassj', 'pl_bmassjerr1', 'pl_bmassjerr2', 'pl_bmassjlim', 'pl_bmassprov', 'pl_radj', 'pl_radjerr1', 'pl_radjerr2', 'pl_radjlim',  'pl_denserr1', 'pl_denserr2', 'pl_denslim', 'pl_ttvflag', 'pl_kepflag', 'pl_k2flag', 'pl_nnotes',  'ra',  'dec', 'st_dist', 'st_disterr1', 'st_disterr2', 'st_distlim', 'gaia_dist', 'gaia_disterr1', 'gaia_disterr2', 'gaia_distlim', 'st_optmag', 'st_optmagerr', 'st_optmaglim', 'st_optband', 'gaia_gmag', 'gaia_gmagerr', 'gaia_gmaglim', 'st_tefferr1', 'st_tefferr2', 'st_tefflim',  'st_masserr1', 'st_masserr2', 'st_masslim', 'st_raderr1', 'st_raderr2', 'st_radlim', 'rowupdate', 'pl_facility']
print(a)
for i in b :
    del df[i] 
print(df.shape)


df=df.rename({"pl_hostname" : "solar_system_name" , "pl_discmethod" : "planet_discovery_method",
"pl_orbincl" : "planet_orbital_inclination", "pl_dens" : "planet_density",
"ra_str" : "right_asension" , "dec_str" : "declination" , "st_teff" : "host_temperature"},axis = "columns")