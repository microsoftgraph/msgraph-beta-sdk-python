from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ClaimsMapping(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new claimsMapping and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The claim that provides the display name or full name for the user. It is a required propoerty.
        self._display_name: Optional[str] = None
        # The claim that provides the email address of the user.
        self._email: Optional[str] = None
        # The claim that provides the first name of the user.
        self._given_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The claim that provides the last name of the user.
        self._surname: Optional[str] = None
        # The claim that provides the unique identifier for the signed-in user. It is a required propoerty.
        self._user_id: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClaimsMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClaimsMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClaimsMapping()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The claim that provides the display name or full name for the user. It is a required propoerty.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The claim that provides the display name or full name for the user. It is a required propoerty.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The claim that provides the email address of the user.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The claim that provides the email address of the user.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        return fields
    
    @property
    def given_name(self,) -> Optional[str]:
        """
        Gets the givenName property value. The claim that provides the first name of the user.
        Returns: Optional[str]
        """
        return self._given_name
    
    @given_name.setter
    def given_name(self,value: Optional[str] = None) -> None:
        """
        Sets the givenName property value. The claim that provides the first name of the user.
        Args:
            value: Value to set for the given_name property.
        """
        self._given_name = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("surname", self.surname)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def surname(self,) -> Optional[str]:
        """
        Gets the surname property value. The claim that provides the last name of the user.
        Returns: Optional[str]
        """
        return self._surname
    
    @surname.setter
    def surname(self,value: Optional[str] = None) -> None:
        """
        Sets the surname property value. The claim that provides the last name of the user.
        Args:
            value: Value to set for the surname property.
        """
        self._surname = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The claim that provides the unique identifier for the signed-in user. It is a required propoerty.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The claim that provides the unique identifier for the signed-in user. It is a required propoerty.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    

