from .sbgn_container_node_base import SBGNContainerNodeBase


class SBGNCompartment(SBGNContainerNodeBase):

    @staticmethod
    def get_type():
        return "compartment"

    @staticmethod
    def get_border_width():
        return 12.0

    @staticmethod
    def get_fill_color():
        return "#EEEAE4"

    @staticmethod
    def get_font_color():
        return "black"

    def add_geometric_shape(self, sbmlnetwork_object, parent_element):
        sbmlnetwork_object.addGeometricShape(parent_element.get_id(), "rectangle")
        geometric_shape_index = sbmlnetwork_object.getNumGeometricShapes(parent_element.get_id()) - 1
        geometric_shape_id = self.get_id()
        if parent_element.get_id() == self.get_id() and geometric_shape_index > 0:
            geometric_shape_id += "_" + str(geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeId(parent_element.get_id(), geometric_shape_id,
                                               geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeX(parent_element.get_id(), self.get_relative_x(
            sbmlnetwork_object.getX(parent_element.get_id())),
                                              geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeY(parent_element.get_id(), self.get_relative_y(
            sbmlnetwork_object.getY(parent_element.get_id())),
                                              geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeWidth(parent_element.get_id(), self.get_relative_width(
            sbmlnetwork_object.getWidth(parent_element.get_id())), geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeHeight(parent_element.get_id(), self.get_relative_height(
            sbmlnetwork_object.getHeight(parent_element.get_id())), geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeBorderRadiusX(parent_element.get_id(), 0.025 * self.get_width(),
                                                          geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeBorderRadiusY(parent_element.get_id(), 0.025 * self.get_height(),
                                                          geometric_shape_index=geometric_shape_index)

        # border width
        sbmlnetwork_object.setGeometricShapeBorderWidth(parent_element.get_id(), self.get_border_width(), geometric_shape_index=geometric_shape_index)

        # fill color
        sbmlnetwork_object.setGeometricShapeFillColor(parent_element.get_id(), self.get_fill_color(), geometric_shape_index=geometric_shape_index)

    def load_sbml_text_info(self, sbmlnetwork_object, parent_element=None):
        super(SBGNCompartment, self).load_sbml_text_info(sbmlnetwork_object, parent_element)

        # font color
        sbmlnetwork_object.setFontColor(parent_element.get_id(), self.get_font_color())