import numpy as np

from webdnn.graph.graph import Graph
from webdnn.graph.operators.elementwise import Elementwise
from webdnn.graph.optimize_rule import OptimizeRule
from webdnn.graph.variables.constant_variable import ConstantVariable


class Cos(Elementwise):
    """Cos(name)

    Elementwise cos operator.

    Args:
        name (str): Operator name.

    Signature
        .. code::

            y, = op(x0)

        - **x0** - Input variable.
        - **y** - Output variable.
    """

    def fold_constance(self, graph: Graph):
        x0 = self.inputs["x0"]  # type: ConstantVariable
        y = self.outputs["y"]
        self.remove_all()

        OptimizeRule.replace_variable(graph, y, ConstantVariable(np.cos(x0.copy().change_order(y.order).data), y.order))
