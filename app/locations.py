floor_room = {
    "105旁楼梯": [101, 201, 301, 401, 203, 303, 403, 501, 105, 206, 306, 406, 106, 207, 307, 407, 502],
    "107旁楼梯": [106, 207, 307, 407, 502, 503, 408, 308, 208, 107, 506, 411, 311, 211],
    "215值班室旁楼梯": [506, 411, 311, 211, 601, 507, 412, 312, 215, 509, 414, 314, 216],
    "216旁楼梯": [601, 507, 412, 312, 215, 509, 414, 314, 216, 602, 510, 415, 315, 217],
    "318旁楼梯": [603, 511, 416, 316, 605, 513, 418, 318, 701, 606, 514, 419],
    "320旁楼梯": [701, 606, 514, 419, 608, 516, 421, 320, 703, 609, 517, 422, 706, 612, 520, 425, 707, 613, 521, 426],
    "东-北楼大楼梯": [532, 529, 528, 437, 434, 433],
    "西-北楼大楼梯": [538, 442, 537, 443, 532, 437],
}

room_floor = {

}

for key, val in floor_room.items():
    for v in val:
        if v in room_floor:
            room_floor[v].append(key)
        else:
            room_floor[v] = [key, ]

dorm_b = {
    "1": {
        "name": "竹园1号楼",
        "location": [108.840477, 34.126696]
    },
    "2": {
        "name": "竹园2号楼",
        "location": [108.840477, 34.126696]
    },
    "3": {
        "name": "竹园3号楼",
        "location": [108.838792, 34.127424]
    },
    "4": {
        "name": "竹园4号楼",
        "location": [108.838792, 34.127424]
    },
    "5": {
        "name": "海棠5号楼",
        "location": [108.835348, 34.128974]
    },
    "6": {
        "name": "海棠6号楼",
        "location": [108.834501, 34.129329]
    },
    "7": {
        "name": "海棠7号楼",
        "location": [108.832757, 34.130035]
    },
    "8": {
        "name": "海棠8号楼",
        "location": [108.832757, 34.130035]
    },
    "9": {
        "name": "海棠9号楼",
        "location": [108.832087, 34.128969]
    },
    "10": {
        "name": "海棠10号楼",
        "location": [108.832087, 34.128969]
    },

    "11": {
        "name": "丁香11号楼",
        "location": [108.832087, 34.128969]
    },

    "12": {
        "name": "丁香12号楼",
        "location": [108.828321, 34.122952]
    },

    "13": {
        "name": "丁香13号楼",
        "location": [108.828321, 34.122952]
    },
    "14": {
        "name": "丁香14号楼",
        "location": [108.830225, 34.12214]
    },

    "15": {
        "name": "丁香15号楼",
        "location": [108.830225, 34.12214]
    },
}