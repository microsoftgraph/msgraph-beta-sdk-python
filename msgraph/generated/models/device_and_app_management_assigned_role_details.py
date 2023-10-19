from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceAndAppManagementAssignedRoleDetails(AdditionalDataHolder, BackedModel, Parsable):
    """
    The set of Role Definitions and Role Assignments assigned to a user.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Role Assignment IDs for the specifc Role Assignments assigned to a user. This property is read-only.
    role_assignment_ids: Optional[List[str]] = None
    # Role Definition IDs for the specifc Role Definitions assigned to a user. This property is read-only.
    role_definition_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignedRoleDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignedRoleDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceAndAppManagementAssignedRoleDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roleAssignmentIds": lambda n : setattr(self, 'role_assignment_ids', n.get_collection_of_primitive_values(str)),
            "roleDefinitionIds": lambda n : setattr(self, 'role_definition_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

