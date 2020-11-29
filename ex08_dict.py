#%%
conn_info = dict(host='localhost',port=3306, db='northwind',perm=True)
conn_info
# %%
conn_info['host']
# %%
e = ['localhost',3306, 'northwind',True]
e
# %%
user = {
    'lastName':'Smith',
    'firstName':'Anna',
    'age':30,
    'mail':'anna@no.com'
}

user['firstName']
# %%
user.keys()
# %%
user.values()
# %%
user.items()
# %%
user['phone']
# %%
'phone' in user
# %%
user.get('phone','111-11-11')
# %%
