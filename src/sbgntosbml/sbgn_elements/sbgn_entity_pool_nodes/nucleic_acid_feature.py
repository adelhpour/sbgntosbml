from .sbgn_entity_pool_node_base import SBGNEntityPoolNodeBase
import math


class SBGNNucleicAcidFeature(SBGNEntityPoolNodeBase):

    def get_type(self):
        return "nucleic acid feature"

    def add_geometric_shape(self, sbmlnetwork_object, parent_element):
        sbmlnetwork_object.addGeometricShape(parent_element.get_id(), "octagon")
        geometric_shape_index = sbmlnetwork_object.getNumGeometricShapes(parent_element.get_id()) - 1
        sbmlnetwork_object.setGeometricShapeId(parent_element.get_id(), self.get_id(),
                                               geometric_shape_index=geometric_shape_index)
        horizontal_edge_ratio = 0.1
        vertical_edge_ratio = 0.1
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(), 0.0, segment_index=0,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(), 0.0, segment_index=0,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(),
                                                     sbmlnetwork_object.getWidth(parent_element.get_id()),
                                                     segment_index=1, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(), 0.0, segment_index=1,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(),
                                                     sbmlnetwork_object.getWidth(parent_element.get_id()),
                                                     segment_index=2, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(),
                                                     (1 - vertical_edge_ratio) * sbmlnetwork_object.getHeight(
                                                         parent_element.get_id()), segment_index=2,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(), (
                1 - 0.5 * (1.0 / math.sqrt(2)) * horizontal_edge_ratio) * sbmlnetwork_object.getWidth(
            parent_element.get_id()), segment_index=3, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(), (
                1 - 0.5 * (1.0 / math.sqrt(2)) * vertical_edge_ratio) * sbmlnetwork_object.getHeight(
            parent_element.get_id()), segment_index=3, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(),
                                                     (1 - horizontal_edge_ratio) * sbmlnetwork_object.getWidth(
                                                         parent_element.get_id()), segment_index=4,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(),
                                                     sbmlnetwork_object.getHeight(parent_element.get_id()),
                                                     segment_index=4, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(),
                                                     horizontal_edge_ratio * sbmlnetwork_object.getWidth(
                                                         parent_element.get_id()), segment_index=5,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(),
                                                     sbmlnetwork_object.getHeight(parent_element.get_id()),
                                                     segment_index=5, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(), 0.5 * horizontal_edge_ratio * (
                1.0 / math.sqrt(2)) * sbmlnetwork_object.getWidth(parent_element.get_id()), segment_index=6,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(), (
                1 - 0.5 * (1.0 / math.sqrt(2)) * vertical_edge_ratio) * sbmlnetwork_object.getHeight(
            parent_element.get_id()), segment_index=6, geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentX(parent_element.get_id(), 0.0, segment_index=7,
                                                     geometric_shape_index=geometric_shape_index)
        sbmlnetwork_object.setGeometricShapeSegmentY(parent_element.get_id(),
                                                     (1 - vertical_edge_ratio) * sbmlnetwork_object.getHeight(
                                                         parent_element.get_id()), segment_index=7,
                                                     geometric_shape_index=geometric_shape_index)

        # border width
        sbmlnetwork_object.setGeometricShapeBorderWidth(parent_element.get_id(), self.get_border_width(), geometric_shape_index=geometric_shape_index)