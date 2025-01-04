# Noktaları tanımlama
points = [(1, 2), (4, 6), (7, 8), (2, 3)]  # Örnek bir noktalar listesi

# Öklid mesafesi için fonksiyon tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Mesafeleri hesaplama
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
minimum_distance = min(distances)

# Sonucu yazdırma
print("Noktalar arasındaki minimum Öklid mesafesi:", minimum_distance)
