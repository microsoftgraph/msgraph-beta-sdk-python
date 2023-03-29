from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import custom_extension_callout_instance_status

class CustomExtensionCalloutInstance(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new customExtensionCalloutInstance and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identification of the custom extension that was triggered at this instance.
        self._custom_extension_id: Optional[str] = None
        # Details provided by the logic app during the callback of the request instance.
        self._detail: Optional[str] = None
        # The unique run identifier for the logic app.
        self._external_correlation_id: Optional[str] = None
        # Unique identifier for the callout instance. Read-only.
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status of the request to the custom extension. The possible values are: calloutSent, callbackReceived, calloutFailed, callbackTimedOut, waitingForCallback, unknownFutureValue.
        self._status: Optional[custom_extension_callout_instance_status.CustomExtensionCalloutInstanceStatus] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionCalloutInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCalloutInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionCalloutInstance()
    
    @property
    def custom_extension_id(self,) -> Optional[str]:
        """
        Gets the customExtensionId property value. Identification of the custom extension that was triggered at this instance.
        Returns: Optional[str]
        """
        return self._custom_extension_id
    
    @custom_extension_id.setter
    def custom_extension_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customExtensionId property value. Identification of the custom extension that was triggered at this instance.
        Args:
            value: Value to set for the custom_extension_id property.
        """
        self._custom_extension_id = value
    
    @property
    def detail(self,) -> Optional[str]:
        """
        Gets the detail property value. Details provided by the logic app during the callback of the request instance.
        Returns: Optional[str]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[str] = None) -> None:
        """
        Sets the detail property value. Details provided by the logic app during the callback of the request instance.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def external_correlation_id(self,) -> Optional[str]:
        """
        Gets the externalCorrelationId property value. The unique run identifier for the logic app.
        Returns: Optional[str]
        """
        return self._external_correlation_id
    
    @external_correlation_id.setter
    def external_correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalCorrelationId property value. The unique run identifier for the logic app.
        Args:
            value: Value to set for the external_correlation_id property.
        """
        self._external_correlation_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import custom_extension_callout_instance_status

        fields: Dict[str, Callable[[Any], None]] = {
            "customExtensionId": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "externalCorrelationId": lambda n : setattr(self, 'external_correlation_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(custom_extension_callout_instance_status.CustomExtensionCalloutInstanceStatus)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Unique identifier for the callout instance. Read-only.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Unique identifier for the callout instance. Read-only.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
        writer.write_str_value("customExtensionId", self.custom_extension_id)
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("externalCorrelationId", self.external_correlation_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[custom_extension_callout_instance_status.CustomExtensionCalloutInstanceStatus]:
        """
        Gets the status property value. The status of the request to the custom extension. The possible values are: calloutSent, callbackReceived, calloutFailed, callbackTimedOut, waitingForCallback, unknownFutureValue.
        Returns: Optional[custom_extension_callout_instance_status.CustomExtensionCalloutInstanceStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[custom_extension_callout_instance_status.CustomExtensionCalloutInstanceStatus] = None) -> None:
        """
        Sets the status property value. The status of the request to the custom extension. The possible values are: calloutSent, callbackReceived, calloutFailed, callbackTimedOut, waitingForCallback, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

