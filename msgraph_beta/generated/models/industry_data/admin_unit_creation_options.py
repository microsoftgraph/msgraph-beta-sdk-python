from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AdminUnitCreationOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether the administrative unit should be created based on the org.
    create_based_on_org: Optional[bool] = None
    # Indicates whether the administrative unit should be created based on the org and role group.
    create_based_on_org_plus_role_group: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminUnitCreationOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminUnitCreationOptions
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AdminUnitCreationOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "createBasedOnOrg": lambda n : setattr(self, 'create_based_on_org', n.get_bool_value()),
            "createBasedOnOrgPlusRoleGroup": lambda n : setattr(self, 'create_based_on_org_plus_role_group', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("createBasedOnOrg", self.create_based_on_org)
        writer.write_bool_value("createBasedOnOrgPlusRoleGroup", self.create_based_on_org_plus_role_group)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

