def max_circle(queries):
  answers = []
  next_group_id = 0
  id_to_group_map = {}
  group_to_ids_map = {}
  current_max_size = 1

  for query in queries:
    a, b = query[0], query[1]
    grp_a, grp_b = id_to_group_map.get(a), id_to_group_map.get(b)
    if (grp_a and grp_b) and grp_a == grp_b:
      continue

    members_grp_a = group_to_ids_map.get(grp_a) if group_to_ids_map.get(grp_a) else {a}
    members_grp_b = group_to_ids_map.get(grp_b) if group_to_ids_map.get(grp_b) else {b}
    members_new_grp = members_grp_a.union(members_grp_b)

    current_max_size = max(len(members_new_grp), current_max_size)
    answers.append(current_max_size)

    for el in members_new_grp:
      id_to_group_map[el] = next_group_id
    
    group_to_ids_map[next_group_id] = members_new_grp

    next_group_id = next_group_id + 1

  return answers


# max_circle([[1, 2], [3, 4], [1, 3], [5, 7], [5, 6], [7, 4]])
