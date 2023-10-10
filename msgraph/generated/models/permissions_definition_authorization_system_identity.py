from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource
    from .permissions_definition_identity_type import PermissionsDefinitionIdentityType

@dataclass
class PermissionsDefinitionAuthorizationSystemIdentity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The externalId property
    external_id: Optional[str] = None
    # The identityType property
    identity_type: Optional[PermissionsDefinitionIdentityType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source property
    source: Optional[PermissionsDefinitionIdentitySource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionsDefinitionAuthorizationSystemIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsDefinitionAuthorizationSystemIdentity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PermissionsDefinitionAuthorizationSystemIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource
        from .permissions_definition_identity_type import PermissionsDefinitionIdentityType

        from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource
        from .permissions_definition_identity_type import PermissionsDefinitionIdentityType

        fields: Dict[str, Callable[[Any], None]] = {
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "identityType": lambda n : setattr(self, 'identity_type', n.get_enum_value(PermissionsDefinitionIdentityType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(PermissionsDefinitionIdentitySource)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("externalId", self.external_id)
        writer.write_enum_value("identityType", self.identity_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

