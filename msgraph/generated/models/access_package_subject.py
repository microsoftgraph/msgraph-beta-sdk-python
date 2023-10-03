from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_subject_lifecycle import AccessPackageSubjectLifecycle
    from .connected_organization import ConnectedOrganization
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageSubject(Entity):
    # Not Supported.
    alt_sec_id: Optional[str] = None
    # The date and time the subject is marked to be blocked from sign in or deleted. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time.
    cleanup_scheduled_date_time: Optional[datetime.datetime] = None
    # The connected organization of the subject. Read-only. Nullable.
    connected_organization: Optional[ConnectedOrganization] = None
    # The identifier of the connected organization of the subject.
    connected_organization_id: Optional[str] = None
    # The display name of the subject.
    display_name: Optional[str] = None
    # The email address of the subject.
    email: Optional[str] = None
    # The object identifier of the subject. null if the subject isn't yet a user in the tenant. Alternate key.
    object_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The onPremisesSecurityIdentifier property
    on_premises_security_identifier: Optional[str] = None
    # The principal name, if known, of the subject.
    principal_name: Optional[str] = None
    # The lifecycle of the subject user, if a guest. The possible values are: notDefined, notGoverned, governed, unknownFutureValue.
    subject_lifecycle: Optional[AccessPackageSubjectLifecycle] = None
    # The resource type of the subject.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageSubject
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageSubject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_subject_lifecycle import AccessPackageSubjectLifecycle
        from .connected_organization import ConnectedOrganization
        from .entity import Entity

        from .access_package_subject_lifecycle import AccessPackageSubjectLifecycle
        from .connected_organization import ConnectedOrganization
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "altSecId": lambda n : setattr(self, 'alt_sec_id', n.get_str_value()),
            "cleanupScheduledDateTime": lambda n : setattr(self, 'cleanup_scheduled_date_time', n.get_datetime_value()),
            "connectedOrganization": lambda n : setattr(self, 'connected_organization', n.get_object_value(ConnectedOrganization)),
            "connectedOrganizationId": lambda n : setattr(self, 'connected_organization_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "onPremisesSecurityIdentifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "principalName": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "subjectLifecycle": lambda n : setattr(self, 'subject_lifecycle', n.get_enum_value(AccessPackageSubjectLifecycle)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("altSecId", self.alt_sec_id)
        writer.write_datetime_value("cleanupScheduledDateTime", self.cleanup_scheduled_date_time)
        writer.write_object_value("connectedOrganization", self.connected_organization)
        writer.write_str_value("connectedOrganizationId", self.connected_organization_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("onPremisesSecurityIdentifier", self.on_premises_security_identifier)
        writer.write_str_value("principalName", self.principal_name)
        writer.write_enum_value("subjectLifecycle", self.subject_lifecycle)
        writer.write_str_value("type", self.type)
    

