from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_connection = lazy_import('msgraph.generated.models.teamwork_connection')
teamwork_peripheral = lazy_import('msgraph.generated.models.teamwork_peripheral')

class TeamworkPeripheralHealth(AdditionalDataHolder, Parsable):
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
    def connection(self,) -> Optional[teamwork_connection.TeamworkConnection]:
        """
        Gets the connection property value. The connected state and time since the peripheral device was connected.
        Returns: Optional[teamwork_connection.TeamworkConnection]
        """
        return self._connection
    
    @connection.setter
    def connection(self,value: Optional[teamwork_connection.TeamworkConnection] = None) -> None:
        """
        Sets the connection property value. The connected state and time since the peripheral device was connected.
        Args:
            value: Value to set for the connection property.
        """
        self._connection = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkPeripheralHealth and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The connected state and time since the peripheral device was connected.
        self._connection: Optional[teamwork_connection.TeamworkConnection] = None
        # True if the peripheral is optional. Used for health computation.
        self._is_optional: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The peripheral property
        self._peripheral: Optional[teamwork_peripheral.TeamworkPeripheral] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkPeripheralHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkPeripheralHealth
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkPeripheralHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connection": lambda n : setattr(self, 'connection', n.get_object_value(teamwork_connection.TeamworkConnection)),
            "is_optional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "peripheral": lambda n : setattr(self, 'peripheral', n.get_object_value(teamwork_peripheral.TeamworkPeripheral)),
        }
        return fields
    
    @property
    def is_optional(self,) -> Optional[bool]:
        """
        Gets the isOptional property value. True if the peripheral is optional. Used for health computation.
        Returns: Optional[bool]
        """
        return self._is_optional
    
    @is_optional.setter
    def is_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOptional property value. True if the peripheral is optional. Used for health computation.
        Args:
            value: Value to set for the isOptional property.
        """
        self._is_optional = value
    
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
    def peripheral(self,) -> Optional[teamwork_peripheral.TeamworkPeripheral]:
        """
        Gets the peripheral property value. The peripheral property
        Returns: Optional[teamwork_peripheral.TeamworkPeripheral]
        """
        return self._peripheral
    
    @peripheral.setter
    def peripheral(self,value: Optional[teamwork_peripheral.TeamworkPeripheral] = None) -> None:
        """
        Sets the peripheral property value. The peripheral property
        Args:
            value: Value to set for the peripheral property.
        """
        self._peripheral = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("connection", self.connection)
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("peripheral", self.peripheral)
        writer.write_additional_data_value(self.additional_data)
    

