import pandas as pd
import numpy as np

VA_zips = [20109, 20110, 20111, 20112, 20120, 20121, 20124, 20136,
  20147, 20148, 20151, 20152, 20164, 20165, 20166, 20170, 20171, 20190, 20191,
  20194, 22003, 22015, 22020, 22025, 22026, 22027, 22030, 22031, 22032, 22033,
  22039, 22041, 22042, 22043, 22044, 22046, 22060, 22066, 22079, 22081, 22101,
  22102, 22124, 22134, 22150, 22151, 22152, 22153, 22172, 22180, 22181, 22182,
  22191, 22192, 22193, 22201, 22202, 22203, 22204, 22205, 22206, 22207, 22209,
  22213, 22301, 22302, 22303, 22304, 22305, 22306, 22307, 22308, 22309, 22310,
  22311, 22312, 22314, 22315, 23888, 24281]
MD_zips = [20601, 20602, 20603, 20607, 20611, 20613, 20616, 20637,
   20639, 20640, 20646, 20675, 20695, 20705, 20706, 20707, 20708, 20710, 20712,
   20714, 20715, 20716, 20720, 20721, 20722, 20723, 20724, 20732, 20733, 20735,
   20737, 20738, 20740, 20742, 20743, 20744, 20745, 20746, 20747, 20748, 20751,
   20754, 20758, 20759, 20763, 20764, 20769, 20770, 20772, 20774, 20777, 20778,
   20781, 20782, 20783, 20784, 20785, 20794, 20814, 20815, 20816, 20817, 20818,
   20832, 20837, 20841, 20850, 20851, 20852, 20853, 20854, 20855, 20860, 20866,
   20871, 20872, 20874, 20876, 20877, 20878, 20879, 20882, 20886, 20895, 20901,
   20902, 20903, 20904, 20905, 20906, 20910, 20911, 20912, 21012, 21029, 21032,
   21037, 21042, 21043, 21044, 21045, 21046, 21054, 21060, 21061, 21075, 21076,
   21090, 21104, 21108, 21113, 21114, 21117, 21122, 21128, 21140, 21144, 21146,
   21163, 21208, 21227, 21228, 21229, 21234, 21236, 21401, 21402, 21403, 21409]

def Employ_prep(DC, MD, VA):
    #DC
    DC.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    DC_emp = DC
    #Maryland
    MD.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    MD_emp = MD[MD['ZIPCODE'].isin(MD_zips)]
    #Virginia
    VA.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    VA_emp = VA[VA['ZIPCODE'].isin(VA_zips)]
    Employment = pd.concat([DC_emp, MD_emp, VA_emp])
    return(Employment)

def Healthcare_prep(DC, MD, VA):
    #DC
    DC.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    DC_health = DC
    #Maryland
    MD.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    MD_health = MD[MD['ZIPCODE'].isin(MD_zips)]
    #Virginia
    VA.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    VA_health = VA[VA['ZIPCODE'].isin(VA_zips)]
    Healthcare = pd.concat([DC_health, MD_health, VA_health])
    return(Healthcare)

def Income_prep(DC, MD, VA):
    #DC
    DC.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    DC_inc = DC
    #Maryland
    MD.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    MD_inc = MD[MD['ZIPCODE'].isin(MD_zips)]
    #Virginia
    VA.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    VA_inc = VA[VA['ZIPCODE'].isin(VA_zips)]
    Income = pd.concat([DC_inc, MD_inc, VA_inc])
    return(Income)

def Social_prep(DC, MD, VA):
    #DC
    DC.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    DC_soc = DC
    #Maryland
    MD.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    MD_soc = MD[MD['ZIPCODE'].isin(MD_zips)]
    #Virginia
    VA.rename(columns={'GEO.id': 'ID', 'GEO.id2': 'ZIPCODE', 'GEO.display-label': 'Label'}, inplace=True)
    VA_soc = VA[VA['ZIPCODE'].isin(VA_zips)]
    Social = pd.concat([DC_soc, MD_soc, VA_soc])
    return(Social)

def Full_merge(Employment, Healthcare, Income, Social):
    Merged = pd.concat([Employment, Healthcare, Income, Social],axis=1)
    return(Merged)

#File Paths
DCE = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_DC/DC_Employ_Chars_2015.csv',encoding="Latin1")
DCH = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_DC/DC_Healthcare_2015.csv',encoding="Latin1")
DCI = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_DC/DC_IncomeChars_2015.csv',encoding="Latin1")
DCS = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_DC/DC_SocialChars_2015.csv',encoding="Latin1")

VAE = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_VA/VA_Employ_chars_2015.csv',encoding="Latin1")
VAH = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_VA/VA_Healthcare_2015.csv',encoding="Latin1")
VAI = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_VA/VA_Income_chars_2015.csv',encoding="Latin1")
VAS = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_VA/VA_Social_chars_2015.csv',encoding="Latin1")

MDE = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_MD/MD_Employ_Chars_2015.csv',encoding="Latin1")
MDH = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_MD/MD_Healthcare_2015.csv',encoding="Latin1")
MDI = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_MD/MD_Income_chars_2015.csv',encoding="Latin1")
MDS = pd.read_csv('/Users/MaggieCorry/Documents/Georgetown/Capstone/FactFinder_Data/Raw_Data_MD/MD_Social_chars_2015.csv',encoding="Latin1")

#Wrangle the data
Employment = Employ_prep(DCE, VAE, MDE)
Healthcare = Healthcare_prep(DCH, VAH, MDH)
Income = Income_prep(DCI, VAI, MDI)
Social = Social_prep(DCS, VAS, MDS)
#Merge the four
Merged = Full_merge(Employment, Healthcare, Income, Social)

def na_fix(Merged):
    Working = Merged.replace(['(X)', '**', '-'],["NaN", 0, 0])
    Working.dropna(axis=1, how='all')
    Working.to_csv('Census_Data_merged.csv', encoding='utf-8')
