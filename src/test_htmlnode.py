import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "This is a text node")
        self.assertEqual(repr(node), "HTMLNode(p, This is a text node, [], {})")

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a text node", props={"class": "text-class", "id": "text-id"})
        self.assertEqual(node.props_to_html(), 'class="text-class" id="text-id"')

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "This is a text node")
        self.assertEqual(node.props_to_html(), '')

    def test_children(self):
        child1 = HTMLNode("span", "Child 1")
        child2 = HTMLNode("span", "Child 2")
        parent = HTMLNode("div", "Parent", children=[child1, child2])
        self.assertEqual(parent.children, [child1, child2])

    def test_children_empty(self):
        parent = HTMLNode("div", "Parent")
        self.assertEqual(parent.children, [])

    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "This is a text node")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_special_characters(self):
        node = HTMLNode("p", "This is a text node", props={"data-info": "some \"special\" characters"})
        self.assertEqual(node.props_to_html(), 'data-info="some &quot;special&quot; characters"')

    def test_repr_with_children_and_props(self):
        child1 = HTMLNode("span", "Child 1")
        child2 = HTMLNode("span", "Child 2")
        parent = HTMLNode("div", "Parent", children=[child1, child2], props={"class": "parent-class"})
        self.assertEqual(repr(parent), "HTMLNode(div, Parent, [HTMLNode(span, Child 1, [], {}), HTMLNode(span, Child 2, [], {})], {'class': 'parent-class'})")

if __name__ == '__main__':
    unittest.main()