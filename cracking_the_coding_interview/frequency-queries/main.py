from collections import defaultdict


def getDictDefaultValue():
    return 0


def frequency_queries(queries):
    result = []

    v_occ = defaultdict(getDictDefaultValue)
    occ_c = defaultdict(getDictDefaultValue)

    for [command, value] in queries:
        if command == 1:  # insert
            occ_c[v_occ[value]] = max(0, occ_c[v_occ[value]] - 1)
            v_occ[value] = v_occ[value] + 1
            occ_c[v_occ[value]] = occ_c[v_occ[value]] + 1
        elif command == 2:
            occ_c[v_occ[value]] = max(0, occ_c[v_occ[value]] - 1)
            v_occ[value] = max(0, v_occ[value] - 1)
            occ_c[v_occ[value]] = occ_c[v_occ[value]] + 1
        else:
            if value in occ_c and occ_c[value] > 0:
                result.append(1)
            else:
                result.append(0)

    return result
