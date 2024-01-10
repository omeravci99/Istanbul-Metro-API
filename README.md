﻿# Istanbul-Metro-API

Bu Python kodu, İstanbul metrosundaki istasyonları ve hatları görselleştirmek için kullanılır. Ayrıca, sadece metro hatlarını kullanarak belirli iki istasyon arasındaki en kısa yolun bulunmasını sağlar.
Not: Bazı tramvay hatları ve yeni yapılan İstanbul Havalimanı Metrosu bu projede bulunmamaktadır.
## Gereksinimler

- `requests`: İnternet üzerinden veri çekmek için kullanılır.
- `networkx`: Graf oluşturmak ve en kısa yol bulmak için kullanılır.
- `matplotlib`: Grafikleri çizmek için kullanılır.

Gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install requests
pip install networkx
pip install matplotlib

## Örnek Kullanım
shortest_path = nx.shortest_path(G, source=212, target=301, weight='weight')
print("En kısa yol:", shortest_path)

