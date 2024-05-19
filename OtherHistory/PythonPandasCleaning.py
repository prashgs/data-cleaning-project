# %%
import pandas as pd
from pandas_profiling import ProfileReport


# %%
'''Read cleaned and original datasets'''

# df_dish = pd.read_csv(r'./Original/Dish.csv')
df_dish_cleaned = pd.read_csv(r'./data/cleaned/OpenRefine/Dish_cleaned.csv')
df_menu_cleaned = pd.read_csv(r'./data/cleaned/OpenRefine/Menu_cleaned.csv')
# df_menu = pd.read_csv(r'./Original/Menu.csv')
# df_menu_item = pd.read_csv(r'./Original/MenuItem.csv')
# df_menu_page = pd.read_csv(r'./Original/MenuPage.csv')


# %%
'''Functiona to remove columns with all blank rows'''
def remove_empty_columns(df):
    df_new = df.dropna(axis='columns', how='all')
    columns_removed = set(df.columns.to_list()) - set(df_new.columns.to_list())
    return columns_removed, df_new



# %%
'''Remove columns that have are empty'''
menu_columns_removed, df_menu_cleaned = remove_empty_columns(df_menu_cleaned)
print(f'Menu dataset - Empty columns removed - {menu_columns_removed}')

# %%
'''Keep Columns that are relevent to use case'''
df_menu_cleaned = df_menu_cleaned[['id','name','event','venue','occasion','date','location','currency','status']]


# %%
'''Change Menu Date to yyyy-mm-dd format'''
df_menu_cleaned['date'] = pd.to_datetime(df_menu_cleaned['date'], format=r'%Y-%m-%d', errors='coerce').dt.date
df_menu_cleaned['date']


# %%
'''Fill blank currency with Dollars'''
print(f'Menu dataset - Number of blank currency values filled with "Dollars" - {sum(df_menu_cleaned.currency.isna())}')
df_menu_cleaned['currency'] = df_menu_cleaned['currency'].fillna('Dollars')


# %%
'''Number of Menu's that are under review'''
under_review_rows = df_menu_cleaned[df_menu_cleaned.status== 'under review'].shape[0]
print(f'Menu dataset - Number of rows with "Under Review" status removed - {under_review_rows}')

# %%
'''Drop rows that are "Under Review"'''
# print(f'Menu dataset - Shape of Menu before removal - {df_menu_cleaned.shape}')
df_menu_cleaned = df_menu_cleaned.drop(df_menu_cleaned[df_menu_cleaned.status=='under review'].index)
print(f'Menu dataset - Final columns - {df_menu_cleaned.columns.tolist()}')
df_menu_cleaned.to_csv('./data/cleaned/PyPandas/menu_cleaned.csv', index=False)


#%%
'''Remove blank columns from Dish'''
dish_columns_removed, df_dish_cleaned = remove_empty_columns(df_dish_cleaned)
print(f'Dish Dataset - Empty columns removed - {dish_columns_removed}')
df_dish_cleaned = df_dish_cleaned[['id','name','first_appeared','last_appeared','lowest_price','highest_price']]
print(f'Dish Dataset - Final columns - {df_dish_cleaned.columns.tolist()}')
df_dish_cleaned.to_csv('./data/cleaned/PyPandas/dish_cleaned.csv', index=False)

# # %%
# profile = ProfileReport(df_menu_cleaned, title="Pandas Profiling Report",explorative=True)
# profile.to_file("menu_cleaned.html")

# profile = ProfileReport(df_menu, title="Pandas Profiling Report",explorative=True)
# profile.to_file("menu_original.html")

# # %%
# profile = ProfileReport(df_dish_cleaned, title="Pandas Profiling Report",explorative=True)
# # profile.to_notebook_iframe()
# profile.to_file("dish_cleaned.html")

# profile = ProfileReport(df_dish, title="Pandas Profiling Report",explorative=True)
# # profile.to_notebook_iframe()
# profile.to_file("dish_original.html")
# # %%