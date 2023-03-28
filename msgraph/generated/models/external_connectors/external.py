from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import external_connection
    from ..industry_data import industry_data_root

class External(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new External and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The connections property
        self._connections: Optional[List[external_connection.ExternalConnection]] = None
        # The industryData property
        self._industry_data: Optional[industry_data_root.IndustryDataRoot] = None
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
    def connections(self,) -> Optional[List[external_connection.ExternalConnection]]:
        """
        Gets the connections property value. The connections property
        Returns: Optional[List[external_connection.ExternalConnection]]
        """
        return self._connections
    
    @connections.setter
    def connections(self,value: Optional[List[external_connection.ExternalConnection]] = None) -> None:
        """
        Sets the connections property value. The connections property
        Args:
            value: Value to set for the connections property.
        """
        self._connections = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> External:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: External
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return External()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import external_connection
        from ..industry_data import industry_data_root

        fields: Dict[str, Callable[[Any], None]] = {
            "connections": lambda n : setattr(self, 'connections', n.get_collection_of_object_values(external_connection.ExternalConnection)),
            "industryData": lambda n : setattr(self, 'industry_data', n.get_object_value(industry_data_root.IndustryDataRoot)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def industry_data(self,) -> Optional[industry_data_root.IndustryDataRoot]:
        """
        Gets the industryData property value. The industryData property
        Returns: Optional[industry_data_root.IndustryDataRoot]
        """
        return self._industry_data
    
    @industry_data.setter
    def industry_data(self,value: Optional[industry_data_root.IndustryDataRoot] = None) -> None:
        """
        Sets the industryData property value. The industryData property
        Args:
            value: Value to set for the industry_data property.
        """
        self._industry_data = value
    
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
        writer.write_collection_of_object_values("connections", self.connections)
        writer.write_object_value("industryData", self.industry_data)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

