from .sbgn_entity_pool_node_base import SBGNEntityPoolNodeBase
import math


class SBGNUnitOfInformation(SBGNEntityPoolNodeBase):

    def __init__(self, node_id, x, y, width, height, text="", text_x=math.nan, text_y=math.nan, text_width=math.nan,
                 text_height=math.nan,
                 font_size=11, text_vertical_alignment="middle", text_horizontal_alignment="middle", sub_elements=None):
        super(SBGNUnitOfInformation, self).__init__(node_id, x, y, width, height, text, text_x, text_y, text_width,
                                                     text_height,
                                                     font_size, text_vertical_alignment, text_horizontal_alignment,
                                                     sub_elements)

    def get_type(self):
        return "unit of information"

    @staticmethod
    def get_fill_color():
        return "white"

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
        sbmlnetwork_object.setGeometricShapeBorderRadiusX(parent_element.get_id(), 0.0,
                                                          geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeBorderRadiusY(parent_element.get_id(), 0.0,
                                                          geometric_shape_index=geometric_shape_index)

        # border width
        sbmlnetwork_object.setGeometricShapeBorderWidth(parent_element.get_id(), self.get_border_width(), geometric_shape_index=geometric_shape_index)

        # fill color
        sbmlnetwork_object.setGeometricShapeFillColor(parent_element.get_id(), self.get_fill_color(), geometric_shape_index=geometric_shape_index)