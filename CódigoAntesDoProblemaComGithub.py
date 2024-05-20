# Calculando as porcentagens de 'repeat_retailer' para cada cluster
repeat_retailer_percentages = []
for cluster in clusters:
    total_obs = len(dataClustered[dataClustered['clus'] == cluster])
    repeat_retailer_1 = len(dataClustered[(dataClustered['clus'] == cluster) & (dataClustered['repeat_retailer'] == 1)])
    repeat_retailer_percentages.append(repeat_retailer_1 / total_obs * 100)

# Calculando as porcentagens de 'repeat_retailer = 0' para cada cluster
repeat_retailer_0_percentages = [100 - perc for perc in repeat_retailer_percentages]

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(clusters, repeat_retailer_percentages, color='skyblue', label='repeat_retailer = 1')
plt.bar(clusters, repeat_retailer_0_percentages, bottom=repeat_retailer_percentages, color='lightgreen', label='repeat_retailer = 0')
plt.title('Porcentagem de observações com repeat_retailer por cluster')
plt.xlabel('Cluster')
plt.ylabel('Porcentagem')
plt.xticks(clusters)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Calculando as porcentagens de 'used_chip' para cada cluster
used_chip_percentages = []
for cluster in clusters:
    total_obs = len(dataClustered[dataClustered['clus'] == cluster])
    used_chip_1 = len(dataClustered[(dataClustered['clus'] == cluster) & (dataClustered['used_chip'] == 1)])
    used_chip_percentages.append(used_chip_1 / total_obs * 100)

# Calculando as porcentagens de 'used_chip = 0' para cada cluster
used_chip_0_percentages = [100 - perc for perc in used_chip_percentages]

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(clusters, used_chip_percentages, color='skyblue', label='used_chip = 1')
plt.bar(clusters, used_chip_0_percentages, bottom=used_chip_percentages, color='lightgreen', label='used_chipr = 0')
plt.title('Porcentagem de observações com used_chip por cluster')
plt.xlabel('Cluster')
plt.ylabel('Porcentagem')
plt.xticks(clusters)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# Calculando as porcentagens de 'used_pin_number' para cada cluster
used_pin_number_percentages = []
for cluster in clusters:
    total_obs = len(dataClustered[dataClustered['clus'] == cluster])
    used_pin_number_1 = len(dataClustered[(dataClustered['clus'] == cluster) & (dataClustered['used_pin_number'] == 1)])
    used_pin_number_percentages.append(used_pin_number_1 / total_obs * 100)

# Calculando as porcentagens de 'used_pin_number = 0' para cada cluster
used_pin_number_0_percentages = [100 - perc for perc in used_pin_number_percentages]

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(clusters, used_pin_number_percentages, color='skyblue', label='used_pin_number = 1')
plt.bar(clusters, used_pin_number_0_percentages, bottom=used_pin_number_percentages, color='lightgreen', label='used_pin_numberr = 0')
plt.title('Porcentagem de observações com used_pin_number por cluster')
plt.xlabel('Cluster')
plt.ylabel('Porcentagem')
plt.xticks(clusters)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# Calculando as porcentagens de 'used_pin_number' para cada cluster
used_pin_number_percentages = []
for cluster in clusters:
    total_obs = len(dataClustered[dataClustered['clus'] == cluster])
    used_pin_number_1 = len(dataClustered[(dataClustered['clus'] == cluster) & (dataClustered['used_pin_number'] == 1)])
    used_pin_number_percentages.append(used_pin_number_1 / total_obs * 100)

# Calculando as porcentagens de 'used_pin_number = 0' para cada cluster
used_pin_number_0_percentages = [100 - perc for perc in used_pin_number_percentages]

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(clusters, used_pin_number_percentages, color='skyblue', label='used_pin_number = 1')
plt.bar(clusters, used_pin_number_0_percentages, bottom=used_pin_number_percentages, color='lightgreen', label='used_pin_numberr = 0')
plt.title('Porcentagem de observações com used_pin_number por cluster')
plt.xlabel('Cluster')
plt.ylabel('Porcentagem')
plt.xticks(clusters)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

