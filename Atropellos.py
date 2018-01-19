sheets = pd.read_excel('/home/dsc/Desktop/Master/01_ ACCIDENTES POR TIPO EN  DISTRITOS.xls',
                       skiprows=7, skipfooter=1, parse_cols='A:K', 
                       sheetname=None)
result = []
for name in sheets.keys()
    year = int(name)
    skiprows = 4 if year == 2013 else 7
    this_sheet = pd.read_excel('/home/dsc/Desktop/Master//01_ ACCIDENTES POR TIPO EN  DISTRITOS.xls',
                       skiprows=skiprows, skipfooter=1, parse_cols='A:K', 
                       sheetname=name)
    this_sheet['YEAR'] = year
    result.append(this_sheet)
whole_df = pd.concat(result)
whole_df.sample(3)

años=[]
atropellos = []
distrito = []
for i in whole_df['YEAR']:
    if i not in años:
        años.append(i)
for i in whole_df['DISTRITO_ACCIDENTE']:
    if i not in distrito:
        distrito.append(i)
for i in range(21):
    atropellos.append(whole_df['ATROPELLO                               '].loc[i])
    atropellados = np.array(atropellos)

for i in range(21):
    plt.plot(años,atropellados[i],label=distrito[i])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('Años')
plt.ylabel('Atropellos')
plt.show()
# Todos los atropellos por distrito en una misma gráfica, en el eje 'x' los años 2009-2016 
# y en el eje 'y' el número de atropellos


for i in range(21):
    plt.plot(años,atropellados[i],label=distrito[i])
    plt.legend()
    plt.xlabel('Años')
    plt.ylabel('Atropellos')
    plt.show()
# Gráfica de los atropellos para cada distrito. 
