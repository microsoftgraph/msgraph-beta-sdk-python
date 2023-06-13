from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_subject_lifecycle, connected_organization, entity

from . import entity

@dataclass
class AccessPackageSubject(entity.Entity):
    # The altSecId property
    alt_sec_id: Optional[str] = None
    # The connected organization of the subject. Read-only. Nullable.
    connected_organization: Optional[connected_organization.ConnectedOrganization] = None
    # The identifier of the connected organization of the subject.
    connected_organization_id: Optional[str] = None
    # The display name of the subject.
    display_name: Optional[str] = None
    # The email address of the subject.
    email: Optional[str] = None
    # The object identifier of the subject. null if the subject is not yet a user in the tenant.
    object_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The onPremisesSecurityIdentifier property
    on_premises_security_identifier: Optional[str] = None
    # The principal name, if known, of the subject.
    principal_name: Optional[str] = None
    # The subjectLifecycle property
    subject_lifecycle: Optional[access_package_subject_lifecycle.AccessPackageSubjectLifecycle] = None
    # The resource type of the subject.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageSubject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageSubject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_subject_lifecycle, connected_organization, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "altSecId": lambda n : setattr(self, 'alt_sec_id', n.get_str_value()),
            "connectedOrganization": lambda n : setattr(self, 'connected_organization', n.get_object_value(connected_organization.ConnectedOrganization)),
            "connectedOrganizationId": lambda n : setattr(self, 'connected_organization_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "principalName": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "subjectLifecycle": lambda n : setattr(self, 'subject_lifecycle', n.get_enum_value(access_package_subject_lifecycle.AccessPackageSubjectLifecycle)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("altSecId", self.alt_sec_id)
        writer.write_object_value("connectedOrganization", self.connected_organization)
        writer.write_str_value("connectedOrganizationId", self.connected_organization_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_str_value("principalName", self.principal_name)
        writer.write_enum_value("subjectLifecycle", self.subject_lifecycle)
        writer.write_str_value("type", self.type)
    

