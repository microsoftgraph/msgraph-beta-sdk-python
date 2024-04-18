from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .password_settings import PasswordSettings
    from .role_group import RoleGroup

@dataclass
class UserConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The password settings for the users to be provisioned with.
    default_password_settings: Optional[PasswordSettings] = None
    # The license skus for the users to be provisioned with.
    license_skus: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The roleGroup property
    role_group: Optional[RoleGroup] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .password_settings import PasswordSettings
        from .role_group import RoleGroup

        from .password_settings import PasswordSettings
        from .role_group import RoleGroup

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultPasswordSettings": lambda n : setattr(self, 'default_password_settings', n.get_object_value(PasswordSettings)),
            "licenseSkus": lambda n : setattr(self, 'license_skus', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roleGroup": lambda n : setattr(self, 'role_group', n.get_object_value(RoleGroup)),
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
        writer.write_object_value("defaultPasswordSettings", self.default_password_settings)
        writer.write_collection_of_primitive_values("licenseSkus", self.license_skus)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("roleGroup", self.role_group)
        writer.write_additional_data_value(self.additional_data)
    

