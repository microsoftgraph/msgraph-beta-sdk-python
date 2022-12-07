from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class GovernanceSubject(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new governanceSubject and sets the default values.
        """
        super().__init__()
        # The display name of the subject.
        self._display_name: Optional[str] = None
        # The email address of the user subject. If the subject is in other types, it is empty.
        self._email: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The principal name of the user subject. If the subject is in other types, it is empty.
        self._principal_name: Optional[str] = None
        # The type of the subject. The value can be User, Group, and ServicePrincipal.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GovernanceSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceSubject
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GovernanceSubject()
    
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
        Gets the email property value. The email address of the user subject. If the subject is in other types, it is empty.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address of the user subject. If the subject is in other types, it is empty.
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
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "principal_name": lambda n : setattr(self, 'principal_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def principal_name(self,) -> Optional[str]:
        """
        Gets the principalName property value. The principal name of the user subject. If the subject is in other types, it is empty.
        Returns: Optional[str]
        """
        return self._principal_name
    
    @principal_name.setter
    def principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the principalName property value. The principal name of the user subject. If the subject is in other types, it is empty.
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("principalName", self.principal_name)
        writer.write_str_value("type", self.type)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type of the subject. The value can be User, Group, and ServicePrincipal.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type of the subject. The value can be User, Group, and ServicePrincipal.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

