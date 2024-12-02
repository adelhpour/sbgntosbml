from .sbgn_entity_pool_node_base import SBGNEntityPoolNodeBase


class SBGNSimpleChemical(SBGNEntityPoolNodeBase):

    def get_type(self):
        return "simple chemical"

    @staticmethod
    def get_fill_color():
        return "#E4F8E4"

    def add_geometric_shape(self, sbmlnetwork_object, parent_element):
        sbmlnetwork_object.addGeometricShape(parent_element.get_id(), "ellipse")
        geometric_shape_index = sbmlnetwork_object.getNumGeometricShapes(parent_element.get_id()) - 1
        geometric_shape_id = self.get_id()
        if parent_element.get_id() == self.get_id() and geometric_shape_index > 0:
            geometric_shape_id += "_" + str(geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeId(parent_element.get_id(), geometric_shape_id,
                                               geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeCenterX(parent_element.get_id(), self.get_relative_x(
            sbmlnetwork_object.getX(parent_element.get_id())) + 0.5 * self.get_relative_width(
            sbmlnetwork_object.getWidth(parent_element.get_id())), geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeCenterY(parent_element.get_id(), self.get_relative_y(
            sbmlnetwork_object.getY(parent_element.get_id())) + 0.5 * self.get_relative_height(
            sbmlnetwork_object.getHeight(parent_element.get_id())), geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeRadiusX(parent_element.get_id(), 0.5 * self.get_relative_width(
            sbmlnetwork_object.getWidth(parent_element.get_id())), geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeRadiusY(parent_element.get_id(), 0.5 * self.get_relative_height(
            sbmlnetwork_object.getHeight(parent_element.get_id())), geometric_shape_index=geometric_shape_index)

        # border width
        sbmlnetwork_object.setGeometricShapeBorderWidth(parent_element.get_id(), self.get_border_width(), geometric_shape_index=geometric_shape_index)

        # fill color
        sbmlnetwork_object.setGeometricShapeFillColor(parent_element.get_id(), self.get_fill_color(), geometric_shape_index=geometric_shape_index)