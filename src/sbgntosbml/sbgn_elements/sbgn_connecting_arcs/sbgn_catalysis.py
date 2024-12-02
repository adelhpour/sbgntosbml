from .sbgn_connecting_arc_base import SBGNConnectingArcBase


class SBGNCatalysis(SBGNConnectingArcBase):

    def __init__(self, element_id, source_id, target_id, start_x, start_y, end_x, end_y, intermediate_points=None, sub_elements=None):
        super(SBGNCatalysis, self).__init__(element_id, source_id, target_id, start_x, start_y, end_x, end_y, intermediate_points, sub_elements)
        self.line_ending_horizontal_padding = -3.5

    @staticmethod
    def get_type():
        return "catalysis"


