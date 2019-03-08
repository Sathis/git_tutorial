import json
from collections import defaultdict

def loadJson():
    ''' Method to load input for creating Stops'''

data = '''{
            "load_id": 123, 
            "load_type": "ocpt",
            "origin": 6001,
            "origin_type": "DC",
            "dest": 100,
            "dest_type": "STORE",
            "orders":[
                {
                    
                    "po_number": "9999999",
                    "origin": "6001",
                    "origin_type": "DC",
                    "dest": 100,
                    "dest_type":"STORE",
                    "pallets": "2"
                },
                {
                    "po_number": "888888",
                    "origin": "6001",
                    "origin_type": "DC",
                    "dest": 101,
                    "dest_type":"STORE",
                    "pallets": "1"
                },
                {
                    "po_number": "77777",
                    "origin": "6005",
                    "origin_type": "DC",
                    "dest": 100,
                    "dest_type":"STORE",
                    "pallets": "3"
                },
                {
                    
                    "po_number": "9999999",
                    "origin": "6005",
                    "origin_type": "DC",
                    "dest": 101,
                    "dest_type":"STORE",
                    "pallets": "2"
                },
                {
                    "po_number": "77777",
                    "origin": "6005",
                    "origin_type": "DC",
                    "dest": 100,
                    "dest_type":"STORE",
                    "pallets": "3"
                }
            ]
        }'''
        
dict = json.loads(data)

dest_dict = defaultdict(list)

#map(lambda order: dest_dict[order['dest']].append(order['origin']),dict['orders'])

for idx,order in enumerate(dict['orders']):
    order['seq'] = idx
    dest_dict[order['dest']].append(order)

req_order =[]


for  k, orders in dest_dict.items():
    temp = []
    dup_origin = []
    for order in orders:
        same_origin = []
       # print(k)
        #print(order['origin'])
        if not list(filter(lambda _order: _order['seq'] == order['seq'], req_order)):
            same_origin.append(order)
            if order['origin'] not in dup_origin:   
                same_origin.extend(list(filter (lambda _order:(_order['origin'] == order['origin'] and 
                _order['seq'] != order['seq'] and _order['dest'] != order['dest']), dict['orders'])))
            if (len(same_origin) == 1):
                req_order.extend(same_origin)
            else:
                temp.extend(same_origin)
            #print(same_origin)
        dup_origin.append(order['origin'])
    req_order.extend(temp)
print(req_order)



     



if __name__ == "__main__":
    loadJson()

class Load:
    pass

    
