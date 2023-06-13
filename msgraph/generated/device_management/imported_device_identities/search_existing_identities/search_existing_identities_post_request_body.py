from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import imported_device_identity

@dataclass
class SearchExistingIdentitiesPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The importedDeviceIdentities property
    imported_device_identities: Optional[List[imported_device_identity.ImportedDeviceIdentity]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchExistingIdentitiesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchExistingIdentitiesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchExistingIdentitiesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import imported_device_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "importedDeviceIdentities": lambda n : setattr(self, 'imported_device_identities', n.get_collection_of_object_values(imported_device_identity.ImportedDeviceIdentity)),
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
        writer.write_collection_of_object_values("importedDeviceIdentities", self.imported_device_identities)
        writer.write_additional_data_value(self.additional_data)
    

