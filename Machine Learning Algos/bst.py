def is_correct(bst_list, index=0, min_value=float('-inf'), max_value=float('inf')):
    if len(bst_list) <= index or bst_list[index] is None:
        return True

    value = bst_list[index]

    if value <= min_val or value >= max_val:
        return False
    
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    left_is_bst = is_correct(bst_list, left_index, min_value, value)
    right_is_bst = is_correct(bst_list, right_index, value, max_value)

    return left_is_bst and right_is_bst

def fix(bst_list):
    def is_leaf(index):
        left = 2 * index + 1
        right = 2 * index + 2
        return (left >= len(bst_list) or bst_list[left] is None) and (right >= len(bst_list) or bst_list[right] is None)

    n = len(bst_list)
    for i in range(n):
        if bst_list[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < n and bst_list[left_index] is not None and bst_list[left_index] > bst_list[i]:
                if is_leaf(left_index):
                    bst_list[left_index], bst_list[right_index] = bst_list[right_index], bst_list[left_index]
            if right_index < n and bst_list[right_index] is not None and bst_list[right_index] < bst_list[i]:
                if is_leaf(right_index):
                    bst_list[left_index], bst_list[right_index] = bst_list[right_index], bst_list[left_index]

    return bst_list


def get_keys(bst_list, index=0):
    key_values = []
     if index < len(bst_list) and bst_list[index] is not None:
        key_values.extend(get_keys(bst_list, 2 * index + 1))
        key_values.append(bst_list[index])
        key_values.extend(get_keys(bst_list, 2 * index + 2))
    return key_values

def give_values(bst_list, key_values, index=0):
    if index < len(bst_list) and bst_list[index] is not None:
    give_values(bst_list, key_values, 2 * index + 1)
    # Visit current node
    bst_list[index] = key_values.pop(0)
    # Traverse right subtree
    give_values(bst_list, key_values, 2 * index + 2)
    
def fix(bst_list):
    if not bst_list:
        return bst_list
    new_key_values = get_keys(bst_list)
    new_key_values.sort()
    give_values(bst_list, key_values)
    return bst_list
