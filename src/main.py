import requests
import networkx as nx
import matplotlib.pyplot as plt
# Requests
response = requests.get("https://api.ibb.gov.tr/MetroIstanbul/api/MetroMobile/V2/GetStations")
data_list = []
data = response.json()
stations = {"M5":[],"M4":[],"M8":[],"MM":[],"M2":[],"M7":[],"M3":[],"T1":[],"T5":[],"M1A":[],"M1B":[],"M6":[],"M9":[],"M11":[],"T4":[],"F1":[],"F4":[]}
#f1, tf1, tf2, f3, f4, 
# Initialize a list to hold dictionaries for each station

# Iterate through the data and filter stations for LineName 'M5'
for station_data in data["Data"]:
    for key in stations:
        if station_data["LineName"] == key:
            station = {
                "name": station_data["Name"],
                "latitude": station_data["DetailInfo"].get("Latitude",""),
                "longitude": station_data["DetailInfo"].get("Longitude", ""),
                "id": station_data["Id"],
                "order": station_data["Order"]
            }
            stations[key].append(station)

stations["MM"] = [{'name': 'GEBZE', 'latitude': '40.784181', 'longitude': '29.3935358', 'id': 301, 'order': 1}, {'name': 'DARICA', 'latitude': '40.78982', 'longitude': '29.3895205', 'id': 302, 'order': 2}, {'name': 'OSMANGAZI', 'latitude': '40.7986566', 'longitude': '29.3782534', 'id': 303, 'order': 3}, {'name': 'GEBZE_TEKNIK_ÜNIVERSITESI', 'latitude': '40.8082463', 'longitude': '29.3594667', 'id': 304, 'order': 4}, {'name': 'CAYIROVA', 'latitude': '40.8107955', 'longitude': '29.3465654', 'id': 305, 'order': 5}, {'name': 'TUZLA', 'latitude': '40.8290353', 'longitude': '29.3207176', 'id': 306, 'order': 6}, {'name': 'ICMELER', 'latitude': '40.8455518', 'longitude': '29.2998963', 'id': 307, 'order': 7}, {'name': 'AYDINTEPE', 'latitude': '40.8508856', 'longitude': '29.295064', 'id': 308, 'order': 8}, {'name': 'GUZELYALI', 'latitude': '40.8561729', 'longitude': '29.2860626', 'id': 309, 'order': 9}, {'name': 'TERSANE', 'latitude': '40.8598315', 'longitude': '29.2747476', 'id': 310, 'order': 10}, {'name': 'KAYNARCA', 'latitude': '40.8705039', 'longitude': '29.2558612', 'id': 311, 'order': 11}, {'name': 'PENDIK', 'latitude': '40.8806883', 'longitude': '29.2316707', 'id': 312, 'order': 12}, {'name': 'YUNUS', 'latitude': '40.8834551', 'longitude': '29.2091668', 'id': 313, 'order': 13}, {'name': 'KARTAL', 'latitude': '40.8870486', 'longitude': '29.1851243', 'id': 314, 'order': 14}, {'name': 'BASAK', 'latitude': '40.891103', 'longitude': '29.1752967', 'id': 315, 'order': 15}, {'name': 'ATALAR', 'latitude': '40.8981152', 'longitude': '29.1674154', 'id': 316, 'order': 16}, {'name': 'CEVIZLI', 'latitude': '40.9082929', 'longitude': '29.155834', 'id': 317, 'order': 17}, {'name': 'MALTEPE', 'latitude': '40.9198759', 'longitude': '29.1308588', 'id': 318, 'order': 18}, {'name': 'SUREYYA_PLAJI', 'latitude': '40.9261565', 'longitude': '29.1197238', 'id': 319, 'order': 19}, {'name': 'IDEALTEPE', 'latitude': '40.9383674', 'longitude': '29.1099494', 'id': 320, 'order': 20}, {'name': 'KUUCKYALI', 'latitude': '40.9439545', 'longitude': '29.1057246', 'id': 321, 'order': 21}, {'name': 'BOSTANCI', 'latitude': '40.95128998347687', 'longitude': '29.097243057130374', 'id': 161, 'order': 22}, {'name': 'SUADIYE', 'latitude': '40.9587123', 'longitude': '29.0850411', 'id': 323, 'order': 23}, {'name': 'ERENKOY', 'latitude': '40.9703631', 'longitude': '29.0736159', 'id': 324, 'order': 24}, {'name': 'GOZTEPE', 'latitude': '40.9782839', 'longitude': '29.0594758', 'id': 325, 'order': 25}, {'name': 'FENERYOLU', 'latitude': '40.9767792', 'longitude': '29.0465906', 'id': 326, 'order': 26}, {'name': 'SOGUTLUCESME', 'latitude': '40.9925862', 'longitude': '29.0333966', 'id': 327, 'order': 27}, {'name': 'AYRILIK_CESMESI', 'latitude': '41.00020434433358', 'longitude': '29.030153258203203', 'id': 2, 'order': 28}, {'name': 'USKUDAR', 'latitude': '41.025618259645256', 'longitude': '29.015061927581854', 'id': 122, 'order': 29}, {'name': 'SIRKECI', 'latitude': '41.015180', 'longitude': '28.975890', 'id': 330, 'order': 30}, {'name': 'YENIKAPI', 'latitude': '41.0055971704', 'longitude': '28.9513306172', 'id': 20, 'order': 31}, {'name': 'KAZLICESME', 'latitude': '40.9920031', 'longitude': '28.9166025', 'id': 332, 'order': 32}, {'name': 'ZEYTINBURNU', 'latitude': '40.9866357', 'longitude': '28.9045622', 'id': 333, 'order': 33}, {'name': 'YENIMAHALLE', 'latitude': '40.9817211', 'longitude': '28.8824225', 'id': 334, 'order': 34}, {'name': 'BAKIRKOY', 'latitude': '40.9815344', 'longitude': '28.8734009', 'id': 335, 'order': 35}, {'name': 'ATAKOY', 'latitude': '40.9794168', 'longitude': '28.8555328', 'id': 336, 'order': 36}, {'name': 'YESILYURT', 'latitude': '40.9630548', 'longitude': '28.830968', 'id': 337, 'order': 37}, {'name': 'YESILKOY', 'latitude': '40.9627362', 'longitude': '28.8247946', 'id': 338, 'order': 38}, {'name': 'FLORYA_AKVARUM', 'latitude': '40.96556', 'longitude': '28.7983628', 'id': 339, 'order': 39}, {'name': 'FLORYA', 'latitude': '40.9715111', 'longitude': '28.790156', 'id': 340, 'order': 40}, {'name': 'KUCUKCEKMECE', 'latitude': '40.98784', 'longitude': '28.773917', 'id': 341, 'order': 41}, {'name': 'MUSTAFA_KEMAL', 'latitude': '41.0028258', 'longitude': '28.7656428', 'id': 342, 'order': 42}, {'name': 'HALKALI', 'latitude': '41.0167685', 'longitude': '28.7682746', 'id': 343, 'order': 43}]
stations["M8"][10]["latitude"] = "41.01544045560607"
stations["M8"][10]["longitude"] = "29.16244635386456"
stations["M8"][10]["id"] = 135
stations["M8"][3]["latitude"] = "40.9748528607554"
stations["M8"][3]["longitude"] = "29.099330474424526"
stations["M8"][3]["id"] = 7
stations["M7"][2]["latitude"] = "41.0645069127"
stations["M7"][2]["longitude"] = "28.9926697578"
stations["M7"][2]["id"] = 26
stations["M7"][8]["latitude"] = "41.0799901"
stations["M7"][8]["longitude"] = "28.9352699"
stations["M7"][9]["latitude"] = "41.0796898"
stations["M7"][9]["longitude"] = "28.9295594"
stations["M3"][6]["latitude"] = "41.054312"
stations["M3"][6]["longitude"] = "28.830612"
stations["M3"][6]["id"] = 160
stations["M3"][9]["latitude"] = "41.1133997"
stations["M3"][9]["longitude"] = "28.7905842"
stations["M3"][10]["latitude"] = "41.1031843"
stations["M3"][10]["longitude"] = "28.7762591"
stations["M3"][11]["latitude"] = "41.1068062"
stations["M3"][11]["longitude"] = "28.767267"
stations["M3"][12]["latitude"] = "41.1183031"
stations["M3"][12]["longitude"] = "28.7655255"
stations["M3"] = [{'name': 'KAYASEHIR MERKEZ', 'latitude': '41.1183031', 'longitude': '28.7655255', 'id': 240, 'order': 13},{'name': 'TOPLU KONUTLAR', 'latitude': '41.1068062', 'longitude': '28.767267', 'id': 239, 'order': 12}, {'name': 'SEHIR HASTANESI', 'latitude': '41.1031843', 'longitude': '28.7762591', 'id': 238, 'order': 11},{'name': 'ONURKENT', 'latitude': '41.1133997', 'longitude': '28.7905842', 'id': 237, 'order': 10},{'name': 'METROKENT', 'latitude': '41.1075899254', 'longitude': '28.8014768347', 'id': 36, 'order': 9}, {'name': 'BASAK KONUTLARI', 'latitude': '41.0976705948', 'longitude': '28.7912824671', 'id': 37, 'order': 8}, {'name': 'SITELER', 'latitude': '41.0882027223', 'longitude': '28.7965104065', 'id': 38, 'order': 7}, {'name': 'TURGUT OZAL', 'latitude': '41.0811852568', 'longitude': '28.7974049311', 'id': 39, 'order': 6}, {'name': 'IKITELLI SANAYI', 'latitude': '41.0724333906', 'longitude': '28.8023285305', 'id': 40, 'order': 5}, {'name': 'ISTOC', 'latitude': '41.0649996532', 'longitude': '28.8259591715', 'id': 41, 'order': 4}, {'name': 'MAHMUTBEY', 'latitude': '41.054312', 'longitude': '28.830612', 'id': 160, 'order': 3}, {'name': 'YENIMAHALLE', 'latitude': '41.0403571945', 'longitude': '28.8359378583', 'id': 43, 'order': 2}, {'name': 'KIRAZLI', 'latitude': '41.0322960516', 'longitude': '28.8427689525', 'id': 44, 'order': 1}]
stations['T1'][25]["latitude"] = '41.015180'
stations['T1'][25]["longitude"] = "28.975890"
stations['T1'][25]["id"] = 330
stations["T5"][0]["latitude"] = "41.0174770208"
stations["T5"][0]["longitude"] = "28.9732097738"
stations["T5"][0]["id"] = 78
stations["T5"][12]["latitude"] = "41.0791702"
stations["T5"][12]["longitude"] = "28.9493602"
stations["T5"][12]["id"] = 150
stations["M1B"] = [{'name': 'KIRAZLI', 'latitude': '41.0322960516', 'longitude': '28.8427689525', 'id': 44, 'order': 1}, {'name': 'BAGCILAR MEYDAN', 'latitude': '41.0345164689', 'longitude': '28.8561714937', 'id': 48, 'order': 2}, {'name': 'UCYUZLU', 'latitude': '41.036721597', 'longitude': '28.8706340581', 'id': 49, 'order': 3}, {'name': 'MENDERES', 'latitude': '41.0427591002', 'longitude': '28.8784878297', 'id': 50, 'order': 4}, {'name': 'ESENLER', 'latitude': '41.037682433', 'longitude': '28.8884222852', 'id': 51, 'order': 5},{'name': 'OTOGAR', 'latitude': '41.0401441651', 'longitude': '28.8945600984', 'id': 211, 'order': 11}, {'name': 'KOCATEPE', 'latitude': '41.0484928183', 'longitude': '28.8953862076', 'id': 204, 'order': 12}, {'name': 'SAGMALCILAR', 'latitude': '41.0408544497', 'longitude': '28.9072352877', 'id': 205, 'order': 13}, {'name': 'BAYRAMPASA', 'latitude': '41.0340978572', 'longitude': '28.920238689', 'id': 206, 'order': 14}, {'name': 'ULUBATLI', 'latitude': '41.0240250582', 'longitude': '28.9305034257', 'id': 207, 'order': 15}, {'name': 'EMNIYET', 'latitude': '41.0176115439', 'longitude': '28.9395963977', 'id': 208, 'order': 16}, {'name': 'AKSARAY', 'latitude': '41.0120281897', 'longitude': '28.9480625565', 'id': 209, 'order': 17}, {'name': 'YENIKAPI', 'latitude': '41.0055971704', 'longitude': '28.9513306172', 'id': 20, 'order': 18}]
stations["M1A"] = [{'name': 'ATATURK HAVALIMANI', 'latitude': '40.9795429431', 'longitude': '28.8211244027', 'id': 105, 'order': 1}, {'name': 'DTM - ISTANBUL FUAR MERKEZI', 'latitude': '40.9866455145', 'longitude': '28.8285503243', 'id': 106, 'order': 2}, {'name': 'YENIBOSNA', 'latitude': '40.9893149835', 'longitude': '28.8367043004', 'id': 107, 'order': 3}, {'name': 'ATAKOY', 'latitude': '40.9913500997', 'longitude': '28.846082309', 'id': 108, 'order': 4}, {'name': 'BAHCELIEVLER', 'latitude': '40.9953532384', 'longitude': '28.8630661969', 'id': 109, 'order': 5}, {'name': 'BAKIRKOY - INCIRLI', 'latitude': '40.9966121333', 'longitude': '28.8753997556', 'id': 110, 'order': 6}, {'name': 'ZEYTINBURNU', 'latitude': '41.0014853458', 'longitude': '28.8902920022', 'id': 60, 'order': 7}, {'name': 'MERTER', 'latitude': '41.0076458753', 'longitude': '28.8961771147', 'id': 112, 'order': 8}, {'name': 'DAVUTPASA', 'latitude': '41.0206387059', 'longitude': '28.9001417888', 'id': 113, 'order': 9}, {'name': 'TERAZIDERE', 'latitude': '41.0303317032', 'longitude': '28.8979522419', 'id': 114, 'order': 10}, {'name': 'KOCATEPE', 'latitude': '41.0408544497', 'longitude': '28.9072352877', 'id': 205, 'order': 12}]
stations["M6"][0]["latitude"] = "41.0767734293"
stations["M6"][0]["longitude"] = "29.0136876237"
stations["M6"][0]["id"] = 28
stations["M9"][2]["latitude"] = "41.0724333906"
stations["M9"][2]["longitude"] = "28.8023285305"
stations["M9"][2]["id"] = 40
stations["T4"][7]["latitude"] = "41.0815994"
stations["T4"][7]["longitude"] = "28.8754204"
stations["T4"][7]["id"] = 156
stations["T4"][19]["latitude"] = '41.0240250582'
stations["T4"][19]["longitude"] = '28.9305034257'
stations["T4"][19]["id"] = 207
stations["T4"][21]["latitude"] = '41.0192295429'
stations["T4"][21]["longitude"] = '28.9194470285'
stations["T4"][21]["id"] = 65
stations["F1"][0]["latitude"] = '41.034195'
stations["F1"][0]["longitude"] = '28.992712'
stations["F1"][0]["id"] = 82
stations["F1"][1]["latitude"] = '41.038496'
stations["F1"][1]["longitude"] = '28.985783'
stations["F1"][1]["id"] = 24
stations["F4"][1]["latitude"] = '41.085278'
stations["F4"][1]["longitude"] = '29.045519'
stations["F4"][1]["id"] = 141
print(stations["F3"])

