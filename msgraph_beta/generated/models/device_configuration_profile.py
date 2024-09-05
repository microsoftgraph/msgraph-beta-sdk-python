from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .platform_type import PlatformType
    from .profile_type import ProfileType

from .entity import Entity

@dataclass
class DeviceConfigurationProfile(Entity):
    """
    The listing service profile entity contains the meta data of an Intune configuration profile 
    """
    # Account Id.
    account_id: Optional[str] = None
    # Configuration Technologies for Settins Catalog Policies
    configuration_technologies: Optional[int] = None
    # The date and time the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time the entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Platform Type
    platform_type: Optional[PlatformType] = None
    # Profile name
    profile_name: Optional[str] = None
    # Profile Type
    profile_type: Optional[ProfileType] = None
    # The list of scope tags for the configuration.
    role_scope_tag_ids: Optional[List[str]] = None
    # TemplateId for Settings Catalog Policies
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceConfigurationProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceConfigurationProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .platform_type import PlatformType
        from .profile_type import ProfileType

        from .entity import Entity
        from .platform_type import PlatformType
        from .profile_type import ProfileType

        fields: Dict[str, Callable[[Any], None]] = {
            "accountId": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "configurationTechnologies": lambda n : setattr(self, 'configuration_technologies', n.get_int_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(PlatformType)),
            "profileName": lambda n : setattr(self, 'profile_name', n.get_str_value()),
            "profileType": lambda n : setattr(self, 'profile_type', n.get_enum_value(ProfileType)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("accountId", self.account_id)
        writer.write_int_value("configurationTechnologies", self.configuration_technologies)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_str_value("profileName", self.profile_name)
        writer.write_enum_value("profileType", self.profile_type)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_str_value("templateId", self.template_id)
    

