import pandas as pd

PATH = "/Users/junyuwu/Cosmetics /components/cosmetics.csv"
df = pd.read_csv(PATH)

def get_data():
    return df

def get_brand_list():
    bybrand = df["Brand"].value_counts()[:10]
    bylist = sorted(list(set(bybrand.index.tolist())))
    return bylist

def get_brand():
    bybrand = df["Brand"].value_counts()[:10].to_frame()
    bybrand.reset_index(inplace= True)
    bybrand.rename(columns={"index":"Brand_Name","Brand":"Amount"},inplace=True)
    return bybrand

def get_price_list():
    byprice = df.groupby("Brand")[["Price"]].mean().sort_values("Price", ascending=False)[:10].round()
    bylist = sorted(list(set(byprice.index.tolist())))
    return bylist

def get_price():
    byprice = df.groupby("Brand")[["Price"]].mean().sort_values("Price", ascending=False)[:10].round()
    byprice.reset_index(inplace= True)
    byprice.rename(columns={"Brand":"Brand_Name","Price":"Average_Price"},inplace=True)
    return byprice

def get_label():
    bylab = df.groupby("Label")[["Price"]].mean()
    bylab = bylab.reset_index()
    return bylab

def get_com():
    bycom = df.groupby("Combination")[["Price"]].mean()
    bycom = bycom.reset_index()
    return bycom

def get_dry():
    bydry = df.groupby("Dry")[["Price"]].mean()
    bydry = bydry.reset_index()
    return bydry

def get_normal():
    bynor = df.groupby("Normal")[["Price"]].mean()
    bynor = bynor.reset_index()
    return bynor
	
def get_Oily():
    byOily = df.groupby("Oily")[["Price"]].mean()
    byOily = byOily.reset_index()
    return byOily

def get_Sensitive():
    bySensitive = df.groupby("Sensitive")[["Price"]].mean()
    bySensitive = bySensitive.reset_index()
    return bySensitive

def get_treat_list():
    expensive = df[df["Label"]=="Treatment"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    bylist = sorted(list(set(byexpensive.index.tolist())))
    return bylist

def get_treat():
    expensive = df[df["Label"]=="Treatment"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    byexpensive = byexpensive.reset_index()
    return byexpensive

def get_Moisturizer_list():
    expensive = df[df["Label"]=="Moisturizer"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    bylist = sorted(list(set(byexpensive.index.tolist())))
    return bylist

def get_Moisturizer():
    expensive = df[df["Label"]=="Moisturizer"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    byexpensive = byexpensive.reset_index()
    return byexpensive

def get_Eyecream_list():
    expensive = df[df["Label"]=="Eye cream"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    bylist = sorted(list(set(byexpensive.index.tolist())))
    return bylist

def get_Eyecream():
    expensive = df[df["Label"]=="Eye cream"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    byexpensive = byexpensive.reset_index()
    return byexpensive

def get_Sunprotect_list():
    expensive = df[df["Label"]=="Sun protect"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    bylist = sorted(list(set(byexpensive.index.tolist())))
    return bylist

def get_Sunprotect():
    expensive = df[df["Label"]=="Sun protect"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    byexpensive = byexpensive.reset_index()
    return byexpensive

def get_FaceMask_list():
    expensive = df[df["Label"]=="Face Mask"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    bylist = sorted(list(set(byexpensive.index.tolist())))
    return bylist

def get_FaceMask():
    expensive = df[df["Label"]=="Face Mask"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    byexpensive = byexpensive.reset_index()
    return byexpensive

def get_Cleanser_list():
    expensive = df[df["Label"]=="Cleanser"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    bylist = sorted(list(set(byexpensive.index.tolist())))
    return bylist

def get_Cleanser():
    expensive = df[df["Label"]=="Cleanser"]
    byexpensive = expensive.groupby("Brand")[["Price"]].mean().sort_values("Price",ascending=False)[:10].round()
    byexpensive = byexpensive.reset_index()
    return byexpensive