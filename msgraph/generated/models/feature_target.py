from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import feature_target_type

@dataclass
class FeatureTarget(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The ID of the entity that's targeted in the include or exclude rule or all_users to target all users.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The kind of entity that's targeted. The possible values are: group, administrativeUnit, role, unknownFutureValue.
    target_type: Optional[feature_target_type.FeatureTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FeatureTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FeatureTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FeatureTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import feature_target_type

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(feature_target_type.FeatureTargetType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("targetType", self.target_type)
        writer.write_additional_data_value(self.additional_data)
    

