from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class CustomExtensionClientConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new customExtensionClientConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The max duration in milliseconds that Azure AD will wait for a response from the logic app before it shuts down the connection. The valid range is between 200 and 2000 milliseconds. Default duration is 1000.
        self._timeout_in_milliseconds: Optional[int] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionClientConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionClientConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionClientConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeoutInMilliseconds": lambda n : setattr(self, 'timeout_in_milliseconds', n.get_int_value()),
        }
        return fields
    
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("timeoutInMilliseconds", self.timeout_in_milliseconds)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def timeout_in_milliseconds(self,) -> Optional[int]:
        """
        Gets the timeoutInMilliseconds property value. The max duration in milliseconds that Azure AD will wait for a response from the logic app before it shuts down the connection. The valid range is between 200 and 2000 milliseconds. Default duration is 1000.
        Returns: Optional[int]
        """
        return self._timeout_in_milliseconds
    
    @timeout_in_milliseconds.setter
    def timeout_in_milliseconds(self,value: Optional[int] = None) -> None:
        """
        Sets the timeoutInMilliseconds property value. The max duration in milliseconds that Azure AD will wait for a response from the logic app before it shuts down the connection. The valid range is between 200 and 2000 milliseconds. Default duration is 1000.
        Args:
            value: Value to set for the timeout_in_milliseconds property.
        """
        self._timeout_in_milliseconds = value
    

