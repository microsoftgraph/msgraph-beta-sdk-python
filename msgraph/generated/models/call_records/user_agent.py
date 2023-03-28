from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import client_user_agent, service_user_agent

class UserAgent(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new userAgent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identifies the version of application software used by this endpoint.
        self._application_version: Optional[str] = None
        # User-agent header value reported by this endpoint.
        self._header_value: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def application_version(self,) -> Optional[str]:
        """
        Gets the applicationVersion property value. Identifies the version of application software used by this endpoint.
        Returns: Optional[str]
        """
        return self._application_version
    
    @application_version.setter
    def application_version(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationVersion property value. Identifies the version of application software used by this endpoint.
        Args:
            value: Value to set for the application_version property.
        """
        self._application_version = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserAgent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.callRecords.clientUserAgent":
                from . import client_user_agent

                return client_user_agent.ClientUserAgent()
            if mapping_value == "#microsoft.graph.callRecords.serviceUserAgent":
                from . import service_user_agent

                return service_user_agent.ServiceUserAgent()
        return UserAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import client_user_agent, service_user_agent

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationVersion": lambda n : setattr(self, 'application_version', n.get_str_value()),
            "headerValue": lambda n : setattr(self, 'header_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def header_value(self,) -> Optional[str]:
        """
        Gets the headerValue property value. User-agent header value reported by this endpoint.
        Returns: Optional[str]
        """
        return self._header_value
    
    @header_value.setter
    def header_value(self,value: Optional[str] = None) -> None:
        """
        Sets the headerValue property value. User-agent header value reported by this endpoint.
        Args:
            value: Value to set for the header_value property.
        """
        self._header_value = value
    
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
        writer.write_str_value("applicationVersion", self.application_version)
        writer.write_str_value("headerValue", self.header_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

