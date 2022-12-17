from pprint import pprint
lst = [
    {"id": 0, "job": "CEO", "ManagerID": 0, "name": "John Smith"},
    {"id": 1, "job": "Medical Manager", "ManagerID": 0, "name": "Medic 1"},
    {"id": 2, "job": "Medical Assist", "ManagerID": 1, "name": "Medic 2"},
    {"id": 3, "job": "ICT Manager", "ManagerID": 0, "name": "ICT 1"},
    {"id": 4, "job": "ICT Assist", "ManagerID": 3, "name": "ICT 2"},
    {"id": 5, "job": "ICT Junior", "ManagerID": 4, "name": "ICT 3"}
]
employees = {}
managers = set()
root_id = None
for emp in lst:
    id, mid = emp['id'], emp['ManagerID']
    # create a copy of emp, and add a "children" list
    employees[id] = {**emp, 'children': []}
    managers.add(mid)
    if id == mid:
        # the root of the tree references itself as the manager
        root_id = id

# add empty manager entries for missing manager IDs, reporting to root ID.
for id in managers - employees.keys():
    employees[id] = {
        'id': id, 'ManagerID': root_id, 'children': [],
        'job': None, 'name': None
    }

for id, emp in employees.items():
    manager = employees[emp.pop('ManagerID')]
    if id != root_id:  # don't add the root to anything
        manager['children'].append(emp)

output = employees[root_id]
pprint(output)