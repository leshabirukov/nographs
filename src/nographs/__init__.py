# In the following, all API elements are listed that are
# not private of the module that defines it.
# The elements that are ment to be package private, are
# commented out to document this property.
# All other elements are imported and exported "flat"
# as direct elements of the package.

from ._types import (
    # TypeVars, type aliases, and protocols that are used in NoGraphs to describe its
    # API and to specify type annotations. They are exported only for the rare use
    # case that an applications bases own type annotations on them.
    # vertex_as_id is the only exception, it is defined here because
    # it is used as a singleton, and is the only predefined instance of VertexToID.
    T,
    Weight,
    T_vertex,
    T_vertex_id,
    T_weight,
    T_labels,
    VertexToID,
    vertex_as_id,
    UnweightedLabeledOutEdge,
    WeightedUnlabeledOutEdge,
    WeightedLabeledOutEdge,
    WeightedOutEdge,
    LabeledOutEdge,
    OutEdge,
    UnweightedUnlabeledFullEdge,
    UnweightedLabeledFullEdge,
    WeightedFullEdge,
    WeightedOrLabeledFullEdge,
)
from ._gear_collections import (
    # --- Gear collection types ---
    VertexSet,
    VertexMapping,
    # --- Gear collections for dense integer keys ---
    # -- Protocols for the used kind of sequences and the wrappers
    # (Only needed for defining/configuring new gears)
    GettableSettableForGearProto,
    SequenceForGearProto,
    VertexSequenceWrapperForSetProto,
    VertexSequenceWrapperForMappingProto,
    # -- ABCs and helper functions to allow for type-save down casts
    # get_wrapper_from_vertex_set,
    # access_to_vertex_set,
    # get_wrapper_from_vertex_mapping,
    # access_to_vertex_mapping_expect_none,
    # access_to_vertex_mapping,
    # -- Implementations or VertexSet/VertexMapping based on wrappers
    # (needed to define new gears that are based on sequences)
    VertexSetWrappingSequence,
    VertexSetWrappingSequenceNoBitPacking,
    VertexSetWrappingSequenceBitPacking,
    VertexMappingWrappingSequence,
    VertexMappingWrappingSequenceWithNone,
    VertexMappingWrappingSequenceWithoutNone,
)
from ._gears import (
    # -- ABCs for the needed collection kinds for NoGraphs
    # (Used library-internal to better document special semantics of some objects)
    # VertexIdSet,
    # VertexIdToVertexMapping,
    # VertexIdToDistanceMapping,
    # VertexIdToPathEdgeDataMapping,
    # MutableSequenceOfVertices,
    # -- Gear protocols
    GearWithoutDistances,
    Gear,
    # -- Concrete gears
    GearForHashableVertexIDs,
    GearDefault,
    GearForHashableVertexIDsAndIntsMaybeFloats,
    GearForHashableVertexIDsAndFloats,
    GearForHashableVertexIDsAndDecimals,
    GearForIntVertexIDs,
    GearForIntVertexIDsAndIntsMaybeFloats,
    GearForIntVertexIDsAndDecimals,
    GearForIntVertexIDsAndCFloats,
    GearForIntVertexIDsAndCInts,
    GearForIntVerticesAndIDs,
    GearForIntVerticesAndIDsAndIntsMaybeFloats,
    GearForIntVerticesAndIDsAndDecimals,
    GearForIntVerticesAndIDsAndCFloats,
    GearForIntVerticesAndIDsAndCInts,
)
from ._paths import (
    Paths,
    # PathsOfUnlabeledEdges,
    # PathsOfLabeledEdges,
    # PathsDummy,
    # DummyPredecessorOrAttributesMapping,
)
from ._strategies import (
    # StrRepr,
    Strategy,
    T_strategy,
    NextVertices,  # Usable, in rare cases, for typing application-defined functions
    NextEdges,
    NextLabeledEdges,
    NextWeightedEdges,
    NextWeightedLabeledEdges,
    # NextEdgesOrVertices,
    # NextWeightedMaybeLabeledEdges,
    BNextVertices,
    BNextEdges,
    BNextLabeledEdges,
    BNextWeightedEdges,
    BNextWeightedLabeledEdges,
    # BNextEdgesOrVertices,
    # BNextWeightedMaybeLabeledEdges,
    # iter_start_ids,
    # iter_start_vertices_and_ids,
    # define_visited,
    # define_distances,
    # create_paths,
    # NoIterator,
    # NoVisitedSet,
    # NoDistancesMapping,
)
from ._traversals import (
    Traversal,
    TraversalBreadthFirstFlex,
    TraversalBreadthFirst,
    TraversalDepthFirstFlex,
    TraversalDepthFirst,
    TraversalNeighborsThenDepthFlex,
    TraversalNeighborsThenDepth,
    TraversalTopologicalSortFlex,
    TraversalTopologicalSort,
    TraversalShortestPathsFlex,
    TraversalShortestPaths,
    TraversalAStarFlex,
    TraversalAStar,
    TraversalMinimumSpanningTreeFlex,
    TraversalMinimumSpanningTree,
)
from ._path import Path
from ._bidir_search import (
    BSearchBreadthFirstFlex,
    BSearchBreadthFirst,
    BSearchShortestPathFlex,
    BSearchShortestPath,
)
from ._matrix_gadgets import (
    Vector,
    Limits,
    Position,
    Array,
)
from ._edge_gadgets import (
    adapt_edge_index,
    adapt_edge_iterable,
)

