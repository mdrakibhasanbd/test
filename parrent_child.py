lst =[{
    "parent": "com.company.object.kind.type.subtype.family.Feline",
    "class": "com.company.object.kind.type.subtype.family.species.Cat"
}, {
    "parent": "com.company.object.kind.type.subtype.Mammal",
    "class": "com.company.object.kind.type.subtype.family.Feline"
}, {
    "parent": "com.company.object.Being",
    "class": "com.company.object.kind.LivingBeing"
}, {
    "parent": "com.company.object.kind.type.subtype.family.Canine",
    "class": "com.company.object.kind.type.subtype.family.species.Wolf"
}, {
    "parent": "com.company.object.kind.type.subtype.Mammal",
    "class": "com.company.object.kind.type.subtype.family.Canine"
}, {
    "parent": "com.company.object.kind.type.Animal",
    "class": "com.company.object.kind.type.subtype.Mammal"
}, {
    "parent": "com.company.object.kind.LivingBeing",
    "class": "com.company.object.kind.type.Animal"
}, {
    "parent": "com.company.object.kind.type.Animal",
    "class": "com.company.object.kind.type.subtype.Fish"
}, {
    "parent": "com.company.object.kind.StaticBeing",
    "class": "com.company.object.kind.type.Solid"
}, {
    "parent": "com.company.object.Being",
    "class": "com.company.object.kind.StaticBeing"
}, {
    "parent": "com.company.object.kind.type.subtype.family.Feline",
    "class": "com.company.object.kind.type.subtype.family.species.Lion"
}, {
    "parent": "com.company.object.kind.type.subtype.family.Canine",
    "class": "com.company.object.kind.type.subtype.family.species.Hyena"
}, {
    "parent": "com.company.object.kind.StaticBeing",
    "class": "com.company.object.kind.type.Liquid"
}]


def build_tree(elems):
  elem_with_children = {}

  def _build_children_sub_tree(parent):
      cur_dict = {
          'id': parent,
          # put whatever attributes here
      }  
      if parent in elem_with_children.keys():
          cur_dict["children"] = [_build_children_sub_tree(cid) for cid in elem_with_children[parent]]
      return cur_dict

  for item in elems:
      cid = item['id']
      pid = item['parent']
      elem_with_children.setdefault(pid, []).append(cid)

  res = _build_children_sub_tree("com.company.object.Being")
  return res