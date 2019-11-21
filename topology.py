
ID = 'App Name'
DEPEND = 'Dependencies'
INCHARGE = 'In Charge'


def preprocess_data(data):
    apps = {}

    for record in data:
        id = record[ID].strip()
        if not id:
            continue
        if id not in apps:
            apps[id] = {'to': [], 'inDegree': 0, 'outDegree': 0, 'inCharge': record[INCHARGE]}
        if not apps[id]['inCharge']:
            apps[id]['inCharge'] = record[INCHARGE]

        if record[DEPEND].strip():
            depends = record[DEPEND].split(',')

            for depend in depends:
                d = depend.strip()
                if d in apps:
                    apps[id]['inDegree'] += 1
                    apps[d]['outDegree'] += 1
                    apps[d]['to'].append(id)
                else:
                    apps[id]['inDegree'] += 1
                    apps[d] = {'to': [id], 'inDegree': 0, 'outDegree': 1, 'inCharge': ''}
    return apps


def topological_sort(apps):
    queue = []
    top_order = []
    cnt = 0

    current_x = 50
    current_y = 100

    free_apps = []
    current_free_x = 0
    current_free_y = 0

    for id in apps:
        if apps[id]['inDegree'] == 0:
            if apps[id]['outDegree'] == 0:
                free_apps.append({'id':id, 'inCharge': apps[id]['inCharge']})
                apps[id]['x'] = current_free_x
                if apps[id]['x'] == 0:
                    current_free_y += 10
                apps[id]['y'] = current_free_y
                cnt += 1
            else:
                queue.append({'id':id, 'inCharge': apps[id]['inCharge']})
                if 'x' not in apps[id]:
                    apps[id]['x'] = current_x
                    apps[id]['y'] = current_y
                    current_y += 40
    queue.sort(key=lambda app: apps[app['id']]['outDegree'], reverse=True)

    while queue:
        delta_y = -25
        app = queue.pop(0)
        u = app['id']
        top_order.append({'id':u, 'inCharge': apps[u]['inCharge']})

        for id in apps[u]['to']:
            apps[id]['inDegree'] -= 1
            if apps[id]['inDegree'] == 0:
                queue.append({'id':id, 'inCharge': apps[id]['inCharge']})
                if 'x' not in apps[id]:
                    apps[id]['x'] = apps[u]['x'] + 80
                    apps[id]['y'] = apps[u]['y'] + delta_y
                    delta_y -= 15

        queue.sort(key=lambda app: apps[app['id']]['outDegree'], reverse=True)
        cnt += 1

    if cnt != len(apps):
        return ('Error', "There exists a cycle in the graph")
    else:
        return ('OK', top_order + free_apps)
