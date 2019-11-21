import json

def draw_graph(apps):
    list_nodes = []
    list_edges = []

    index = 0
    for id in apps:
        list_nodes.append({
            "id": id,
            "label": id,
            "size": 3,
            "x": apps[id]['x'],
            "y": apps[id]['y'],
        })

        for d in apps[id]['to']:
            list_edges.append({
                "id": str(index),
                "source": id,
                "target": d,
                'type': "arrow",
                'size': 1,
                'color': "#94aa2a",
            })
            index += 1

    result = {
        "nodes": list_nodes,
        "edges": list_edges
    }

    with open('visual_graph/data.json', 'w') as outfile:
        json.dump(result, outfile)