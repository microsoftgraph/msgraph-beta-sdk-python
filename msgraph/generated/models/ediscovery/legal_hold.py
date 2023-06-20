from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import legal_hold_status, site_source, unified_group_source, user_source
    from .. import entity, identity_set

from .. import entity

@dataclass
class LegalHold(entity.Entity):
    # KQL query that specifies content to be held in the specified locations. To learn more, see Keyword queries and search conditions for Content Search and eDiscovery.  To hold all content in the specified locations, leave contentQuery blank.
    content_query: Optional[str] = None
    # The user who created the legal hold.
    created_by: Optional[identity_set.IdentitySet] = None
    # The date and time the legal hold was created.
    created_date_time: Optional[datetime] = None
    # The legal hold description.
    description: Optional[str] = None
    # The display name of the legal hold.
    display_name: Optional[str] = None
    # Lists any errors that happened while placing the hold.
    errors: Optional[List[str]] = None
    # Indicates whether the hold is enabled and actively holding content.
    is_enabled: Optional[bool] = None
    # the user who last modified the legal hold.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The date and time the legal hold was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Data source entity for SharePoint sites associated with the legal hold.
    site_sources: Optional[List[site_source.SiteSource]] = None
    # The status of the legal hold. Possible values are: Pending, Error, Success, UnknownFutureValue.
    status: Optional[legal_hold_status.LegalHoldStatus] = None
    # The unifiedGroupSources property
    unified_group_sources: Optional[List[unified_group_source.UnifiedGroupSource]] = None
    # Data source entity for a the legal hold. This is the container for a mailbox and OneDrive for Business site.
    user_sources: Optional[List[user_source.UserSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LegalHold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LegalHold
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LegalHold()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import legal_hold_status, site_source, unified_group_source, user_source
        from .. import entity, identity_set

        from . import legal_hold_status, site_source, unified_group_source, user_source
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "contentQuery": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_primitive_values(str)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "siteSources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(site_source.SiteSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(legal_hold_status.LegalHoldStatus)),
            "unifiedGroupSources": lambda n : setattr(self, 'unified_group_sources', n.get_collection_of_object_values(unified_group_source.UnifiedGroupSource)),
            "userSources": lambda n : setattr(self, 'user_sources', n.get_collection_of_object_values(user_source.UserSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("contentQuery", self.content_query)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("errors", self.errors)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("unifiedGroupSources", self.unified_group_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    

