from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .restorable_artifact import RestorableArtifact

@dataclass
class ArtifactQuery(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The type of artifact to search. The possible values are: message, unknownFutureValue.
    artifact_type: Optional[RestorableArtifact] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies criteria to retrieve artifacts.
    query_expression: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ArtifactQuery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ArtifactQuery
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ArtifactQuery()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .restorable_artifact import RestorableArtifact

        from .restorable_artifact import RestorableArtifact

        fields: dict[str, Callable[[Any], None]] = {
            "artifactType": lambda n : setattr(self, 'artifact_type', n.get_enum_value(RestorableArtifact)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "queryExpression": lambda n : setattr(self, 'query_expression', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("artifactType", self.artifact_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("queryExpression", self.query_expression)
        writer.write_additional_data_value(self.additional_data)
    

