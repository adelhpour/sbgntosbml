from numpy.random import geometric

from .sbgn_connecting_arc_base import SBGNConnectingArcBase


class SBGNStimulation(SBGNConnectingArcBase):

    def __init__(self, element_id, source_id, target_id, start_x, start_y, end_x, end_y, intermediate_points=None, sub_elements=None):
        super(SBGNStimulation, self).__init__(element_id, source_id, target_id, start_x, start_y, end_x, end_y, intermediate_points, sub_elements)
        self.line_ending_horizontal_padding = -3.5

    @staticmethod
    def get_type():
        return "stimulation"

    def set_geometric_shape_features(self, sbmlnetwork_object, reaction, species):
        super(SBGNStimulation, self).set_geometric_shape_features(sbmlnetwork_object, reaction, species)
        species_reference_index = sbmlnetwork_object.getSpeciesReferenceIndexAssociatedWithSpecies(species.get_id(),
                                                                                                   reaction.get_id())
        sbmlnetwork_object.setSpeciesReferenceLineEndingGeometricShapeType(reaction.get_id(), "triangle",
                                                                           species_reference_index=species_reference_index)
        geometric_shape_index = sbmlnetwork_object.getNumSpeciesReferenceLineEndingGeometricShapes(reaction.get_id(),
                                                                                                   species_reference_index=species_reference_index) - 1
        sbmlnetwork_object.setSpeciesReferenceLineEndingGeometricShapeSegmentX(reaction.get_id(), x=0.0,
                                                                               segment_index=0,
                                                                               species_reference_index=species_reference_index,
                                                                               index=geometric_shape_index)
        sbmlnetwork_object.setSpeciesReferenceLineEndingGeometricShapeSegmentY(reaction.get_id(), y=0.0,
                                                                               segment_index=0, layout_index=0,
                                                                               species_reference_index=species_reference_index,
                                                                               index=geometric_shape_index)
        sbmlnetwork_object.setSpeciesReferenceLineEndingGeometricShapeSegmentX(reaction.get_id(), x=12.0,
                                                                               segment_index=1,
                                                                               species_reference_index=species_reference_index,
                                                                               index=geometric_shape_index)
        sbmlnetwork_object.setSpeciesReferenceLineEndingGeometricShapeSegmentY(reaction.get_id(), y=6.0,
                                                                               segment_index=1, layout_index=0,
                                                                               species_reference_index=species_reference_index,
                                                                               index=geometric_shape_index)
        sbmlnetwork_object.setSpeciesReferenceLineEndingGeometricShapeSegmentX(reaction.get_id(), x=0.0,
                                                                               segment_index=2,
                                                                               species_reference_index=species_reference_index,
                                                                               index=geometric_shape_index)
        sbmlnetwork_object.setSpeciesReferenceLineEndingGeometricShapeSegmentY(reaction.get_id(), y=12.0,
                                                                               segment_index=2, layout_index=0,
                                                                               species_reference_index=species_reference_index,
                                                                               index=geometric_shape_index)
        sbmlnetwork_object.setSpeciesReferenceLineEndingBorderColor(reaction.get_id(), border_color="black",
                                                                    species_reference_index=species_reference_index)
        sbmlnetwork_object.setSpeciesReferenceLineEndingFillColor(reaction.get_id(), fill_color="white",
                                                                  species_reference_index=species_reference_index)