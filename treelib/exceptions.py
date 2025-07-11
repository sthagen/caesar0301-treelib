class NodePropertyError(Exception):
    """Basic Node attribute error"""


class NodeIDAbsentError(NodePropertyError):
    """Exception throwed if a node's identifier is unknown"""


class NodePropertyAbsentError(NodePropertyError):
    """Exception throwed if a node's data property is not specified"""


class MultipleRootError(Exception):
    """Exception throwed if more than one root exists in a tree."""


class DuplicatedNodeIdError(Exception):
    """Exception throwed if an identifier already exists in a tree."""


class LinkPastRootNodeError(Exception):
    """
    Exception throwed in Tree.link_past_node() if one attempts
    to "link past" the root node of a tree.
    """


class InvalidLevelNumber(Exception):
    pass


class LoopError(Exception):
    """
    Exception thrown if trying to move node B to node A's position
    while A is B's ancestor.
    """
