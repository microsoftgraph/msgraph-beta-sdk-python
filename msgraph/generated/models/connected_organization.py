from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connected_organization_state import ConnectedOrganizationState
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .identity_source import IdentitySource

from .entity import Entity

@dataclass
class ConnectedOrganization(Entity):
    # UPN of the user who created this resource. Read-only.
    created_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The description of the connected organization.
    description: Optional[str] = None
    # The display name of the connected organization. Supports $filter (eq).
    display_name: Optional[str] = None
    # The externalSponsors property
    external_sponsors: Optional[List[DirectoryObject]] = None
    # The identity sources in this connected organization, one of azureActiveDirectoryTenant, crossCloudAzureActiveDirectoryTenant, domainIdentitySource or externalDomainFederation. Read-only. Nullable. Supports $select and $filter(eq). To filter by the derived types, you must declare the resource using its full OData cast, for example, $filter=identitySources/any(is:is/microsoft.graph.azureActiveDirectoryTenant/tenantId eq 'bcfdfff4-cbc3-43f2-9000-ba7b7515054f').
    identity_sources: Optional[List[IdentitySource]] = None
    # The internalSponsors property
    internal_sponsors: Optional[List[DirectoryObject]] = None
    # UPN of the user who last modified this resource. Read-only.
    modified_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of a connected organization defines whether assignment policies with requestor scope type AllConfiguredConnectedOrganizationSubjects are applicable or not. Possible values are: configured, proposed.
    state: Optional[ConnectedOrganizationState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectedOrganization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectedOrganization
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConnectedOrganization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .connected_organization_state import ConnectedOrganizationState
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .identity_source import IdentitySource

        from .connected_organization_state import ConnectedOrganizationState
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .identity_source import IdentitySource

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalSponsors": lambda n : setattr(self, 'external_sponsors', n.get_collection_of_object_values(DirectoryObject)),
            "identitySources": lambda n : setattr(self, 'identity_sources', n.get_collection_of_object_values(IdentitySource)),
            "internalSponsors": lambda n : setattr(self, 'internal_sponsors', n.get_collection_of_object_values(DirectoryObject)),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ConnectedOrganizationState)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("externalSponsors", self.external_sponsors)
        writer.write_collection_of_object_values("identitySources", self.identity_sources)
        writer.write_collection_of_object_values("internalSponsors", self.internal_sponsors)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_enum_value("state", self.state)
    

