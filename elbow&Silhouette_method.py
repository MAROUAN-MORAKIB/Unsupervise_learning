# elbow method 
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(data)
    distortions.append(kmeanModel.inertia_)
k =autoelbow.auto_elbow_search(data)
plt.figure(figsize=(10,5))
plt.plot(K, distortions, 'o-')
splt.xlabel('k values')
plt.ylabel('Distortion')
plt.title(f'The Elbow Method showing the optimal k = {k}')
plt.show()    
# Silhouette method 
k_max = 10
silhouette_avg = []
for num_clusters in range(2, k_max+1):
 
 # initialise kmeans
 kmeans = KMeans(n_clusters=num_clusters)
 kmeans.fit(data)
 cluster_labels = kmeans.labels_
 # silhouette score
 silhouette_avg.append(silhouette_score(data, cluster_labels))
 k_op = np.argmax(silhouette_avg) + 2
 
plt.plot(range(2,k_max+1),silhouette_avg,'bx-')
plt.xlabel('Values of K') 
plt.ylabel('Silhouette score') 
plt.title(f'Silhouette analysis For Optimal k = {k_op}')
plt.show()
