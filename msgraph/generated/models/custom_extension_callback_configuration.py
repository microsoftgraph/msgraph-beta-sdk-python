from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CustomExtensionCallbackConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new customExtensionCallbackConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Callback time out in ISO 8601 time duration. Accepted time durations are between five minutes to three hours. For example, PT5M for five minutes and PT3H for three hours.
        self._timeout_duration: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionCallbackConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCallbackConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionCallbackConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeout_duration": lambda n : setattr(self, 'timeout_duration', n.get_object_value(Timedelta)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("timeoutDuration", self.timeout_duration)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def timeout_duration(self,) -> Optional[Timedelta]:
        """
        Gets the timeoutDuration property value. Callback time out in ISO 8601 time duration. Accepted time durations are between five minutes to three hours. For example, PT5M for five minutes and PT3H for three hours.
        Returns: Optional[Timedelta]
        """
        return self._timeout_duration
    
    @timeout_duration.setter
    def timeout_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the timeoutDuration property value. Callback time out in ISO 8601 time duration. Accepted time durations are between five minutes to three hours. For example, PT5M for five minutes and PT3H for three hours.
        Args:
            value: Value to set for the timeoutDuration property.
        """
        self._timeout_duration = value
    

