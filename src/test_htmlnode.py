import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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