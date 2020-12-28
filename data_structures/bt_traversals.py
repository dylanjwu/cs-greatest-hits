# EASY

from binary_tree import TreeNode, Tree

def construct_bst(arr):
    def recurse(arr, l, h, root):
        if l > h:
            return 
        if l==h:
            root.val = arr[l]
            return
        mid = (l+h)//2
        root.val = arr[mid]
        root.left = TreeNode()
        root.right = TreeNode()
        recurse(arr, l, mid-1, root.left)
        recurse(arr, mid+1, h, root.right)

    root = Tree(TreeNode())
    recurse(arr, 0, len(arr)-1, root)
    return root


def traverse(root, traversal_type):
    if not root:
        return

    notNone = not root.val == None

    if traversal_type == 0 and notNone:
        print(root.val)

    traverse(root.left, traversal_type)

    if traversal_type == 1 and notNone:
        print(root.val)

    traverse(root.right, traversal_type)

    if traversal_type == 2 and notNone:
        print(root.val)


arr = [0,1,2,3,4,5,6]
arr1 = [0,1,2,3,4,5]
constructed_tree = construct_bst(arr1)

traversal_types = {
    'preorder': 0,
    'inorder': 1,
    'postorder': 2
}
traversal_type = traversal_types['inorder']
traverse(constructed_tree, traversal_type)