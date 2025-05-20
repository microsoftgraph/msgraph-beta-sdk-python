from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .organization_allowed_audiences import OrganizationAllowedAudiences

from .entity import Entity

@dataclass
class ProfilePropertySetting(Entity, Parsable):
    # A privacy setting that reflects the allowed audience for the configured property. The possible values are: me, organization, federatedOrganizations, everyone, unknownFutureValue.
    allowed_audiences: Optional[OrganizationAllowedAudiences] = None
    # Defines whether a user is allowed to override the tenant admin privacy setting.
    is_user_override_for_audience_enabled: Optional[bool] = None
    # Name of the property-level setting.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of prioritized profile source URLs ordered by data precedence within an organization.
    prioritized_source_urls: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfilePropertySetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfilePropertySetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfilePropertySetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .organization_allowed_audiences import OrganizationAllowedAudiences

        from .entity import Entity
        from .organization_allowed_audiences import OrganizationAllowedAudiences

        fields: dict[str, Callable[[Any], None]] = {
            "allowedAudiences": lambda n : setattr(self, 'allowed_audiences', n.get_enum_value(OrganizationAllowedAudiences)),
            "isUserOverrideForAudienceEnabled": lambda n : setattr(self, 'is_user_override_for_audience_enabled', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "prioritizedSourceUrls": lambda n : setattr(self, 'prioritized_source_urls', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("allowedAudiences", self.allowed_audiences)
        writer.write_bool_value("isUserOverrideForAudienceEnabled", self.is_user_override_for_audience_enabled)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("prioritizedSourceUrls", self.prioritized_source_urls)
    