line_colors = {
    "M5": "red", "M4": "blue", "M8": "green", "MM": "purple", "M2": "orange", "M7": "cyan",
    "M3": "brown", "T1": "pink", "T5": "yellow", "M1A": "gray", "M1B": "magenta",
    "M6": "lime", "M9": "teal", "M11": "indigo", "T4": "maroon", "F1": "navy", "F4": "olive"
}
####graph jobs
G = nx.Graph()
def addNode(graph,list):
    for node_data in list:
        node_id = node_data['id']
        posx = float(node_data["longitude"]) # float tipine dönüştür
        posy = float(node_data["latitude"])
        order = node_data["order"]
        graph.add_node(node_id, pos=(posx, posy),order=order)  # pos adında bir özellik ekleyerek konum bilgisini düğüme ekle
def addEdge(graph,list,weight):
    for i in range(len(list)-1):
        graph.add_edge(list[i]["id"],list[i+1]["id"],weight=weight)

for x in stations.keys():
    addNode(G,stations[x])
    addEdge(G,stations[x],2)

node_positions = {node: data['pos'] for node, data in G.nodes(data=True)}
# Visualize the graph with specified positions
nx.draw(G, pos=node_positions, with_labels=True, node_size=5,
        node_color='skyblue', font_color='black', font_size=0, edge_color='red', width=0.5, alpha=0.7,
        node_shape="o")
# Display the graph
plt.show()

shortest_path = nx.shortest_path(G, source=212, target=301, weight='weight')

print("En kısa yol:", shortest_path)



