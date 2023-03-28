from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import connected_organization_state, directory_object, entity, identity_source

from . import entity

class ConnectedOrganization(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new connectedOrganization and sets the default values.
        """
        super().__init__()
        # UPN of the user who created this resource. Read-only.
        self._created_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The description of the connected organization.
        self._description: Optional[str] = None
        # The display name of the connected organization. Supports $filter (eq).
        self._display_name: Optional[str] = None
        # The externalSponsors property
        self._external_sponsors: Optional[List[directory_object.DirectoryObject]] = None
        # The identity sources in this connected organization, one of azureActiveDirectoryTenant, crossCloudAzureActiveDirectoryTenant, domainIdentitySource or externalDomainFederation. Read-only. Nullable. Supports $select and $filter(eq). To filter by the derived types, you must declare the resource using its full OData cast, for example, $filter=identitySources/any(is:is/microsoft.graph.azureActiveDirectoryTenant/tenantId eq 'bcfdfff4-cbc3-43f2-9000-ba7b7515054f').
        self._identity_sources: Optional[List[identity_source.IdentitySource]] = None
        # The internalSponsors property
        self._internal_sponsors: Optional[List[directory_object.DirectoryObject]] = None
        # UPN of the user who last modified this resource. Read-only.
        self._modified_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The state of a connected organization defines whether assignment policies with requestor scope type AllConfiguredConnectedOrganizationSubjects are applicable or not. Possible values are: configured, proposed.
        self._state: Optional[connected_organization_state.ConnectedOrganizationState] = None
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. UPN of the user who created this resource. Read-only.
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. UPN of the user who created this resource. Read-only.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectedOrganization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectedOrganization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConnectedOrganization()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the connected organization.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the connected organization.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the connected organization. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the connected organization. Supports $filter (eq).
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def external_sponsors(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the externalSponsors property value. The externalSponsors property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._external_sponsors
    
    @external_sponsors.setter
    def external_sponsors(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the externalSponsors property value. The externalSponsors property
        Args:
            value: Value to set for the external_sponsors property.
        """
        self._external_sponsors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import connected_organization_state, directory_object, entity, identity_source

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalSponsors": lambda n : setattr(self, 'external_sponsors', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "identitySources": lambda n : setattr(self, 'identity_sources', n.get_collection_of_object_values(identity_source.IdentitySource)),
            "internalSponsors": lambda n : setattr(self, 'internal_sponsors', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(connected_organization_state.ConnectedOrganizationState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_sources(self,) -> Optional[List[identity_source.IdentitySource]]:
        """
        Gets the identitySources property value. The identity sources in this connected organization, one of azureActiveDirectoryTenant, crossCloudAzureActiveDirectoryTenant, domainIdentitySource or externalDomainFederation. Read-only. Nullable. Supports $select and $filter(eq). To filter by the derived types, you must declare the resource using its full OData cast, for example, $filter=identitySources/any(is:is/microsoft.graph.azureActiveDirectoryTenant/tenantId eq 'bcfdfff4-cbc3-43f2-9000-ba7b7515054f').
        Returns: Optional[List[identity_source.IdentitySource]]
        """
        return self._identity_sources
    
    @identity_sources.setter
    def identity_sources(self,value: Optional[List[identity_source.IdentitySource]] = None) -> None:
        """
        Sets the identitySources property value. The identity sources in this connected organization, one of azureActiveDirectoryTenant, crossCloudAzureActiveDirectoryTenant, domainIdentitySource or externalDomainFederation. Read-only. Nullable. Supports $select and $filter(eq). To filter by the derived types, you must declare the resource using its full OData cast, for example, $filter=identitySources/any(is:is/microsoft.graph.azureActiveDirectoryTenant/tenantId eq 'bcfdfff4-cbc3-43f2-9000-ba7b7515054f').
        Args:
            value: Value to set for the identity_sources property.
        """
        self._identity_sources = value
    
    @property
    def internal_sponsors(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the internalSponsors property value. The internalSponsors property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._internal_sponsors
    
    @internal_sponsors.setter
    def internal_sponsors(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the internalSponsors property value. The internalSponsors property
        Args:
            value: Value to set for the internal_sponsors property.
        """
        self._internal_sponsors = value
    
    @property
    def modified_by(self,) -> Optional[str]:
        """
        Gets the modifiedBy property value. UPN of the user who last modified this resource. Read-only.
        Returns: Optional[str]
        """
        return self._modified_by
    
    @modified_by.setter
    def modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the modifiedBy property value. UPN of the user who last modified this resource. Read-only.
        Args:
            value: Value to set for the modified_by property.
        """
        self._modified_by = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the modified_date_time property.
        """
        self._modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def state(self,) -> Optional[connected_organization_state.ConnectedOrganizationState]:
        """
        Gets the state property value. The state of a connected organization defines whether assignment policies with requestor scope type AllConfiguredConnectedOrganizationSubjects are applicable or not. Possible values are: configured, proposed.
        Returns: Optional[connected_organization_state.ConnectedOrganizationState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[connected_organization_state.ConnectedOrganizationState] = None) -> None:
        """
        Sets the state property value. The state of a connected organization defines whether assignment policies with requestor scope type AllConfiguredConnectedOrganizationSubjects are applicable or not. Possible values are: configured, proposed.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

