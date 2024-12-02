from .sbgn_port_base import SBGNPortBase

class SBGNPort(SBGNPortBase):

    def __init__(self, port_id, x, y, sub_elements=None):
        super(SBGNPortBase, self).__init__(port_id, x, y, sub_elements)

    def add_geometric_shape(self, sbmlnetwork_object, parent_element):
        sbmlnetwork_object.addGeometricShape(parent_element.get_id(), "rendercurve")
        geometric_shape_index = sbmlnetwork_object.getNumGeometricShapes(parent_element.get_id()) - 1
        geometric_shape_id = self.get_id()
        if parent_element.get_id() == self.get_id() and geometric_shape_index > 0:
            geometric_shape_id += "_" + str(geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeId(parent_element.get_id(), geometric_shape_id,
                                               geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.getGeometricShapeId(parent_element.get_id(), geometric_shape_index)
        relative_start_point_x, relative_start_point_y = self.get_relative_start_point(sbmlnetwork_object, parent_element)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(), relative_start_point_x, segment_index=0, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(), relative_start_point_y, segment_index=0, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(),
                                                     self.get_relative_x(sbmlnetwork_object.getX(parent_element.get_id())),
                                                     segment_index=1, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(),
                                                        self.get_relative_y(sbmlnetwork_object.getY(parent_element.get_id())),
                                                        segment_index=1, geometric_shape_index=geometric_shape_index)


