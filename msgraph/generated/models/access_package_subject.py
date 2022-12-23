from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_subject_lifecycle = lazy_import('msgraph.generated.models.access_package_subject_lifecycle')
connected_organization = lazy_import('msgraph.generated.models.connected_organization')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageSubject(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def alt_sec_id(self,) -> Optional[str]:
        """
        Gets the altSecId property value. The altSecId property
        Returns: Optional[str]
        """
        return self._alt_sec_id
    
    @alt_sec_id.setter
    def alt_sec_id(self,value: Optional[str] = None) -> None:
        """
        Sets the altSecId property value. The altSecId property
        Args:
            value: Value to set for the altSecId property.
        """
        self._alt_sec_id = value
    
    @property
    def connected_organization(self,) -> Optional[connected_organization.ConnectedOrganization]:
        """
        Gets the connectedOrganization property value. The connected organization of the subject. Read-only. Nullable.
        Returns: Optional[connected_organization.ConnectedOrganization]
        """
        return self._connected_organization
    
    @connected_organization.setter
    def connected_organization(self,value: Optional[connected_organization.ConnectedOrganization] = None) -> None:
        """
        Sets the connectedOrganization property value. The connected organization of the subject. Read-only. Nullable.
        Args:
            value: Value to set for the connectedOrganization property.
        """
        self._connected_organization = value
    
    @property
    def connected_organization_id(self,) -> Optional[str]:
        """
        Gets the connectedOrganizationId property value. The identifier of the connected organization of the subject.
        Returns: Optional[str]
        """
        return self._connected_organization_id
    
    @connected_organization_id.setter
    def connected_organization_id(self,value: Optional[str] = None) -> None:
        """
        Sets the connectedOrganizationId property value. The identifier of the connected organization of the subject.
        Args:
            value: Value to set for the connectedOrganizationId property.
        """
        self._connected_organization_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageSubject and sets the default values.
        """
        super().__init__()
        # The altSecId property
        self._alt_sec_id: Optional[str] = None
        # The connected organization of the subject. Read-only. Nullable.
        self._connected_organization: Optional[connected_organization.ConnectedOrganization] = None
        # The identifier of the connected organization of the subject.
        self._connected_organization_id: Optional[str] = None
        # The display name of the subject.
        self._display_name: Optional[str] = None
        # The email address of the subject.
        self._email: Optional[str] = None
        # The object identifier of the subject. null if the subject is not yet a user in the tenant.
        self._object_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The onPremisesSecurityIdentifier property
        self._on_premises_security_identifier: Optional[str] = None
        # The principal name, if known, of the subject.
        self._principal_name: Optional[str] = None
        # The subjectLifecycle property
        self._subject_lifecycle: Optional[access_package_subject_lifecycle.AccessPackageSubjectLifecycle] = None
        # The resource type of the subject.
        self._type: Optional[str] = None
    
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
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the subject.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the subject.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address of the subject.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address of the subject.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alt_sec_id": lambda n : setattr(self, 'alt_sec_id', n.get_str_value()),
            "connected_organization": lambda n : setattr(self, 'connected_organization', n.get_object_value(connected_organization.ConnectedOrganization)),
            "connected_organization_id": lambda n : setattr(self, 'connected_organization_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "object_id": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "on_premises_security_identifier": lambda n : setattr(self, 'on_premises_security_identifier', n.get_str_value()),
            "principal_name": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "subject_lifecycle": lambda n : setattr(self, 'subject_lifecycle', n.get_enum_value(access_package_subject_lifecycle.AccessPackageSubjectLifecycle)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def object_id(self,) -> Optional[str]:
        """
        Gets the objectId property value. The object identifier of the subject. null if the subject is not yet a user in the tenant.
        Returns: Optional[str]
        """
        return self._object_id
    
    @object_id.setter
    def object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the objectId property value. The object identifier of the subject. null if the subject is not yet a user in the tenant.
        Args:
            value: Value to set for the objectId property.
        """
        self._object_id = value
    
    @property
    def on_premises_security_identifier(self,) -> Optional[str]:
        """
        Gets the onPremisesSecurityIdentifier property value. The onPremisesSecurityIdentifier property
        Returns: Optional[str]
        """
        return self._on_premises_security_identifier
    
    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesSecurityIdentifier property value. The onPremisesSecurityIdentifier property
        Args:
            value: Value to set for the onPremisesSecurityIdentifier property.
        """
        self._on_premises_security_identifier = value
    
    @property
    def principal_name(self,) -> Optional[str]:
        """
        Gets the principalName property value. The principal name, if known, of the subject.
        Returns: Optional[str]
        """
        return self._principal_name
    
    @principal_name.setter
    def principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the principalName property value. The principal name, if known, of the subject.
        Args:
            value: Value to set for the principalName property.
        """
        self._principal_name = value
    
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
    
    @property
    def subject_lifecycle(self,) -> Optional[access_package_subject_lifecycle.AccessPackageSubjectLifecycle]:
        """
        Gets the subjectLifecycle property value. The subjectLifecycle property
        Returns: Optional[access_package_subject_lifecycle.AccessPackageSubjectLifecycle]
        """
        return self._subject_lifecycle
    
    @subject_lifecycle.setter
    def subject_lifecycle(self,value: Optional[access_package_subject_lifecycle.AccessPackageSubjectLifecycle] = None) -> None:
        """
        Sets the subjectLifecycle property value. The subjectLifecycle property
        Args:
            value: Value to set for the subjectLifecycle property.
        """
        self._subject_lifecycle = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The resource type of the subject.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The resource type of the subject.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

