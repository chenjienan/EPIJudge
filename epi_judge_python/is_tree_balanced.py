from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    
    def get_height(node):
        if not node: return 0

        # divide
        left = get_height(node.left)
        right = get_height(node.right)
        
        # conquer
        if left == -1 or right == -1: return -1
        if abs(left - right) > 1: return -1

        return max(left, right) + 1

    height = get_height(tree)
    return height != -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
