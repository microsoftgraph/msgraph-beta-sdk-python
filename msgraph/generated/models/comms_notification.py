from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_type

class CommsNotification(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new commsNotification and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The changeType property
        self._change_type: Optional[change_type.ChangeType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # URI of the resource that was changed.
        self._resource_url: Optional[str] = None
    
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
    
    @property
    def change_type(self,) -> Optional[change_type.ChangeType]:
        """
        Gets the changeType property value. The changeType property
        Returns: Optional[change_type.ChangeType]
        """
        return self._change_type
    
    @change_type.setter
    def change_type(self,value: Optional[change_type.ChangeType] = None) -> None:
        """
        Sets the changeType property value. The changeType property
        Args:
            value: Value to set for the change_type property.
        """
        self._change_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommsNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommsNotification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommsNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_type

        fields: Dict[str, Callable[[Any], None]] = {
            "changeType": lambda n : setattr(self, 'change_type', n.get_enum_value(change_type.ChangeType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceUrl": lambda n : setattr(self, 'resource_url', n.get_str_value()),
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
    
    @property
    def resource_url(self,) -> Optional[str]:
        """
        Gets the resourceUrl property value. URI of the resource that was changed.
        Returns: Optional[str]
        """
        return self._resource_url
    
    @resource_url.setter
    def resource_url(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceUrl property value. URI of the resource that was changed.
        Args:
            value: Value to set for the resource_url property.
        """
        self._resource_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("changeType", self.change_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceUrl", self.resource_url)
        writer.write_additional_data_value(self.additional_data)
    

