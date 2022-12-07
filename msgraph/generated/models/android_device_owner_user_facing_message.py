from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class AndroidDeviceOwnerUserFacingMessage(AdditionalDataHolder, Parsable):
    """
    Represents a user-facing message with locale information as well as a default message to be used if the user's locale doesn't match with any of the localized messages
    """
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
        Instantiates a new androidDeviceOwnerUserFacingMessage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The default message displayed if the user's locale doesn't match with any of the localized messages
        self._default_message: Optional[str] = None
        # The list of <locale, message> pairs. This collection can contain a maximum of 500 elements.
        self._localized_messages: Optional[List[key_value_pair.KeyValuePair]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceOwnerUserFacingMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerUserFacingMessage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidDeviceOwnerUserFacingMessage()
    
    @property
    def default_message(self,) -> Optional[str]:
        """
        Gets the defaultMessage property value. The default message displayed if the user's locale doesn't match with any of the localized messages
        Returns: Optional[str]
        """
        return self._default_message
    
    @default_message.setter
    def default_message(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultMessage property value. The default message displayed if the user's locale doesn't match with any of the localized messages
        Args:
            value: Value to set for the defaultMessage property.
        """
        self._default_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_message": lambda n : setattr(self, 'default_message', n.get_str_value()),
            "localized_messages": lambda n : setattr(self, 'localized_messages', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def localized_messages(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the localizedMessages property value. The list of <locale, message> pairs. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._localized_messages
    
    @localized_messages.setter
    def localized_messages(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the localizedMessages property value. The list of <locale, message> pairs. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the localizedMessages property.
        """
        self._localized_messages = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("defaultMessage", self.default_message)
        writer.write_collection_of_object_values("localizedMessages", self.localized_messages)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