__all__ = (
    # -- types --
    "T",
    "Weight",
    "T_vertex",
    "T_vertex_id",
    "T_weight",
    "T_labels",
    "VertexToID",
    "vertex_as_id",
    "UnweightedLabeledOutEdge",
    "WeightedUnlabeledOutEdge",
    "WeightedLabeledOutEdge",
    "WeightedOutEdge",
    "LabeledOutEdge",
    "OutEdge",
    "UnweightedUnlabeledFullEdge",
    "UnweightedLabeledFullEdge",
    "WeightedFullEdge",
    "WeightedOrLabeledFullEdge",
    # -- gear collections --
    "VertexSet",
    "VertexMapping",
    "GettableSettableForGearProto",
    "SequenceForGearProto",
    "VertexSequenceWrapperForSetProto",
    "VertexSequenceWrapperForMappingProto",
    "VertexSetWrappingSequence",
    "VertexSetWrappingSequenceNoBitPacking",
    "VertexSetWrappingSequenceBitPacking",
    "VertexMappingWrappingSequence",
    "VertexMappingWrappingSequenceWithNone",
    "VertexMappingWrappingSequenceWithoutNone",
    # -- gears --
    "GearWithoutDistances",
    "Gear",
    "GearForHashableVertexIDs",
    "GearDefault",
    "GearForHashableVertexIDsAndIntsMaybeFloats",
    "GearForHashableVertexIDsAndFloats",
    "GearForHashableVertexIDsAndDecimals",
    "GearForIntVertexIDs",
    "GearForIntVertexIDsAndIntsMaybeFloats",
    "GearForIntVertexIDsAndDecimals",
    "GearForIntVertexIDsAndCFloats",
    "GearForIntVertexIDsAndCFloats",
    "GearForIntVerticesAndIDs",
    "GearForIntVerticesAndIDsAndIntsMaybeFloats",
    "GearForIntVerticesAndIDsAndDecimals",
    "GearForIntVerticesAndIDsAndCFloats",
    "GearForIntVerticesAndIDsAndCInts",
    "GearForIntVertexIDsAndCInts",
    # -- paths --
    "Paths",
    # -- path --
    "Path",
    # -- strategy --
    "Strategy",
    "T_strategy",
    "NextVertices",
    "NextEdges",
    "NextLabeledEdges",
    "NextWeightedEdges",
    "NextWeightedLabeledEdges",
    "BNextVertices",
    "BNextEdges",
    "BNextLabeledEdges",
    "BNextWeightedEdges",
    "BNextWeightedLabeledEdges",
    # -- traversal --
    "Traversal",
    "TraversalBreadthFirstFlex",
    "TraversalBreadthFirst",
    "TraversalDepthFirstFlex",
    "TraversalDepthFirst",
    "TraversalNeighborsThenDepthFlex",
    "TraversalNeighborsThenDepth",
    "TraversalTopologicalSortFlex",
    "TraversalTopologicalSort",
    "TraversalShortestPathsFlex",
    "TraversalShortestPaths",
    "TraversalAStarFlex",
    "TraversalAStar",
    "TraversalMinimumSpanningTreeFlex",
    "TraversalMinimumSpanningTree",
    # -- bidir search --
    "BSearchBreadthFirstFlex",
    "BSearchBreadthFirst",
    "BSearchShortestPathFlex",
    "BSearchShortestPath",
    # -- matrix gadgets --
    "Vector",
    "Limits",
    "Position",
    "Array",
    # -- edge gadgets --
    "adapt_edge_index",
    "adapt_edge_iterable",
)
