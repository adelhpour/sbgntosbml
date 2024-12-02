from .sbgn_process_node_base import SBGNProcessNodeBase


class SBGNProcess(SBGNProcessNodeBase):

    def get_type(self):
        return "process"

    def add_geometric_shape(self, sbmlnetwork_object, parent_element):
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



