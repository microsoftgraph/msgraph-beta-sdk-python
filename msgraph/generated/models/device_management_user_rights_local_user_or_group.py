from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceManagementUserRightsLocalUserOrGroup(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represents information for a local user or group used for user rights setting.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Admin’s description of this local user or group.
    description: Optional[str] = None
    # The name of this local user or group.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The security identifier of this local user or group (e.g. S-1-5-32-544).
    security_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementUserRightsLocalUserOrGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementUserRightsLocalUserOrGroup
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementUserRightsLocalUserOrGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "securityIdentifier": lambda n : setattr(self, 'security_identifier', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("name", self.name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("securityIdentifier", self.security_identifier)
        writer.write_additional_data_value(self.additional_data)
    

