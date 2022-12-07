from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TenantContactInformation(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new tenantContactInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The email address for the contact. Optional
        self._email: Optional[str] = None
        # The name for the contact. Required.
        self._name: Optional[str] = None
        # The notes associated with the contact. Optional
        self._notes: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The phone number for the contact. Optional.
        self._phone: Optional[str] = None
        # The title for the contact. Required.
        self._title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantContactInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantContactInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantContactInformation()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address for the contact. Optional
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address for the contact. Optional
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
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name for the contact. Required.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name for the contact. Required.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. The notes associated with the contact. Optional
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. The notes associated with the contact. Optional
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def phone(self,) -> Optional[str]:
        """
        Gets the phone property value. The phone number for the contact. Optional.
        Returns: Optional[str]
        """
        return self._phone
    
    @phone.setter
    def phone(self,value: Optional[str] = None) -> None:
        """
        Sets the phone property value. The phone number for the contact. Optional.
        Args:
            value: Value to set for the phone property.
        """
        self._phone = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("email", self.email)
        writer.write_str_value("name", self.name)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title for the contact. Required.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title for the contact. Required.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

